from django.utils import timezone
from rest_framework import serializers

from server.apps.branch.models import Branch
from server.apps.order.models import Order
from server.apps.user.models import User, UserTypes


class BranchSerializer(serializers.ModelSerializer):
    """Serializer definition for Branch model unified with User."""

    username = serializers.CharField(source="user.username")
    password = serializers.CharField(source="user.password", write_only=True)

    total_profit = serializers.SerializerMethodField(read_only=True)
    current_month_orders = serializers.SerializerMethodField(read_only=True)
    current_month_profit = serializers.SerializerMethodField(read_only=True)
    past_month_orders = serializers.SerializerMethodField(read_only=True)
    past_month_profit = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Branch
        fields = (
            "id",
            "name",
            "username",
            "password",
            "total_profit",
            "current_month_orders",
            "current_month_profit",
            "past_month_orders",
            "past_month_profit",
            "updated_at",
            "created_at",
        )
        read_only_fields = (
            "id",
            "updated_at",
            "created_at",
        )

    def get_total_profit(self, instance):
        """Return total profit of the branch."""
        return Order.objects.filter(branch=instance).get_sum_of_profits()

    def get_current_month_orders(self, instance):
        """Return total orders of the branch in the current month."""
        return Order.objects.filter(branch=instance).filter(created_at__month=timezone.now().month).count()

    def get_current_month_profit(self, instance):
        """Return total profit of the branch in the current month."""
        return (
            Order.objects.filter(branch=instance).filter(created_at__month=timezone.now().month).get_sum_of_profits()
        )

    def get_past_month_orders(self, instance):
        """Return total orders of the branch in the past month."""
        return Order.objects.filter(branch=instance).filter(created_at__month=timezone.now().month - 1).count()

    def get_past_month_profit(self, instance):
        """Return total profit of the branch in the past month."""
        return (
            Order.objects.filter(branch=instance)
            .filter(created_at__month=timezone.now().month - 1)
            .get_sum_of_profits()
        )

    def __init__(self, *args, **kwargs):
        """Custom initialization method."""
        super().__init__(*args, **kwargs)

        if self.instance:
            self.fields["password"].required = False

    def validate_username(self, value):
        """Check if username is unique."""
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("Username already exists.")

        return value

    def create(self, validated_data):
        """Create a user for the branch."""

        user_data = validated_data.pop("user")

        user = User(
            first_name=validated_data.get("name"),
            last_name="Filialı",
            username=user_data.get("username"),
            type=UserTypes.STORE,
        )
        user.set_password(user_data.get("password"))
        user.save()

        validated_data["user"] = user

        return super().create(validated_data)

    def update(self, instance, validated_data):
        """Update user with the branch."""

        user_data = validated_data.pop("user", None)

        if user_data:
            if username := user_data.get("username", None):
                instance.user.username = username
            if password := user_data.get("password", None):
                instance.user.set_password(password)

            instance.user.save()

        return super().update(instance, validated_data)
