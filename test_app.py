from app import add, multiply, divide


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0


def test_multiply():
    assert multiply(3, 4) == 12


def test_divide():
    assert divide(10, 2) == 5


def test_divide_by_zero():
    try:
        divide(5, 0)
        assert False
    except ValueError:
        assert True
