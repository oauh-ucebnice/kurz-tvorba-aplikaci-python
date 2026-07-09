# Slovník (dictionary)

## Co je slovník

Slovník (`dict`) ukládá dvojice klíč–hodnota. Na rozdíl od pole nepřistupuješ k prvkům podle čísla pozice, ale podle pojmenovaného klíče.

```python
zakaznik = {
    "jmeno": "Karel",
    "vek": 15
}
```

## Přístup k hodnotám

```python
print(zakaznik["jmeno"])  # Karel
print(zakaznik["vek"])    # 15
```

> Pokud klíč ve slovníku neexistuje, Python nahlásí chybu `KeyError`.

## Přidání a úprava hodnoty

```python
zakaznik["email"] = "karel@example.com"  # přidá nový klíč
zakaznik["vek"] = 16                     # upraví existující hodnotu
```

## Průchod slovníkem

```python
for klic in zakaznik:
    print(klic, ":", zakaznik[klic])
```

## Časté chyby
- Přístup k neexistujícímu klíči – `KeyError`.
- Záměna hranatých závorek `[]` (přístup k hodnotě) a kulatých `()` (volání funkce).
- Použití stejného klíče dvakrát – druhé přiřazení přepíše první.

## AI Copilot
Zkus se AI zeptat:
- „Jaký je rozdíl mezi polem a slovníkem?“
- „Proč mi Python hlásí KeyError?“

> I tady platí: kód od AI si vždy ověř – vypiš si celý slovník a zkontroluj, že obsahuje přesně ty klíče a hodnoty, které očekáváš.
