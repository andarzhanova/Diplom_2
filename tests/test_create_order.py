import requests
import allure
from constants import Constants


@allure.feature('Создание заказа')
class TestCreateOrder:
    @allure.title('Проверка создания заказа с авторизацией')
    @allure.description(
        'Отправляем запрос с авторизацией, который создаёт заказ и проверяем, '
        'что вернулись ожидаемые код и тело ответа об успешном создании'
    )
    def test_create_order_with_authorization_success(self, user_token):
        token = user_token
        payload = Constants.INGREDIENTS
        response = requests.post(Constants.ORDER, headers={'Authorization': token}, data=payload)
        assert response.status_code == 200 and response.json()['success']

    @allure.title('Проверка создания заказа с ингредиентами без авторизации')
    @allure.description(
        'Отправляем запрос, который создаёт заказ, с ингредиентами, но без авторизациии и проверяем, '
        'что вернулись ожидаемые код и тело ответа об успешном создании'
    )
    def test_create_order_no_authorization_with_ingredients_success(self):
        payload = Constants.INGREDIENTS
        response = requests.post(Constants.ORDER, data=payload)
        assert response.status_code == 200 and response.json()['success']

    @allure.title('Проверка создания заказа без ингредиентов')
    @allure.description(
        'Отправляем запрос, который создаёт заказ, без ингредиентов, и проверяем, '
        'что вернулись ожидаемые код и текст ответа об ошибке'
    )
    def test_create_order_without_ingredients_error(self):
        payload = Constants.WITHOUT_INGREDIENTS
        response = requests.post(Constants.ORDER, data=payload)
        assert response.status_code == 400
        assert response.text == '{"success":false,"message":"Ingredient ids must be provided"}'

    @allure.title('Проверка создания заказа с неверным хешем ингредиентов')
    @allure.description(
        'Отправляем запрос, который создаёт заказ, с неверным хешем ингредиентов и проверяем, '
        'что вернулись ожидаемые код и тело ответа об ошибке'
    )
    def test_create_order_incorrect_ingredients_error(self):
        payload = Constants.INCORRECT_INGREDIENTS
        response = requests.post(Constants.ORDER, data=payload)
        assert response.status_code == 500 and 'Internal Server Error' in response.text
