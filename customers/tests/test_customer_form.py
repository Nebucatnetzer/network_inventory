from django.test import Client

import pytest


pytestmark = pytest.mark.django_db


def test_customer_create_view(create_admin_user):
    create_admin_user()
    data = {'name': 'Big Pharma',
            'description': 'Some text.'}
    client = Client()
    client.login(username="pharma-admin", password="password")
    response = client.post('/create/customer/', data)
    assert response.status_code == 302
