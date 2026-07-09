# Parsování dat ze souboru

## Co je parsování

Vše, co ze souboru přečteš, je text (`str`) – i kdyby v souboru bylo napsané číslo. Parsování znamená převést text na datový typ, se kterým chceš dál pracovat (číslo, pravdivostní hodnotu...).

## Parsování čísel

```python
with open("cisla.txt", "r") as soubor:
    radky = soubor.readlines()

cisla = []
for radek in radky:
    cislo = int(radek.strip())
    cisla.append(cislo)

print(cisla)
print(sum(cisla))
```

> `strip()` musíš použít před `int()` – jinak by v textu zůstal neviditelný znak konce řádku (`\n`) a převod by skončil chybou.

## Parsování logických hodnot

Python nemá vestavěnou funkci, která by text jako `"True"` sama převedla na `bool` – porovnání musíš napsat sám/sama:

```python
radek = "ano"
je_pravda = radek.strip().lower() == "ano"
print(je_pravda)  # True
```

## Časté chyby
- Zapomenutý `strip()` před `int()`/`float()` – způsobí chybu `ValueError`.
- Očekávání, že `bool("False")` vrátí `False` – ve skutečnosti vrátí `True`, protože jakýkoli neprázdný text je v Pythonu pravdivý.
- Chybějící ošetření řádku, který číslo neobsahuje (například prázdný řádek na konci souboru).

## AI Copilot
Zkus se AI zeptat:
- „Jak převedu text ze souboru na číslo?“
- „Proč mi bool('False') vrátí True?“

> I tady platí: kód od AI si vždy ověř – vyzkoušej ho na souboru s různými hodnotami, včetně prázdného řádku.
