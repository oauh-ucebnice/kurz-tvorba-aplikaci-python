# Datum a čas

## Modul datetime

Pro práci s datem a časem má Python vestavěný modul `datetime`. Než ho začneš používat, musíš ho naimportovat:

```python
from datetime import datetime
```

## Aktuální datum a čas

```python
ted = datetime.now()
print(ted)  # 2026-07-09 14:32:10.123456
```

`datetime.now()` vrátí objekt, který v sobě má uložený rok, měsíc, den, hodinu, minutu i sekundu.

## Přístup k jednotlivým částem

```python
print(ted.year)   # 2026
print(ted.month)  # 7
print(ted.day)    # 9
print(ted.hour)   # 14
```

## Formátování data pro výpis

Přesný formát textu ovlivníš metodou `strftime()`:

```python
print(ted.strftime("%d.%m.%Y"))  # 09.07.2026
print(ted.strftime("%H:%M:%S"))  # 14:32:10
```

| Značka | Význam | Příklad |
|---|---|---|
| `%d` | den | `09` |
| `%m` | měsíc | `07` |
| `%Y` | rok (čtyřmístně) | `2026` |
| `%H` | hodina | `14` |
| `%M` | minuta | `32` |
| `%S` | sekunda | `10` |

> Malá a velká písmena ve značkách `strftime()` mají různý význam – `%m` je měsíc, `%M` je minuta. Snadno se to splete.

## Výpočty s datem – timedelta

Pomocí `timedelta` můžeš k datu přičítat nebo od něj odečítat dny:

```python
from datetime import timedelta

zitra = ted + timedelta(days=1)
print(zitra.strftime("%d.%m.%Y"))
```

## Časté chyby
- Zapomenutý import (`from datetime import datetime`) – Python `datetime` bez importu nezná.
- Záměna `%m` (měsíc) a `%M` (minuta) ve `strftime()`.
- Očekávání, že `datetime.now()` vrátí text – ve skutečnosti vrací objekt, který teprve pomocí `strftime()` převedeš na text v požadovaném formátu.

## AI Copilot
Zkus se AI zeptat:
- „Jak zjistím dnešní datum v Pythonu?“
- „Jak naformátuji datum jako den.měsíc.rok?“

> I tady platí: kód od AI si vždy ověř – vypiš si výsledek a zkontroluj, že formát data odpovídá tomu, co jsi chtěl/a.
