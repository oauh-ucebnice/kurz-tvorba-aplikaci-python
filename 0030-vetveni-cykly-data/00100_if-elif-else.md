# Rozhodování – if, elif, else

## Co je podmínka

Podmínka umožňuje programu reagovat jinak podle toho, jestli je nějaké tvrzení pravdivé, nebo ne.

## if

```python
vek = 15

if vek >= 18:
    print("Jsi plnoletý.")
```

Kód v odsazeném bloku pod `if` se spustí, jen pokud je podmínka pravdivá (`True`).

## else

```python
if vek >= 18:
    print("Jsi plnoletý.")
else:
    print("Ještě nejsi plnoletý.")
```

Blok `else` se spustí, když podmínka u `if` pravdivá není.

## elif

Pokud chceš otestovat víc možností za sebou, použij `elif` (zkratka pro *else if*):

```python
znamka = 2

if znamka == 1:
    print("Výborně!")
elif znamka == 2:
    print("Chvalitebně.")
elif znamka == 3:
    print("Dobře.")
else:
    print("Musíš zabrat.")
```

Python testuje podmínky postupně shora dolů a provede jen první blok, jehož podmínka je pravdivá.

## Porovnávací operátory

| Operátor | Význam |
|---|---|
| `==` | rovná se |
| `!=` | nerovná se |
| `>`, `<` | větší, menší |
| `>=`, `<=` | větší nebo rovno, menší nebo rovno |

> Nezaměňuj `==` (porovnání) s `=` (přiřazení do proměnné). `if vek = 18:` je chyba, správně je `if vek == 18:`.

## Časté chyby
- Záměna `=` a `==` v podmínce.
- Chybějící dvojtečka na konci řádku s `if`/`elif`/`else`.
- Špatné odsazení bloku – Python podle odsazení pozná, co k podmínce patří.

## AI Copilot
Zkus se AI zeptat:
- „Jaký je rozdíl mezi if, elif a else?“
- „Proč mi Python hlásí chybu syntaxe u if?“

> I tady platí: kód od AI si vždy ověř – vyzkoušej všechny větve podmínky (i tu, kterou nečekáš) a zkontroluj, že se chovají správně.
