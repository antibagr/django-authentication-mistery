from typing import Any, Dict, List, Union

from _pytest.main import Session  # Session Type
from pytest_django.fixtures import SettingsWrapper as Settings
from django.contrib.auth import get_user_model
from django.core.mail.message import EmailMultiAlternatives as Mail
from django.test import Client  # Client fixture type
from django.utils.safestring import SafeText
# from django.http.response import HttpResponse
from factory.base import FactoryMetaClass as Factory  # Fake data factory
from py._path.local import LocalPath

JSONContent = Union[str, int, float, bool, None, Dict[str, Any], List[Any]]

JSONType = Dict[str, JSONContent]

Mailbox = List[Mail]

User = get_user_model()
