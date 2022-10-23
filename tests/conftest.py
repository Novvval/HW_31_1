from datetime import date

import pytest
from pytest_factoryboy import register

from tests.factories import AdFactory, CategoryFactory, LocationFactory, UserFactory

@pytest.fixture()
@pytest.mark.django_db
def member_token(client, django_user_model):
    username = "test_user"
    password = "password"
    role = "member"
    email = "test@mail.com"
    birth_date = date(year=2000, month=1, day=1)

    django_user_model.objects.create_user(username=username, password=password, role=role, birth_date=birth_date, email=email)

    response = client.post("/user/token/",
                           {
                               "username": username,
                               "password": password,
                               "role": role,
                               "email": email,
                               "birth_date": birth_date
                           },
                           format="json")
    return response.data["access"]


@pytest.fixture()
@pytest.mark.django_db
def admin_token(client, django_user_model):
    username = "test_user"
    password = "password"
    role = "admin"
    email = "test@mail.com"
    birth_date = date(year=2000, month=1, day=1)

    django_user_model.objects.create_user(username=username, password=password, role=role, birth_date=birth_date, email=email)

    response = client.post("/user/token/",
                           {
                               "username": username,
                               "password": password,
                               "role": role,
                               "email": email,
                               "birth_date": birth_date
                           },
                           format="json")
    return response.data["access"]


register(CategoryFactory)
register(LocationFactory)
register(UserFactory)
register(AdFactory)
