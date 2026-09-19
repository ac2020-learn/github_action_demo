from app import add_numbers, divide_numbers, get_weather


def test_add_numbers():
    assert add_numbers(2, 3) == 5
    assert add_numbers(-1, 1) == 0
    assert add_numbers(0, 0) == 0

def test_divide_numbers():
    assert divide_numbers(10, 2) == 5
    assert divide_numbers(-6, 3) == -2
    try:
        divide_numbers(5, 0)
    except ValueError as e:
        assert str(e) == "Cannot divide by zero."

def test_get_weather():
    assert get_weather.invoke("New York") == "The weather in New York1 is sunny."
    assert get_weather.invoke("Los Angeles") == "The weather in Los Angeles1 is sunny."