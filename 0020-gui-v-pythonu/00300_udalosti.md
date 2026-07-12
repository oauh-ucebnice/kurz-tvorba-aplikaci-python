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

> Za `command=` patří jen název funkce, bez závorek! `command=pozdrav()` funkci spustí hned při startu programu, ne až po kliknutí.

## Práce s hodnotami z widgetů

Funkce může číst text z `Entry` a použít ho:

```python
def zobraz():
    text = vstup.get()
    print(f"Napsal jsi: {text}")

tlacitko = tk.Button(okno, text="Zobraz", command=zobraz)
```

## Výsledný kód

```python
import tkinter as tk

def zobraz():
    text = vstup.get()
    print(f"Napsal jsi: {text}")

okno = tk.Tk()
okno.title("Moje aplikace")
okno.geometry("300x200")

popisek = tk.Label(okno, text="Napiš své jméno:")
popisek.pack()

vstup = tk.Entry(okno)
vstup.pack()

tlacitko = tk.Button(okno, text="Zobraz", command=zobraz)
tlacitko.pack()

okno.mainloop()
```

## Časté chyby
- `command=pozdrav()` místo `command=pozdrav` – funkce se zavolá okamžitě, ne po kliknutí.
- Funkce použitá v `command=` dřív, než je v kódu definovaná – Python ji ještě nezná.

## AI Copilot
Zkus se AI zeptat:
- „Jak zavolám funkci po kliknutí na tlačítko?“
- „Proč se mi funkce spustí hned, i když jsem ještě neklikl?“

> I tady platí: kód od AI si vždy ověř – klikni na tlačítko a zkontroluj, že se stane přesně to, co má.
