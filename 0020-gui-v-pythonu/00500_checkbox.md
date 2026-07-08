# Checkbox

## Co je Checkbox

Checkbox (zaškrtávací políčko) umožňuje uživateli zvolit ano/ne (zapnuto/vypnuto).

## Vytvoření checkboxu

```python
studuje = tk.BooleanVar()

checkbox = tk.Checkbutton(okno, text="Studuji na OA Uherské Hradiště", variable=studuje)
checkbox.pack()
```

- `BooleanVar()` je speciální proměnná tkinteru, která drží hodnotu `True`/`False` a je propojená s widgetem.
- Aktuální stav zjistíš pomocí `.get()`:

```python
if studuje.get():
    print("Zaškrtnuto")
```

> Bez `variable=` bys nezjistil/a, jestli je checkbox zaškrtnutý – widget by jen vypadal, ale nešlo by číst jeho stav.

## Časté chyby
- Čtení `studuje` místo `studuje.get()` – vrátí objekt `BooleanVar`, ne `True`/`False`.
- Zapomenutý parametr `variable=` u `Checkbutton` – stav pak nejde zjistit.

## AI Copilot
Zkus se AI zeptat:
- „Jak zjistím, jestli je checkbox zaškrtnutý?“
- „Co je `BooleanVar` a k čemu slouží?“

> I tady platí: kód od AI si vždy ověř – zaškrtni i odškrtni checkbox a zkontroluj, že se hodnota správně mění.
