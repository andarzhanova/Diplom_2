import requests
import allure
from data.urls_constants import UrlsConstants


@allure.feature('Получение заказов конкретного пользователя')
class TestGetUserOrders:
    @allure.title('Проверка получения заказов авторизованного пользователя')
    @allure.description(
        'Отправляем запрос, который получает заказы авторизованного пользователя и проверяем, '
        'что вернулись ожидаемые код и тело ответа об успешном получении заказов'
    )
    def test_get_user_orders_authorized_user_success(self, user_token):
        token = user_token
        response = requests.get(UrlsConstants.ORDER, headers={'Authorization': token})
        assert response.status_code == 200 and response.json()['success']

    @allure.title('Проверка получения заказов неавторизованного пользователя')
    @allure.description(
        'Отправляем запрос, который получает заказы неавторизованного пользователя и проверяем, '
        'что вернулись ожидаемые код и тело ответа об ошибке'
    )
    def test_get_user_orders_unauthorized_user_error(self):
        token = None
        response = requests.get(UrlsConstants.ORDER, headers={'Authorization': token})
        assert response.status_code == 401 and response.text == '{"success":false,"message":"You should be authorised"}'
