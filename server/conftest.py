import pytest
from pytest_factoryboy import register
from rest_framework.test import APIClient

from server.apps.account.tests import UserFactory


@pytest.fixture
def api_client() -> APIClient:
    return APIClient()


# Register factories
register(UserFactory)
