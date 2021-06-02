import factory

from django.contrib.auth import get_user_model

from django.utils import timezone


class UserFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = get_user_model()

    email = factory.Sequence(lambda n: "user_%d@mail.com" % n)

    last_login = factory.LazyFunction(timezone.now)
