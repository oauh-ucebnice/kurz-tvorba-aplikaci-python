# Funkce

## Co je funkce?

Složitější kód je lepší rozdělit na menší bloky kvůli přehlednosti. Jednotlivé bloky kódu se označují jako *funkce*. 

## Vytvoření a spuštění funkce

Funkci vytvoříš klíčovým slovem `def`:

```python
def pozdrav():
    print("Ahoj!")
```

Aby se kód uvnitř funkce spustil, musíš funkci zavolat:

```python
pozdrav()
```

> Řádky uvnitř funkce musí být odsazené (obvykle o 4 mezery). Python podle odsazení pozná, co do funkce patří a co už ne.

## Parametry – vstup do funkce

Funkci můžeš předat hodnoty, se kterými pak pracuje:

```python
def pozdrav(jmeno):
    print(f"Ahoj, {jmeno}!")

pozdrav("Karel")
```

Funkci můžeš volat opakovaně a nemusíš kód psát znovu. Můžeš třeba převádět teplotu ze stuňů Celsia na stupně Fahrenheita:

```python
def celsius_na_fahrenheit(teplota_celsius):
    return teplota_celsius * 9 / 5 + 32


print(celsius_na_fahrenheit(0))
print(celsius_na_fahrenheit(20))
print(celsius_na_fahrenheit(100))
```


## Návratová hodnota – výstup z funkce

Pomocí `return` funkce vrátí výsledek, který můžeš uložit do proměnné:

```python
def secti(a, b):
    return a + b

vysledek = secti(3, 5)
print(vysledek)  # 8
```

> `print()` uvnitř funkce jen vypíše text na obrazovku, `return` hodnotu vrátí ven, abys s ní mohl/a dál pracovat.

## Proč funkce používat
- kód nemusíš psát víckrát – stačí funkci jednou definovat a pak jen volat,
- program se lépe čte – pojmenovaná funkce řekne, co dělá, aniž bys musel/a číst celý kód,
- snáz najdeš a opravíš chybu – stačí zkontrolovat jednu funkci, ne celý skript.

## Časté chyby
- Definice funkce bez jejího zavolání – kód uvnitř funkce se nikdy nespustí.
- Záměna `print()` a `return` – `return` hodnotu jen vrátí, nezobrazí ji. Pokud chceš výsledek vidět, musíš ho vypsat: `print(secti(3, 5))`.
- Použití proměnné definované uvnitř funkce mimo funkci – taková proměnná mimo funkci neexistuje.

## AI Copilot
Zkus se AI zeptat:
- „K čemu je dobré používat funkce?“
- „Jaký je rozdíl mezi `print()` a `return`?“
- Vysvětli mi označený kód.

> I tady platí: kód od AI si vždy ověř. Zkontroluj, jestli funkce dělá přesně to, co má, a jestli ji voláš na správném místě.
