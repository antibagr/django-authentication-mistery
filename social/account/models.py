from django.db import models

from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from account.managers import UserManager

class TimeBasedModel(models.Model):

    class Meta:
        abstract = True

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class User(AbstractUser):

    class Meta:
        db_table = 'user'

    objects = UserManager()

    username = None
    email = models.EmailField(_('email address'), unique=True, null=False, blank=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    image = models.ImageField(default='default.jpg', upload_to='user_photos')

    def __str__(self) -> str:
        return self.email

    # def last_seen(self) -> datetime.datetime:
    #     return cache.get(f'last_seen_{self.id}') or None
    #
    # def online(self) -> bool:
    #     return False
        # if self.last_seen():
        #     return datetime.datetime.now() < (self.last_seen() + datetime.timedelta(seconds=settings.USER_ONLINE_TIMEOUT))
        # return False
