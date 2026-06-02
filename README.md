# Staff Filter App – Hausaufgabe

Django-Hausaufgabe zur Filter-Übung mit Mitarbeiterdaten.

## Aufgabe

In `employees_app/views.py` werden QuerySets und Filter eingesetzt, um Mitarbeiterdaten auszuwerten und in `employee_list.html` auszugeben.

## Umgesetzte Filter

- alle Mitarbeiter mit Abteilung und Gehalt anzeigen
- Mitarbeiter mit mehr als 3000 € Gehalt anzeigen
- Anzahl der Mitarbeiter mit 5000 € oder mehr zählen
- Durchschnittsgehalt im Sales-Team berechnen und auf zwei Nachkommastellen runden
- Mitarbeiter anzeigen, die vor dem 1. Januar 2022 eingestellt wurden und nicht zur Abteilung HR gehören

## Lokale Ausführung

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py shell < populate.py
python manage.py runserver
```

Danach im Browser öffnen:

```text
http://127.0.0.1:8000/employees/
```

## Tests

```bash
python manage.py test employees_app
```
