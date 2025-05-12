import pytest  # Библиотека для написания тестов
from main03 import get_random_cat_image  # Импортируем функцию, которую будем тестировать

# Тест: успешный запрос
def test_get_random_cat_image_success(mocker):
    """
    Проверяет, что функция возвращает корректный URL,
    если API отвечает успешно.
    """
    # Подменяем requests.get на фиктивную версию
    mock_get = mocker.patch('main03.requests.get')

    # Настраиваем поведение фиктивного ответа
    mock_get.return_value.status_code = 200  # Статус OK
    mock_get.return_value.json.return_value = [{
        'id': 'abc123',
        'url': 'https://cdn2.thecatapi.com/images/abc123.jpg'
    }]

    # Вызываем функцию
    result = get_random_cat_image()

    # Проверяем, что результат — ожидаемый URL
    assert result == 'https://cdn2.thecatapi.com/images/abc123.jpg'

# Тест: неуспешный запрос (например, ошибка 404)
def test_get_random_cat_image_failure(mocker):
    """
    Проверяет, что функция возвращает None, если API вернул ошибку.
    """
    # Подменяем requests.get на фиктивную версию
    mock_get = mocker.patch('main03.requests.get')

    # Настраиваем поведение: вернём ошибку 404
    mock_get.return_value.status_code = 404

    # Вызываем функцию
    result = get_random_cat_image()

    # Ожидаем, что в случае ошибки результат будет None
    assert result is None