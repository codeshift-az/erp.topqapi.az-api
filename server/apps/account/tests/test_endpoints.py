import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from server.apps.user.models import User

pytestmark = pytest.mark.django_db


def test_account_unauthorized(api_client: APIClient) -> None:
    """Test account endpoint unauthorized request."""

    url = reverse("account:account")

    response = api_client.get(url)
    assert response.status_code == status.HTTP_401_UNAUTHORIZED

    response = api_client.put(url)
    assert response.status_code == status.HTTP_401_UNAUTHORIZED

    response = api_client.delete(url)
    assert response.status_code == status.HTTP_401_UNAUTHORIZED


def test_account_get(api_client: APIClient, user: User) -> None:
    """Test account endpoint get request."""

    url = reverse("account:account")

    api_client.force_authenticate(user=user)

    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK

    assert response.data["first_name"] == user.first_name
    assert response.data["last_name"] == user.last_name

    assert "password" not in response.data


def test_account_put(api_client: APIClient, user: User) -> None:
    """Test account endpoint put request."""

    url = reverse("account:account")

    api_client.force_authenticate(user=user)

    user_data = {
        "first_name": "Test2",
        "last_name": "Test2",
        "username": "test2",
        "email": "test@example.com",
    }

    response = api_client.put(url, user_data)
    assert response.status_code == status.HTTP_200_OK

    user.refresh_from_db()

    assert response.data["first_name"] == user.first_name == user_data["first_name"]
    assert response.data["last_name"] == user.last_name == user_data["last_name"]

    assert "password" not in response.data


def test_account_delete(api_client: APIClient, user: User) -> None:
    """Test account endpoint delete request."""

    url = reverse("account:account")

    api_client.force_authenticate(user=user)

    response = api_client.delete(url)
    assert response.status_code == status.HTTP_204_NO_CONTENT

    assert User.objects.filter(pk=user.pk).exists() is False
