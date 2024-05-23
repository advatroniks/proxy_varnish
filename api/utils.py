

def get_filename_from_url(url: str) -> str:
    # Разбиваем URL по символу '/'
    parts = url.split('/')
    # Получаем последний элемент, который представляет имя файла
    filename = parts[-1]
    return filename