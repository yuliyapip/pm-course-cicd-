from app import add, greet, multiply


def test_add():
    """Проверяет, что 2 + 3 = 5."""
    assert add(2, 3) == 5


def test_greet():
    """Проверяет, что greet('PM') возвращает 'Hello, PM!'."""
    assert greet("PM") == "Hello, PM!"

def test_multiply():
    """Проверяет, что 2 * 3 = 6."""
    assert multiply(2, 3) == 6
