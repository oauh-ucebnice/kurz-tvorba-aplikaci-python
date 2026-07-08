# Datové typy

## Co je datový typ?

Datový typ určuje, jaký druh hodnoty proměnná obsahuje – jestli je to text, celé číslo, desetinné číslo, nebo třeba hodnota ano/ne. 

Podle datového typu Python pozná, co s hodnotou smí dělat.

```python
vek = 15         # číslo
jmeno = "Karel"  # text
```

Tady `vek` obsahuje celé číslo, `jmeno` obsahuje text. Typ hodnoty zjistíš funkcí `type()`:

```python
print(type(vek))    # <class 'int'>
print(type(jmeno))   # <class 'str'>
```

## Proč je datový typ důležitý?

V Pythonu při vytváření proměnné typ nikde nepíšeš – Python si ho sám odvodí z hodnoty, kterou proměnné přiřadíš. Přesto typ ovlivňuje, jak se proměnná chová:

```python
print(5 + 3)        # 8   (sčítání čísel)
print("5" + "3")     # 53  (spojení textu)
print("5" + 3)       # chyba! nejde spojit text a číslo
```

Stejný operátor `+` se chová jinak podle toho, jaký typ hodnot spojuje. Proto je důležité vědět, jaký typ proměnná má, i když to nikam explicitně nezapisuješ – pomůže ti to předvídat, jak se kód zachová, a rychleji najít chybu, když něco nefunguje.

> Tomuto přístupu se říká **dynamické typování** – typ se určuje až za běhu programu, podle aktuální hodnoty. Proměnná navíc může typ během programu i změnit, pokud jí přiřadíš hodnotu jiného typu.

## Základní datové typy

| Typ | Popis | Příklad |
|---|---|---|
| `str` | text (řetězec) | `"Karel"` |
| `int` | celé číslo | `15` |
| `float` | desetinné číslo | `15.5` |
| `bool` | pravda/nepravda | `True`, `False` |

> Pro desetinná čísla se používá desetinná tečka. Tedy `15.5`, ne ~~`15,5`~~.

## Převody mezi typy

Hodnoty můžeš mezi typy převádět:

```python
vek_text = "15"
vek_cislo = int(vek_text)        # text -> celé číslo
vek_desetinne = float(vek_text)  # text -> desetinné číslo
vek_zpet = str(vek_cislo)        # číslo -> text
```

> `input()` vždy vrací text (`str`). Pokud chceš s výsledkem počítat, musíš ho převést na `int` nebo `float`.

## Časté chyby
- Sčítání textu a čísla bez převodu: ~~`"Je mi " + 15`~~ způsobí chybu, správně je `"Je mi " + str(15)` nebo `f"Je mi {15}"`.
- Očekávání, že `input()` vrátí číslo – vždy vrací text, i když uživatel napíše číslo.
- Použití desetinné čárky místo desetinné tečky při zadávání desetinných čísel: správně je `28.452` a ne ~~`28,452`~~.

## AI Copilot
Zkus se AI zeptat:
- „Jaký datový typ má tahle proměnná?“
- „Proč mi Python hlásí chybu, když spojuji text a číslo?“

> I tady platí: kód od AI si vždy ověř. Zkontroluj, jestli navržený datový typ opravdu odpovídá tomu, co proměnná má obsahovat.
