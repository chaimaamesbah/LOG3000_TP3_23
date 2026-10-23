
"""Tests du serveur Flask, des expressions et de l'interface HTML."""

import pytest

from app import app, calculate


@pytest.fixture
def client():
    """
    Crée un client Flask pour simuler les requêtes HTTP.

    Yields:
        FlaskClient: Client de test de l'application.
    """
    app.config["TESTING"] = True
    with app.test_client() as test_client:
        yield test_client


def test_valid_expression():
    """Vérifie le calcul d'une expression avec des espaces."""
    assert calculate(" 8 + 2 ") == 10


@pytest.mark.parametrize("expression", ["", "8+", "8+2+3", "abc"])
def test_invalid_expression(expression):
    """
    Vérifie que les expressions invalides sont rejetées.

    Args:
        expression (str) : expression invalide à tester
    """
    with pytest.raises(ValueError):
        calculate(expression)


def test_home_page(client):
    """
    Vérifie que la page de la calculatrice s'affiche.

    Args:
        client : client de test Flask
    """
    response = client.get("/")
    assert response.status_code == 200
    assert b"Flask Calculator" in response.data


def test_form_calculation(client):
    """
    Vérifie qu'un calcul envoyé au serveur apparaît dans la page.

    Args:
        client : client de test Flask
    """
    response = client.post("/", data={"display": "8+2"})
    assert response.status_code == 200
    assert 'value="10.0"' in response.get_data(as_text=True)


def test_form_error(client):
    """
    Vérifie qu'une expression incomplète affiche une erreur.

    Args:
        client : client de test Flask
    """
    response = client.post("/", data={"display": "8+"})
    assert response.status_code == 200
    assert "Error:" in response.get_data(as_text=True)


@pytest.mark.parametrize("valeur", ["2", "8", "*", "/"])
def test_button_label(client, valeur):
    """
    Vérifie que le texte du bouton correspond à sa valeur.

    Args:
        client : client de test Flask
        valeur (str) : chiffre ou opérateur à vérifier 
    """
    page = client.get("/").get_data(as_text=True)
    assert f'''onclick="appendToDisplay('{valeur}')">{valeur}</button>''' in page
