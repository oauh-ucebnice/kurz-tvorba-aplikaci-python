# `print` a `input`

## Co je `print()`

Příkaz `print()` vypíše text nebo hodnotu na obrazovku (do konzole).

```python
print("Ahoj světe!")
```

### Kdy psát uvozovky?

Text uvedený v uvozovkách se opíše tak, jak je:

```python
print("Karel")
```

Velmi často ale budeš pracovat s proměnnými. Do proměnné můžeš uložit hodnotu a přiřadit jí tak název:

```python
jmeno = "Karel"
print(jmeno)
```

### Víc věcí najednou
Do `print()` můžeš vložit víc hodnot oddělených čárkou. Python je automaticky oddělí mezerou.

```python
jmeno = "Karel"
vek = 15
print("Jmenuji se", jmeno, "a je mi", vek, "let.")
```

### f-string – hezčí zápis
Před uvozovky napiš `f` a hodnoty proměnných vlož přímo do textu ve složených závorkách `{}`.

```python
print(f"Jmenuji se {jmeno} a je mi {vek} let.")
```

## Co je `input()`

Příkaz `input()` počká, až uživatel něco napíše a stiskne Enter. Zadaný text pak vrátí jako řetězec (`str`).

```python
jmeno = input("Jak se jmenuješ? ")
print(f"Ahoj, {jmeno}!")
```

> `input()` vrací vždy text (posloupnost písmen a čísel), i když uživatel napíše číslo. Pokud chceš pracovat s čísly, musíš text převést na číslo:

    ```python
    vek_text = input("Kolik je ti let? ")
    vek = int(vek_text)
    print(f"Za rok ti bude {vek + 1} let.")
    ```

## Časté chyby
- Zapomenuté uvozovky při výpisu textu: ~~`print(Ahoj)`~~
- Chybějící kulaté závorky: ~~`print "Ahoj"`~~
- Chybějící `f` před uvozovkami, pokud chceš použít `{proměnnou}` uvnitř textu: ~~`print("Ahoj {jmeno}")`~~

## AI Copilot
Zkus se AI zeptat:
- „Jak vypíšu proměnnou uprostřed věty?“
- „Proč mi Python hlásí chybu?“
- Vysvětli mi označený kód.

> I tady platí: kód od AI si vždy ověř. Může se stát, že vysvětlení nebude správné. Někdy také AI neodhadne správně důvod chyby nebo smysl tvého kódu.
