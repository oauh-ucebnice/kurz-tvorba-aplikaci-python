# Zápis kódu v Pythonu

Python byl navržený v 80. letech 20. století jako jazyk pro výuku programování. Dnes je to jeden z&nbsp;nejběžněji používaných jazyků a využívá se pro mnoho různých typů úloh.

## Odsazování

Python na rozdíl od většiny jiných jazyků nepoužívá pro označení bloku kódu závorky či jiné oddělovače. Vnořený blok kódu se označí odsazováním.

```python
print('Test začíná:')
if 3 > 5:
    print('Matematika nefunguje')
print('Konec testu')
```

## Není potřeba psát středníky

Některé programovací jazyky vyžadují na konci příkazu středník (`;`).

V&nbsp;Pythonu je středník pouze oddělovač příkazů. Pokud tedy máš na řádku jeden příkaz, středník psát nemusíš a ani to není zvykem. Můžeš ale na jeden řádek napsat více příkazů oddělených středníkem.

```python
print('Výpis čísla:')
a = 5; print(f'Číslo a má hodnotu: {a}.')
```

## Spouštění skriptů

Skript (program) v Pythonu se spouští pomocí interpretu. Pro spuštění kódu tedy musíte mít na počítači nainstalovaný Python.

Překlad zdrojového kódu probíhá při každém spuštění znovu.

## Skriptovací jazyk

Python patří do skupiny _skriptovacích jazyků_. Skriptovací jazyky dávají přednost rychlému zápisu kódu. Cenou za rychlost psaní je horší automatická kontrola a nutnost psát kód čitelně.

Typické vlastnosti skriptovacích jazyků:
- proměnné není třeba deklarovat
- datový typ proměnných se může měnit během života proměnné
- kód je stručný s minimem přidaných znaků
- program se typicky spouští pomocí interpretu a překládá za běhu
- knihovny jazyka umožňují spouštět příkazy
- výkonné knihovny pro zpracování textu, práci se soubory a kolekcemi

Možná znáš také další skriptovací jazyky jako PHP, JavaScript či Perl a další.