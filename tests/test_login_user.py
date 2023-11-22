import requests
import allure
from constants import Constants


@allure.feature('Логин пользователя')
class TestLoginUser:
    @allure.title('Проверка логина под существующим пользователем')
    @allure.description(
        'Отправляем запрос, который авторизует существующего пользователя и проверяем, '
        'что вернулись ожидаемые код и тело ответа об успешной авторизации'
    )
    def test_login_user_existing_user_success(self, user_data):
        payload = user_data
        response = requests.post(Constants.LOGIN_USER, data=payload)
        assert response.status_code == 200 and response.json()['success']

    @allure.title('Проверка ошибки при авторизации пользователя с неверным логином и паролем')
    @allure.description(
        'Отправляем запрос, который авторизует пользователя с неверным логином и паролем и проверяем, '
        'что вернулись ожидаемые код и текст ответа об ошибке'
    )
    def test_login_user_incorrect_email_and_password_error(self, user_data):
        payload = user_data.copy()
        payload["email"] += 'incorrect'
        payload["password"] += 1
        response = requests.post(Constants.LOGIN_USER, data=payload)
        assert response.status_code == 401
        assert response.text == '{"success":false,"message":"email or password are incorrect"}'
