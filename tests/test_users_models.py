import pytest

from dateutil.relativedelta import relativedelta
from django.db.utils import IntegrityError
from django.utils import timezone

from apps.api.models import SomeUser


@pytest.mark.django_db
def test_users():
    user = SomeUser(
        username='login',
        email='a@a.ru',
    )
    user.save()

    users = SomeUser.objects.all()
    assert len(users) == 1

    with pytest.raises(IntegrityError):
        user1 = SomeUser(
            username='login',
            email='a@a.ru',
        )
        user1.save()


@pytest.mark.django_db
def test_users_create():
    user = SomeUser.create_user(
        username='login',
        email='a@a.ru',
    )

    users = SomeUser.objects.all()
    assert len(users) == 1
