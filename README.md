# Czym jest Maturix?

**Maturix** jest programem, który pozwoli Ci wykorzystać modele językowe do weryfikacji Twojej wiedzy przed egzaminem maturalnym.

## Jak to działa?

Możesz dodawać przykładowe pytania do swoich zbiorów pytań. Służy do tego program **edytor.py**.

Możesz sprawdzić swoją wiedzę na losowych pytaniach z wybranego przez siebie zbioru. Służy do tego program **quiz.py**.

## Jak zacząć?

1. Sklonuj repozytorium.

2. Zainstaluj wymagane biblioteki:
```
pip install gradio groq
```

3. Załóż konto w serwisie [Groq](https://console.groq.com/login).

- Zaloguj się na swoje konto i przejdź do zakładki **API Keys**.
- Wygeneruj nowy klucz API (przycisk "Create API Key") i skopiuj go, np. do pliku tesktowego.

---

## Korzystanie z **edytor.py**

Uruchom program **edytor.py** poleceniem 
```
python edytor.py
```

- W polu "Nazwa arkusza" wpisz nazwę arkusza egzaminacyjnego, np. "Biologia podstawowa 2024".
- W polu "Numer zadania" wpisz wymyślony numer zadania, np. "1.1".
- W polu "Treść zadania" wpisz treść zadania.
- Wybierz z listy maksymalną liczbę punktów za zadanie.
- W polu "Zasady oceniania" wpisz zasady oceniania zadania, np. wg wzoru publikowanego przez CKE.
- W polu "Przykładowe rozwiązania" wpisz właściwe rozwiązanie, lub przykłady rozwiązań, jeśli zadanie jest opisowe.
- W polu "Uwagi" wpisz dodatkowe uwagi do oceniania, tak jak robi to CKE.
- Kliknij przycisk "Submit".

W polu "output" zobaczysz informację o dodanym zadaniu.

---

## Korzystanie z **quiz.py**

Uruchom program **quiz.py** poleceniem 
```
python quiz.py
```

- W polu "Nazwa folderu z zadaniami" wpisz nazwę swojego arkusza egzaminacyjnego, np. "Biologia podstawowa 2024".
- Kliknij przycisk "Wylosuj zadanie".
- W polu "Klucz API Groq" wklej swój klucz do API Groq.
- W polu "Twoja odpowiedź" wpisz swoją odpowiedź na pytanie.
- Kliknij przycisk "Sprawdź".
- Przeczytaj feedback od modelu w polu "Odpowiedź modelu".
