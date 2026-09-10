from app import add, greet


def test_add():
    """Проверяет, что 2 + 3 = 5."""
    assert add(2, 3) == 5


def test_greet():
    """Проверяет, что greet('PM') возвращает 'Hello, PM!'."""
    assert greet("PM") == "Hello, PM!"
