# Tlačítka a textová pole

Prvek uvnitř okna se označuje jako *widget*.

Nejběžněji potkáš widgety:
- popisky (*label*)
- tlačítka (*button*)
- textová pole (*text field*/*entry*)
- zatrhávací tlačítko (*checkbox*)
- přepínací tlačítko (*radio button*s)

Aby se widget v okně zobrazil, musíš ho vytvořit a poté „umístit“ do okna pomocí `pack()`.

## Ukázka kódu okna

```python
import tkinter as tk

okno = tk.Tk()
okno.title("Moje aplikace")
okno.geometry("300x200")

# Vložíme jednotlivé widgety:
popisek = tk.Label(okno, text="Napiš své jméno:")
popisek.pack()

vstup = tk.Entry(okno)
vstup.pack()

tlacitko = tk.Button(okno, text="Pozdrav")
tlacitko.pack()
# Konec vkládání widgetůů

okno.mainloop()
```

Jednotlivé widgety nyní podrobněji okomentujeme.

## Label – popisek

Textový popis. Uživatel ho nemůže upravovat. Typicky popis ostatních widgetů.

```python
popisek = tk.Label(okno, text="Napiš své jméno:")
popisek.pack()
```

## Entry – textové pole

Textové pole je určeno pro zápis hodnot. Uživatel může aplikaci zadat vstupní data.

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
tlacitko = tk.Button(okno, text="Pozdrav")
tlacitko.pack()
```

Zatím tlačítko nic nedělá – to, co se stane po kliknutí, se nastavuje pomocí `command` (viz kapitola [Obsluha událostí](00300_udalosti.md)).

> Widget vždy vytváříš s parametrem `okno` jako první argument – Python tak ví, do kterého okna widget patří.

## Výsledný kód

```python
import tkinter as tk

okno = tk.Tk()
okno.title("Moje aplikace")
okno.geometry("300x200")

popisek = tk.Label(okno, text="Napiš své jméno:")
popisek.pack()

vstup = tk.Entry(okno)
vstup.pack()

tlacitko = tk.Button(okno, text="Pozdrav")
tlacitko.pack()

okno.mainloop()
```

> Metodu `pack()` můžeš zavolat rovnou při vytvoření widgetu:  
  `tlacitko = tk.Button(okno, text="Pozdrav").pack()`  
  Kód je pak přehlednější.

## Časté chyby
- Zapomenuté `.pack()` – widget existuje, ale nezobrazí se v okně.
- Záměna `.get()` a `text=` – `.get()` čte hodnotu z `Entry`, `text=` nastavuje popisek u `Label`/`Button`.
- Chybí název parametru. Třeba: `tk.Button(okno, "Pozdrav")` místo správného `tk.Button(okno, text="Pozdrav")`.

## AI Copilot
Zkus se AI zeptat:
- „Jak přidám do okna textové pole?“
- „K čemu slouží `pack()`?“
- „Přidej do okna další dvě textová pole s popisem Věk: a Ročník:“
- „Jak by se dal vylepšit vzhled okna?“

> I tady platí: kód od AI si vždy ověř – spusť aplikaci a vyzkoušej, že widgety fungují a jsou vidět tam, kde mají být.
