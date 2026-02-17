"""Tiny calculator utility used in CI pipeline demos."""


def add(a: int, b: int) -> int:
    """Return the sum of two integers."""
    return a + b


def is_even(value: int) -> bool:
    """Return True when value is an even integer."""
    return value % 2 == 0
