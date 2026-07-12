# Tlačítka a textová pole

Prvek uvnitř okna se označuje jako *widget*.

Nejběžnější prvky:
- popisky (*label*)
- tlačítka (*button*)
- textová pole (*text field*/*entry*)
- zatrhávací tlačítko (*checkbox*)
- přepínací tlačítko (*radio button)

Aby se widget v okně zobrazil, musíš ho jednak vytvořit, jednak „umístit“ pomocí `pack()`.

## Ukázka kódu okna

```python
import tkinter as tk

okno = tk.Tk()
okno.title("Moje aplikace")
okno.geometry("300x200")

label = tk.Label(okno, text="Zadej jméno:")
label.pack()

vstup = tk.Entry(okno)
vstup.pack()

button = tk.Button(okno, text="Potvrď")
button.pack()

okno.mainloop()
```

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
- Špatný parametr

## AI Copilot
Zkus se AI zeptat:
- „Jak přidám do okna textové pole?“
- „K čemu slouží `pack()`?“
- „Přidej do okna další dvě textová pole s popisem Věk: a Ročník:“
- „Jak by se dal vylepšit vzhled okna?“

> I tady platí: kód od AI si vždy ověř – spusť aplikaci a vyzkoušej, že widgety fungují a jsou vidět tam, kde mají být.
