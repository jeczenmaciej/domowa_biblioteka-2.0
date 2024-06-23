# domowa_biblioteka-2.0

Aplikacja do zarządzania domową biblioteką, umożliwiająca przechowywanie informacji o książkach, autorach i wypożyczeniach.

## Wymagania

- Python 3.8+
- pip

## Instalacja

1. Sklonuj repozytorium:
git clone https://github.com/jeczenmaciej/domowa_biblioteka-2.0.git
cd domowa_biblioteka-2.0
2. Utwórz i aktywuj wirtualne środowisko:
python -m venv venv
source venv/bin/activate  # Na Windows: venv\Scripts\activate
3. Zainstaluj zależności:
pip install -r requirements.txt
4. Zainicjalizuj bazę danych:
flask db init
flask db migrate
flask db upgrade

## Uruchomienie

Uruchom aplikację komendą:
python run.py

Aplikacja będzie dostępna pod adresem http://localhost:5000.

## Endpointy API

- GET /books - Lista wszystkich książek
- POST /books - Dodanie nowej książki
- POST /loans - Dodanie nowego wypożyczenia
- PUT /loans/<loan_id>/return - Zwrot książki

Więcej informacji o dostępnych endpointach znajdziesz w kodzie źródłowym.
