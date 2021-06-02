import pytest
from pytest_factoryboy import register

from tests import factories
from tests.typehints import Session


@pytest.hookimpl()
def pytest_sessionstart(session: Session) -> None:

    print("Start testing")


# Load fixtures
pytest_plugins = [
    'tests.fixtures'
]


for factory in factories.ALL:
    register(factory)
