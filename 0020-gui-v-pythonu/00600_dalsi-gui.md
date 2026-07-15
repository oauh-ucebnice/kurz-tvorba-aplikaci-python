# Další užitečné informace při tvorbě GUI

## Použití schránky (clipboard)

Schránka slouží k přenosu textu mezi aplikacemi pomocí operací kopírovat/vložit. V tkinter se dá pracovat se schránkou pomocí metod okna.

### Základní operace

```python
import tkinter as tk

root = tk.Tk()
root.title("Práce se schránkou")

# Zkopíruj text do schránky
def copy_to_clipboard():
    text = "Tento text se zkopíruje!"
    root.clipboard_clear()
    root.clipboard_append(text)
    root.update()  # Potřeba pro správné fungování
    print("Text zkopírován do schránky!")

# Načti text ze schránky
def paste_from_clipboard():
    try:
        text = root.clipboard_get()
        print(f"Text ze schránky: {text}")
    except tk.TclError:
        print("Schránka je prázdná!")

# Tlačítka
tk.Button(root, text="Kopírovat", command=copy_to_clipboard).pack(pady=5)
tk.Button(root, text="Vložit", command=paste_from_clipboard).pack(pady=5)

root.mainloop()
```

### Praktický příklad s entry polem

```python
import tkinter as tk

root = tk.Tk()

entry = tk.Entry(root, width=40)
entry.pack(pady=10)

def copy():
    root.clipboard_clear()
    root.clipboard_append(entry.get())
    root.update()

def paste():
    text = root.clipboard_get()
    entry.delete(0, tk.END)
    entry.insert(0, text)

tk.Button(root, text="Kopírovat", command=copy).pack()
tk.Button(root, text="Vložit", command=paste).pack()

root.mainloop()
```

### Důležité poznámky

- Vždy zavolej `root.clipboard_clear()` před vložením nového textu
- Po vložení textu je dobré zavolat `root.update()` pro správné fungování
- `root.clipboard_get()` vrátí obsah schránky nebo vyhodí chybu, pokud je prázdná
- Toto funguje pouze s textem, ne s obrázky

## Vyskakovací okna

Vyskakovací okna (dialogy) slouží k zobrazení informací, varování nebo kladení otázek uživateli. V tkinter se používá modul `tkinter.messagebox`.

### Základní typy dialogů

```python
from tkinter import messagebox
import tkinter as tk

# Vytvoř hlavní okno
root = tk.Tk()
root.title("Příklad dialogů")
root.geometry("300x200")

# Informační okno
def show_info():
    messagebox.showinfo("Informace", "Toto je informační okno!")

# Okno s varováním
def show_warning():
    messagebox.showwarning("Varování", "Pozor na tuto akci!")

# Okno s chybou
def show_error():
    messagebox.showerror("Chyba", "Došlo k chybě!")

# Otázka (vrací True/False)
def ask_question():
    result = messagebox.askyesno("Otázka", "Chceš pokračovat?")
    if result:
        messagebox.showinfo("Výsledek", "Odpověděl jsi ano!")
    else:
        messagebox.showinfo("Výsledek", "Odpověděl jsi ne!")

# Tlačítka pro testování
tk.Button(root, text="Informace", command=show_info).pack(pady=5)
tk.Button(root, text="Varování", command=show_warning).pack(pady=5)
tk.Button(root, text="Chyba", command=show_error).pack(pady=5)
tk.Button(root, text="Otázka", command=ask_question).pack(pady=5)

root.mainloop()
```

### Dostupné funkce

| Funkce | Účel | Vrací |
|--------|------|-------|
| `showinfo(title, message)` | Informační okno | `None` |
| `showwarning(title, message)` | Okno s varováním | `None` |
| `showerror(title, message)` | Okno s chybou | `None` |
| `askyesno(title, message)` | Otázka (Ano/Ne) | `True` / `False` |
| `askyesnocancel(title, message)` | Otázka (Ano/Ne/Storno) | `True` / `False` / `None` |
| `askokcancel(title, message)` | OK/Storno dialog | `True` / `False` |
| `askretrycancel(title, message)` | Opakovat/Storno | `True` / `False` |

### Praktický příklad se zpracováním odpovědi

```python
result = messagebox.askyesnocancel("Uložit?", "Chceš uložit změny?")

if result is True:
    print("Ukládám...")
elif result is False:
    print("Zavrhuji změny...")
else:
    print("Zrušit operaci")
```

## Časté chyby

## AI Copilot
Zkus prompty:


> I tady platí: kód od AI si vždy ověř – vyzkoušej, že jde vybrat vždy jen jedna možnost.
