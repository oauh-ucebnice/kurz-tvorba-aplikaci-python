# Cyklus for

## Co je cyklus

Cyklus (smyčka) umožňuje opakovat stejný blok kódu víckrát, aniž bys ho musel/a psát znovu a znovu.

## Cyklus for přes rozsah čísel

```python
for cislo in range(5):
    print(cislo)
```

`range(5)` vytvoří posloupnost čísel od `0` do `4` (celkem 5 čísel). Proměnná `cislo` postupně nabývá každé z těchto hodnot.

> `range(5)` začíná od `0`, ne od `1`, a poslední hodnota `5` se do posloupnosti nezahrne.

## range() s vlastním začátkem a krokem

```python
for cislo in range(1, 6):      # 1, 2, 3, 4, 5
    print(cislo)

for cislo in range(0, 10, 2):  # 0, 2, 4, 6, 8
    print(cislo)
```

## Cyklus for přes seznam

Pomocí `for` můžeš procházet i prvky pole (viz lekce [Pole](00400_pole.md)):

```python
jmena = ["Karel", "Petra", "Jan"]

for jmeno in jmena:
    print(f"Ahoj, {jmeno}!")
```

## Časté chyby
- Očekávání, že `range(5)` obsahuje i číslo `5` – poslední hodnota se nezahrnuje.
- Chybějící dvojtečka na konci řádku s `for`.
- Změna proměnné cyklu (`cislo`) uvnitř těla cyklu – nijak neovlivní, kolikrát se cyklus provede.

## AI Copilot
Zkus se AI zeptat:
- „Jak funguje range()?“
- „Jak projdu cyklem for všechny prvky seznamu?“

> I tady platí: kód od AI si vždy ověř – spočítej si ručně, kolikrát by se cyklus měl opakovat, a porovnej to s výstupem programu.
