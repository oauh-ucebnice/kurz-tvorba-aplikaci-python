# Tlačítka a textová pole

## Co je widget

Widget je prvek uvnitř okna – třeba popisek, textové pole nebo tlačítko. Aby se widget v okně zobrazil, musíš ho jednak vytvořit, jednak „umístit“ pomocí `pack()`.

## Label – popisek

```python
popisek = tk.Label(okno, text="Napiš své jméno:")
popisek.pack()
```

## Entry – textové pole

```python
vstup = tk.Entry(okno)
vstup.pack()
```

Text, který uživatel napíše, získáš metodou `.get()`:

```python
text = vstup.get()
```

## Button – tlačítko

```python
tlacitko = tk.Button(okno, text="Zobraz")
tlacitko.pack()
```

Zatím tlačítko nic nedělá – to, co se stane po kliknutí, se nastavuje pomocí `command` (viz kapitola [Obsluha událostí](00300_udalosti.md)).

> Widget vždy vytváříš s parametrem `okno` jako první argument – Python tak ví, do kterého okna widget patří.

## Časté chyby
- Zapomenuté `.pack()` – widget existuje, ale nezobrazí se v okně.
- Záměna `.get()` a `text=` – `.get()` čte hodnotu z `Entry`, `text=` nastavuje popisek u `Label`/`Button`.

## AI Copilot
Zkus se AI zeptat:
- „Jak přidám do okna textové pole?“
- „K čemu slouží `pack()`?“

> I tady platí: kód od AI si vždy ověř – spusť aplikaci a vyzkoušej, že widgety fungují a jsou vidět tam, kde mají být.
