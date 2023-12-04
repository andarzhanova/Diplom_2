import requests
import allure
from data.urls_constants import UrlsConstants
import helpers


@allure.feature('Изменение данных пользователя')
class TestChangeUserData:
    @allure.title('Проверка изменения данных пользователя с авторизацией')
    @allure.description(
        'Отправляем запрос с авторизацией, который передаёт во все поля новые данные пользователя  '
        'и проверяем, что вернулись ожидаемые код и тело ответа об успешном изменении'
    )
    def test_change_user_data_with_authorization_success(self, user_token):
        token = user_token
        payload = helpers.payload
        response = requests.patch(UrlsConstants.DELETE_USER, headers={'Authorization': token}, data=payload)
        assert response.status_code == 200 and response.json()['success']

    @allure.title('Проверка ошибки при изменении данных пользователя без авторизации')
    @allure.description(
        'Отправляем запрос без авторизации, который передаёт во все поля новые данные пользователя  '
        'и проверяем, что вернулись ожидаемые код и текст ответа об ошибке'
    )
    def test_change_user_data_without_authorization_error(self):
        payload = helpers.payload
        response = requests.patch(UrlsConstants.DELETE_USER, data=payload)
        assert response.status_code == 401
        assert response.text == '{"success":false,"message":"You should be authorised"}'
