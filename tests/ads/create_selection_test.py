import pytest


@pytest.mark.django_db
def test_create_selection(client, admin_token, ad, user):
    response = client.post("/selection/create/", {
        "name": "name",
        "owner": user.pk,
        "items": [ad.pk]
    }, content_type="application/json", HTTP_AUTHORIZATION="Bearer " + admin_token)

    assert response.status_code == 201
    assert response.data == {
        "id": 1,
        "name": "name",
        "owner": user.pk,
        "items": [ad.pk]
    }
