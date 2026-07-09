# Formáty souborů – JSON, CSV, XML

## Proč strukturované formáty

Obyčejný text se hodí na jednoduchá data, ale pro složitější záznamy (víc položek, vnořené údaje) se používají standardizované formáty, které umí přečíst i jiné programy a jazyky.

Tato lekce je jen velmi stručné představení nejznámnějších formátů. Ber ji jako tip, co si můžeš vyzkoušet dál.

## JSON

JSON (*JavaScript Object Notation*) ukládá data podobně jako Python slovník (`dict`):

```json
{
    "jmeno": "Karel",
    "vek": 15
}
```

Python má pro práci s JSON vestavěný modul `json`:

```python
import json

with open("data.json", "r") as soubor:
    data = json.load(soubor)

print(data["jmeno"])
```

## CSV

CSV (*Comma-Separated Values*) ukládá data v řádcích, kde jsou hodnoty oddělené čárkou – hodí se pro tabulková data:

```
jmeno,vek
Karel,15
Petra,16
```

Python má vestavěný modul `csv`:

```python
import csv

with open("data.csv", "r") as soubor:
    reader = csv.reader(soubor)
    for radek in reader:
        print(radek)
```

## XML

XML (*eXtensible Markup Language*) zapisuje data pomocí značek (tagů), podobně jako HTML:

```xml
<osoba>
    <jmeno>Karel</jmeno>
    <vek>15</vek>
</osoba>
```

Pro práci s XML slouží modul `xml.etree.ElementTree`. Práce s ním je složitější než u JSON nebo CSV a ve školních projektech se používá méně často.

> Který formát zvolit? JSON je dobrá volba pro strukturovaná data (i vnořená), CSV pro jednoduché tabulky, XML se dnes používá hlavně tam, kde ho vyžaduje starší systém.

## Časté chyby
- Otevření JSON/CSV souboru bez příslušného modulu (`json`, `csv`) a snaha parsovat text ručně.
- Špatně formátovaný JSON soubor (např. chybějící uvozovky u klíčů) – `json.load()` skončí chybou.
- Otevření souboru bez zadání kódování, pokud obsahuje diakritiku (doporučeno: `open("data.csv", "r", encoding="utf-8")`).

## AI Copilot
Zkus se AI zeptat:
- „Jak načtu data z JSON souboru v Pythonu?“
- „Jaký je rozdíl mezi JSON, CSV a XML?“

> I tady platí: kód od AI si vždy ověř – zkontroluj, že načtená data odpovídají tomu, co je v souboru.
