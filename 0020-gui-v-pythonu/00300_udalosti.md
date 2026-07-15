# Obsluha událostí

## Co je událost

Událost je akce uživatele – třeba kliknutí na tlačítko. Aby program na událost zareagoval, musíš mu říct, jakou funkci má při ní spustit.

## Funkce jako reakce na klik

Nejdřív napiš funkci, která se má spustit:

```python
def pozdrav():
    print("Ahoj!")
```

Pak ji propoj s tlačítkem pomocí parametru `command`:

```python
tlacitko = tk.Button(okno, text="Pozdrav", command=pozdrav)
tlacitko.pack()
```

> Za `command=` patří jen název funkce, bez závorek! Když napíšeš závorky `command=pozdrav()`, funkce se spustí jednou při startu programu a tlačítko na další kliknutí nereaguje.

## Funkce piš na začátek kódu

Je zvykem funkce psát (definovat) na začátek skriptu a pak teprve psát kód okna.

Pokud zadáš do `command=` funkci, která ještě nebyla definována, nebude fungovat – Python ji ještě nezná.

## Práce s hodnotami z widgetů

Funkce může číst text z `Entry` a použít ho:

```python
def zobraz():
    text = vstup.get()
    print(f"Napsal jsi: {text}")

vstup = tk.Entry(okno).pack()
tlacitko = tk.Button(okno, text="Zobraz", command=zobraz).pack()
```

## Změna hodnot widgetů

Vlastnosti widgetů změníš metodou `.config()`:

```python

def prepis():
    vysledek.config(text="Nový text")

vysledek = tk.Label(okno, text="Původní text").pack()
tlacitko = tk.Button(okno, text="Přepiš text", command=prepis)
tlacitko.pack()
```

- Popisek `vysledek` vytvoříš prázdný (`text=""`) a text do něj doplníš, až uživatel klikne na tlačítko.
- `.config(text=...)` přepíše text libovolného widgetu i po jeho vytvoření.

> `.config()` funguje na většině widgetů – můžeš tak měnit nejen text, ale třeba i barvu (`bg`, `fg`) nebo velikost písma (`font`).


## Výsledný kód

```python
import tkinter as tk

def opis():
    zadany_text = vstup.get()
    vystup.config(text="text")
    print(f"Napsal jsi: {zadany_text}")

okno = tk.Tk()
okno.title("Opisuj")
okno.geometry("300x200")

popisek = tk.Label(okno, text="Napiš nový text:").pack()
vstup = tk.Entry(okno).pack()
vystup = tk.Label(okno, text="Zatím nic...").pack()

tlacitko = tk.Button(okno, text="Opiš", command=opis).pack()

okno.mainloop()
```

## Časté chyby
- `command=pozdrav()` místo `command=pozdrav` – funkce se zavolá okamžitě, ne po kliknutí.
- Přiřazuješ v `command=` funkci, kterou v kódu definuješ až poté. Přesuň funkce na začátek skriptu!
- Vytvoření nového `Label(...)` místo použití `.config()` – vznikne tak druhý popisek navíc místo úpravy toho původního.
- Čtení textu z `Entry` (`vstup.get()`) mimo funkci, ještě než uživatel něco napsal – vrátí prázdný řetězec.

- Při nastavování prvků jsi zapomněl na `.config()`. Například: `vysledek = "Nový"` místo `vysledek.config(text="Nový")`.

## AI Copilot
Zkus se AI zeptat:
- „Jak zavolám funkci po kliknutí na tlačítko?“
- „Proč se mi funkce spustí hned, i když jsem ještě neklikl?“
- „Přiřaď tlačítku funkci, které přečte text z textového pole a zobrazí ho ve vyskakovacím okně (message box).“
- „Proč se při kliknutí na tlačítko neaktualizuje text popisku?“
- „Vysvětli mi, jak tento kód funguje.“

> I tady platí: kód od AI si vždy ověř – klikni na tlačítko a zkontroluj, že se stane přesně to, co má.
