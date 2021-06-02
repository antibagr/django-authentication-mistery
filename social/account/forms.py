from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from .models import User


class AccountCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email',)


class AccountUpdateForm(UserChangeForm):

    password = None

    class Meta:
        model = User
        fields = ('email', 'image')
        exclude = ('password',)
