# Zobrazení výsledku uživatele

## Jak změnit text popisku

Text u `Label` po vytvoření změníš metodou `.config()`:

```python
vysledek = tk.Label(okno, text="")
vysledek.pack()

def zobraz():
    text = vstup.get()
    vysledek.config(text=f"Napsal jsi: {text}")

tlacitko = tk.Button(okno, text="Zobraz", command=zobraz)
tlacitko.pack()
```

- Popisek `vysledek` vytvoříš prázdný (`text=""`) a text do něj doplníš, až uživatel klikne na tlačítko.
- `.config(text=...)` přepíše text libovolného widgetu i po jeho vytvoření.

> `.config()` funguje na většině widgetů – můžeš tak měnit nejen text, ale třeba i barvu (`bg`, `fg`) nebo velikost písma (`font`).

## Celý příklad pohromadě

```python
import tkinter as tk

def zobraz():
    text = vstup.get()
    vysledek.config(text=f"Napsal jsi: {text}")

okno = tk.Tk()
okno.title("Zobrazovač textu")

vstup = tk.Entry(okno)
vstup.pack()

tlacitko = tk.Button(okno, text="Zobraz", command=zobraz)
tlacitko.pack()

vysledek = tk.Label(okno, text="")
vysledek.pack()

okno.mainloop()
```

## Časté chyby
- Vytvoření nového `Label(...)` místo použití `.config()` – vznikne tak druhý popisek navíc místo úpravy toho původního.
- Čtení textu z `Entry` (`vstup.get()`) mimo funkci, ještě než uživatel něco napsal – vrátí prázdný řetězec.

## AI Copilot
Zkus se AI zeptat:
- „Jak změním text popisku po kliknutí na tlačítko?“
- „Jak najdu chybu, když se text v okně neaktualizuje?“

> I tady platí: kód od AI si vždy ověř – vyzkoušej aplikaci s různým vstupem a zkontroluj, že se popisek správně mění.
