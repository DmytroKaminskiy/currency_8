from rest_framework.reverse import reverse
from rest_framework.test import APIClient


# @pytest.fixture(scope='module')
# def test_fixture_module():
#     print('START TEST FIXTURE')
#     return 1


def test_rates_get(api_client_auth, test_fixture):
    # here
    print('test_rates_get')
    response = api_client_auth.get(reverse('api-v1:rate-list'))
    assert response.status_code == 200
    assert response.json()['count']
    assert response.json()['results']


def test_rates_post_empty(api_client_auth):
    # here
    response = api_client_auth.post(reverse('api-v1:rate-list'), data={})
    assert response.status_code == 400
    assert response.json() == {
        'buy': ['This field is required.'],
        'sale': ['This field is required.'],
        'currency_type': ['This field is required.'],
        'source': ['This field is required.'],
    }
