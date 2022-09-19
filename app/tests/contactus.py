from django.urls import reverse
import pytest


def test_contactus_get(client):
    response = client.get(reverse('currency:contactus_create'))
    assert response.status_code == 200


def test_contactus_post_empty(client):
    response = client.post(reverse('currency:contactus_create'), data={})
    assert response.status_code == 200  # error
    assert response.context_data['form'].errors == {
        'from_email': ['This field is required.'],
        'subject': ['This field is required.'],
        'body': ['This field is required.'],
    }


def test_contactus_post_valid(client, mailoutbox):
    data = {
        'from_email': 'example@mail.com',
        'subject': 'subject example',
        'body': 'Body Example',
    }
    response = client.post(reverse('currency:contactus_create'), data=data)
    assert response.status_code == 302  # success
    assert response.headers['Location'] == '/currency/rate/list/'

    assert len(mailoutbox) == 1
    assert mailoutbox[0].subject == 'ContactUs From Currency Project'



@pytest.mark.parametrize('from_email', ('examplemail.com', '12312', 'WAFASEFS'))
def test_contactus_post_invalid_email(client, from_email):
    data = {
        'from_email': from_email,
        'subject': 'subject example',
        'body': 'Body Example',
    }
    response = client.post(reverse('currency:contactus_create'), data=data)
    assert response.status_code == 200
    assert response.context_data['form'].errors == {'from_email': ['Enter a valid email address.']}

# python app/manage.py dumpdata currency.source > source.json
