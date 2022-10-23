import pytest

from ads.serializers import AdSerializer


@pytest.mark.django_db
def test_ad_view(client, ad, admin_token):
    response = client.get(f"/ad/{ad.pk}/", content_type="application/json", HTTP_AUTHORIZATION="Bearer " + admin_token)

    assert response.status_code == 200
    assert response.data == AdSerializer(ad).data
