import requests  # Импортируем библиотеку для выполнения HTTP-запросов


def get_random_cat_image():
    """
    Делает запрос к TheCatAPI для получения случайного изображения кошки.

    Возвращает:
        str: URL изображения, если запрос успешен и структура ответа ожидаемая.
        None: если возникла ошибка или структура ответа неожиданная.
    """
    url = "https://api.thecatapi.com/v1/images/search"  # URL для получения случайной кошки

    # Выполняем GET-запрос к API
    response = requests.get(url)

    # Проверяем, что ответ успешный (код 200)
    if response.status_code == 200:
        data = response.json()  # Преобразуем JSON-ответ в Python-объект (обычно это список словарей)

        # Проверяем, что ответ — это список и первый элемент содержит ключ 'url'
        if data and isinstance(data, list) and 'url' in data[0]:
            return data[0]['url']  # Возвращаем URL изображения
        else:
            return None  # Структура ответа неожиданная
    else:
        return None  # Запрос завершился ошибкой