import pytest
import requests
import helpers
from data.urls_constants import UrlsConstants


@pytest.fixture
def registered_user():
    payload = helpers.payload
    response = requests.post(UrlsConstants.CREATE_USER, data=payload)

    yield response
    token = response.json()['accessToken']
    requests.delete(UrlsConstants.DELETE_USER, headers={'Authorization': token})


@pytest.fixture
def user_data():
    payload = helpers.payload
    response = requests.post(UrlsConstants.CREATE_USER, data=payload)

    yield payload
    token = response.json()['accessToken']
    requests.delete(UrlsConstants.DELETE_USER, headers={'Authorization': token})


@pytest.fixture
def user_token():
    payload = helpers.payload
    response = requests.post(UrlsConstants.CREATE_USER, data=payload)
    token = response.json()['accessToken']

    yield token
    requests.delete(UrlsConstants.DELETE_USER, headers={'Authorization': token})
