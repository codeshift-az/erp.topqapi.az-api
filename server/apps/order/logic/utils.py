from django.conf import settings
from django.core.mail import send_mail


def send_status_change_email(order, status):
    """Send email notification to the seller when order status changes."""

    subject = f"Satış №{order.id} - Sifarişin statusu dəyişdirildi"
    body = f"Satış №{order.id} - Sifarişin statusu dəyişdirildi: {status}"
    recipients = []

    if order.seller.email:
        recipients.append(order.seller.email)

    if recipients:
        send_mail(subject=subject, message=body, from_email=settings.EMAIL_HOST_USER, recipient_list=recipients)
