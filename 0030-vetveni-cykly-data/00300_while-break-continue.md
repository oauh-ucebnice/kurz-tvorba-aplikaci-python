# Další možnosti cyklů – while, break, continue

## Cyklus while

`while` opakuje blok kódu, dokud je podmínka pravdivá – na rozdíl od `for` předem nevíš, kolikrát se cyklus provede.

```python
cislo = 1

while cislo <= 5:
    print(cislo)
    cislo = cislo + 1
```

> Nezapomeň uvnitř cyklu měnit proměnnou, kterou testuješ v podmínce (`cislo = cislo + 1`). Pokud na to zapomeneš, podmínka zůstane pořád pravdivá a vznikne nekonečný cyklus.

## Cyklus řízený uživatelem

`while` se často používá, když se má opakovat, dokud uživatel nezadá konkrétní hodnotu:

```python
soucet = 0
cislo = int(input("Zadej číslo (0 pro konec): "))

while cislo != 0:
    soucet = soucet + cislo
    cislo = int(input("Zadej číslo (0 pro konec): "))

print(f"Součet je {soucet}")
```

## break – okamžité ukončení cyklu

```python
while True:
    cislo = int(input("Zadej číslo (0 pro konec): "))
    if cislo == 0:
        break
    print(cislo)
```

`break` cyklus okamžitě ukončí, i kdyby podmínka `while True` byla stále pravdivá.

## continue – přeskočení zbytku iterace

```python
for cislo in range(1, 6):
    if cislo == 3:
        continue
    print(cislo)  # vypíše 1, 2, 4, 5 – trojku přeskočí
```

`continue` přeskočí zbytek těla cyklu a pokračuje rovnou další iterací.

## Časté chyby
- Zapomenutá aktualizace proměnné v podmínce `while` – nekonečný cyklus.
- Záměna `break` a `continue` – `break` cyklus ukončí úplně, `continue` jen přeskočí aktuální iteraci.
- `while True` bez `break` uvnitř – program se nikdy nezastaví.

## AI Copilot
Zkus se AI zeptat:
- „Jaký je rozdíl mezi break a continue?“
- „Jak se vyhnu nekonečnému cyklu?“

> I tady platí: kód od AI si vždy ověř – pokud program „zamrzne“ a nic se neděje, pravděpodobně jsi narazil/a na nekonečný cyklus. Ukonči ho v terminálu klávesou `Ctrl+C`.
