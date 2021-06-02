import pytest

from django.test import TestCase
from django.contrib.auth import get_user_model

from tests.typehints import User

""" FIXTURES """

# Enable database access for all tests
pytestmark = pytest.mark.django_db


""" TESTS """

def test_create_user():
    '''
    Test custom user model with email instead of username.
    '''

    user = User.objects.create_user(email='user@mail.com', password='foo')

    assert user.email == 'user@mail.com'

    assert user.is_active
    assert not user.is_staff
    assert not user.is_superuser

    with pytest.raises(TypeError):
        User.objects.create_user()

    with pytest.raises(TypeError):
        User.objects.create_user(email='')

    with pytest.raises(ValueError):
        User.objects.create_user(email='', password="foo")


def test_create_superuser():
    '''
    Test super user to such user model.
    '''

    admin_user = User.objects.create_superuser('super@mail.com', 'foo')

    assert admin_user.email == 'super@mail.com'

    assert admin_user.is_active
    assert admin_user.is_staff
    assert admin_user.is_superuser

    with pytest.raises(ValueError):
        User.objects.create_superuser(
            email='super@mail.com',
            password='foo',
            is_superuser=False
        )
