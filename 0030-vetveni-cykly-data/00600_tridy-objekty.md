# Třídy a objekty

## Co je třída a objekt

Třída je „šablona“, podle které vytváříš objekty se stejnou strukturou. Objekt je konkrétní instance třídy – obsahuje vlastní hodnoty podle této šablony.

## Definice třídy

```python
class Zakaznik:
    def __init__(self, jmeno, pocet_zakazek):
        self.jmeno = jmeno
        self.pocet_zakazek = pocet_zakazek
```

- `class Zakaznik:` vytvoří novou třídu,
- `__init__` je speciální metoda, která se spustí při vytvoření objektu a nastaví jeho počáteční hodnoty,
- `self` odkazuje na konkrétní vytvářený objekt – přes něj přistupuješ k jeho vlastnostem.

## Vytvoření objektu

```python
zakaznik1 = Zakaznik("Karel", 3)

print(zakaznik1.jmeno)          # Karel
print(zakaznik1.pocet_zakazek)  # 3
```

> Objekt `zakaznik1` je konkrétní instance třídy `Zakaznik`. Ze stejné třídy můžeš vytvořit libovolné množství objektů, každý s vlastními hodnotami.

## Objekty v poli

Objekty můžeš stejně jako čísla nebo text ukládat do pole:

```python
zakaznici = [
    Zakaznik("Karel", 3),
    Zakaznik("Petra", 1),
]

for zakaznik in zakaznici:
    print(zakaznik.jmeno, zakaznik.pocet_zakazek)
```

## Třída vs. slovník

Slovník i třída umí uložit víc hodnot pohromadě. Třída navíc umožňuje přidat vlastní metody (funkce, které patří k objektu) a hodí se lépe, pokud se stejnou strukturou dat pracuješ na víc místech v programu.

## Časté chyby
- Zapomenutý parametr `self` v definici metody.
- Volání `Zakaznik.jmeno` místo `zakaznik1.jmeno` – k vlastnosti přistupuješ přes konkrétní objekt, ne přes třídu.
- Chybějící `__init__` – bez něj objekt při vytvoření nezíská žádné počáteční hodnoty.

## AI Copilot
Zkus se AI zeptat:
- „K čemu je dobré použít třídu místo slovníku?“
- „Co dělá metoda __init__?“

> I tady platí: kód od AI si vždy ověř – vytvoř si víc objektů stejné třídy a zkontroluj, že má každý svoje vlastní hodnoty.
