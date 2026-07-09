# Čtení a zápis obsahu

## Čtení celého souboru – read()

```python
with open("data.txt", "r") as soubor:
    obsah = soubor.read()

print(obsah)
```

`read()` vrátí celý obsah souboru jako jeden řetězec (`str`).

## Čtení po řádcích – readlines()

```python
with open("data.txt", "r") as soubor:
    radky = soubor.readlines()

print(radky)
```

`readlines()` vrátí seznam (`list`), kde každý prvek je jeden řádek souboru – včetně znaku konce řádku `\n` na konci.

```python
for radek in radky:
    print(radek.strip())  # strip() odstraní přebytečné mezery a \n
```

## Zápis do souboru – write()

```python
with open("vysledek.txt", "w") as soubor:
    soubor.write("Ahoj světe!\n")
```

`write()` na rozdíl od `print()` na konec textu sám nepřidá odřádkování – pokud ho chceš, musíš napsat `\n`.

## Časté chyby
- Očekávání, že `write()` přidá nový řádek automaticky, jako to dělá `print()`.
- Zapomenutý `.strip()` u řádků z `readlines()` – text pak obsahuje neviditelný znak `\n` navíc.
- Volání `read()` dvakrát po sobě – podruhé vrátí prázdný řetězec, protože se soubor čte od místa, kde předtím skončil.
- Práce s proměnnou `obsah`/`radky` mimo blok `with` je v pořádku (data už jsou v proměnné), ale volání `soubor.read()` mimo `with` nefunguje – soubor je zavřený.

## AI Copilot
Zkus se AI zeptat:
- „Jaký je rozdíl mezi read() a readlines()?“
- „Proč se mi ve výpisu objevuje prázdný řádek navíc?“

> I tady platí: kód od AI si vždy ověř – vypiš si obsah souboru před úpravou a po ní, ať vidíš, že program dělá přesně to, co má.
