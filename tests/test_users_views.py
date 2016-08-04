import pytest
import json

from django.core.urlresolvers import reverse

from apps.api.models import SomeUser


@pytest.mark.urls('apps.api.urls')
def test_ping(client):
    r = client.get(reverse('ping'))
    assert r.status_code == 200
    assert r.json() == {'answer': 'pong'}


@pytest.mark.django_db
def test_list_users(client):
    r = client.get(reverse('api:list_users'))
    assert r.status_code == 200
    assert r.json() == []


@pytest.mark.django_db
def test_create_user(client):
    json_string = json.dumps({'username': 'ololo', 'email': 'a@a.ru'})
    r = client.post(reverse('api:list_users'), json_string, content_type="application/json")

    assert r.status_code == 200
    answer = json.loads(r.json())
    assert answer['username'] == 'ololo'


@pytest.mark.django_db
def test_detail_user(client):
    user = SomeUser(
        username='login1',
        email='a@a.ru',
    )
    user.save()
    r = client.get(reverse('api:detail_user', kwargs={'pk': user.pk}))

    assert r.status_code == 200
    answer = json.loads(r.json())
    assert answer['username'] == 'login1'
    r = client.delete(reverse('api:detail_user', kwargs={'pk': user.pk}))
    assert r.status_code == 204
    with pytest.raises(SomeUser.DoesNotExist):
        g = SomeUser.objects.get(username='login1')

    r = client.put(reverse('api:detail_user', kwargs={'pk': user.pk}))
    assert r.status_code == 200
    r = client.get(reverse('api:detail_user', kwargs={'pk': 150}))
    assert r.status_code == 404


@pytest.mark.django_db
def test_doesnotexist_user(client):
    r = client.get(reverse('api:detail_user', kwargs={'pk': 150}))
    assert r.status_code == 404

