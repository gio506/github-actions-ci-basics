from app import add, is_even


def test_add() -> None:
    assert add(2, 3) == 5


def test_is_even_true() -> None:
    assert is_even(10)


def test_is_even_false() -> None:
    assert not is_even(7)
