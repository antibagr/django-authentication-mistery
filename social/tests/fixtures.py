import os
from unittest import mock

import pytest

from tests.typehints import Client, Factory, User


@pytest.fixture(autouse=True, scope='module')
def mock_recaptcha_environment():
    "Context manager with disabled RECAPTCHA"

    with mock.patch.dict(os.environ, {"RECAPTCHA_DISABLE": "True"}):
        yield

@pytest.fixture
def person() -> User:
    " Return created profile or raise RuntimeError "

    if User.objects.count() == 0:
        raise RuntimeError("No profile were created still")

    return User.objects.first()


@pytest.fixture
def authorized_client(client: Client, user_factory: Factory) -> Client:
    " Return client authorized with profile factory "

    client.force_login(user_factory())
    return client
