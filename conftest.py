import pytest
import requests
import helpers
from constants import Constants


@pytest.fixture
def registered_user():
    payload = helpers.payload
    response = requests.post(Constants.CREATE_USER, data=payload)

    yield response
    token = response.json()['accessToken']
    requests.delete(Constants.DELETE_USER, headers={'Authorization': token})


@pytest.fixture
def user_data():
    payload = helpers.payload
    response = requests.post(Constants.CREATE_USER, data=payload)

    yield payload
    token = response.json()['accessToken']
    requests.delete(Constants.DELETE_USER, headers={'Authorization': token})


@pytest.fixture
def user_token():
    payload = helpers.payload
    response = requests.post(Constants.CREATE_USER, data=payload)
    token = response.json()['accessToken']

    yield token
    requests.delete(Constants.DELETE_USER, headers={'Authorization': token})
