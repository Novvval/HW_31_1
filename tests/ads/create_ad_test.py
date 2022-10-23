import pytest


@pytest.mark.django_db
def test_create_ad(client, admin_token):
    response = client.post("/ad/create/", {
        "name": "test_ad_one",
        "price": 5,
        "description": None,
        "is_published": False,
        "author": 1
    }, content_type="application/json", HTTP_AUTHORIZATION="Bearer " + admin_token)

    assert response.status_code == 201
    assert response.data == {
        "id": 1,
        "name": "test_ad_one",
        "price": 5,
        "description": None,
        "is_published": False,
        "image": None,
        "author": 1,
        "category": None
    }
