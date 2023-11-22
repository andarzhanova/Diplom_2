import pytest
import requests
import allure
import helpers
from constants import Constants


@allure.feature('Создание пользователя')
class TestCreateUser:
    @allure.title('Проверка создания уникального пользователя')
    @allure.description(
        'Отправляем запрос, который создаёт пользователя и проверяем, '
        'что вернулись ожидаемые код и тело ответа об успешном создании'
    )
    def test_create_user_unique_user_success(self, registered_user):
        response = registered_user
        assert response.status_code == 200 and response.json()['success']

    @allure.title('Проверка ошибки при создании пользователя, который уже зарегистрирован')
    @allure.description(
        'Отправляем запросы, которые создают одинаковых пользователей и проверяем, '
        'что вернулись ожидаемые код и текст ответа об ошибке'
    )
    def test_create_user_identical_users_error(self, user_data):
        payload = user_data
        response = requests.post(Constants.CREATE_USER, data=payload)
        assert response.status_code == 403 and response.text == '{"success":false,"message":"User already exists"}'

    @allure.title('Проверка ошибки при создании пользователя без обязательного поля')
    @allure.description(
        'Отправляем запрос, который создаёт пользователя без обязательного поля и проверяем, '
        'что вернулись ожидаемые код и текст ответа об ошибке'
    )
    @pytest.mark.parametrize('field', ['email', 'password', 'name'])
    def test_create_user_no_required_field_error(self, field):
        payload = helpers.payload
        del payload[field]
        response = requests.post(Constants.CREATE_USER, data=payload)
        assert response.status_code == 403
        assert response.text == '{"success":false,"message":"Email, password and name are required fields"}'
