import pytest

from django.urls import reverse


@pytest.mark.django_db
def test_invoice_list_authentication(client, django_user_model):
    response = client.get(reverse('list'))
    assert response.url.startswith('/login/') is True
    assert response.status_code == 302

    user = django_user_model.objects.create_user(
        username='john',
        password='123456')
    user.save()

    client.login(username='john', password='123456')

    response = client.get(reverse('list'))
    assert response.status_code == 200
