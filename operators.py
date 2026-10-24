''' 
Fonctions responsables des opérations arithmétiques de la calculatrice. 
Il est utilisé par app.py pour les calculs. Il ne dépend d'aucune bibliothèque externe.
'''

def add(a,b):
    '''
    Calcule la somme de deux nombres.

    Args: 
        a (float) : premier nombre
        b (float) : deuxième nombre

    Returns :
        float : somme de a et b
    '''
    return a + b

def subtract(a,b):
    '''
    Calcule la différence entre deux nombres.

    Args: 
        a (float) : nombre duquel on soustrait
        b (float) : nombre à soustraire

    Returns :
        float : différence entre a et b
    '''
    return a - b

def multiply(a,b):
    '''
    Calcule le produit de deux nombres.

    Args: 
        a (float) : premier facteur
        b (float) : deuxième facteur

    Returns :
        float : produit de a et b
    '''
    return a * b

def divide(a,b):
    '''
    Calcule le quotient de deux nombres.

    Args: 
        a (float) : dividende
        b (float) : diviseur

    Returns :
        float : quotient de a par b

    Raises:
        ZeroDivisionError : si le diviseur est nul.
    '''
    return a / b