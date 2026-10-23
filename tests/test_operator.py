
"""Tests des quatre opérations mathématiques de la calculatrice."""

import pytest

from operators import add, subtract, multiply, divide

def test_addition():
    """Vérifie que l'addition de 2 et 3 donne 5."""
    assert add(2, 3) == 5


def test_subtraction():
    """Vérifie que 10 moins 3 donne 7."""
    assert subtract(10, 3) == 7


def test_multiplication():
    """Vérifie que 3 multiplié par 4 donne 12."""
    assert multiply(3, 4) == 12


def test_division():
    """Vérifie qu'une division conserve la partie décimale."""
    assert divide(7, 2) == 3.5


def test_division_by_zero():
    """Vérifie qu'une division par zéro provoque une erreur."""
    with pytest.raises(ZeroDivisionError):
        divide(5, 0)
