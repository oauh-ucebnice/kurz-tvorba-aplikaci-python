# Otevření souboru

## Proč pracovat se soubory

Proměnné a jejich hodnoty existují jen po dobu běhu programu – jakmile skript skončí, zmizí. Pokud chceš data uchovat i po vypnutí programu, musíš je uložit do souboru.

## Otevření souboru pomocí with

Soubor otevřeš funkcí `open()`. V Pythonu se ale vždy otevírá pomocí bloku `with` – ten se postará i o to, aby se soubor po dokončení práce sám zavřel:

```python
with open("vstup.txt") as soubor:
    obsah = soubor.read()
    print(obsah)
```

- `open("vstup.txt")` otevře soubor,
- `with ... as soubor:` uloží otevřený soubor do proměnné `soubor`,
- vše, co se souborem chceš dělat, patří do odsazeného bloku pod `with`,
- jakmile blok skončí, soubor se automaticky zavře.

> Proměnná `soubor` je dostupná jen uvnitř bloku `with`. Mimo něj s ní už nemůžeš pracovat, protože soubor je zavřený.

> Pokud soubor `vstup.txt` neexistuje a otevíráš ho jen ke čtení, Python nahlásí chybu `FileNotFoundError`.

## Cesty k souborům

Datové soubory je vhodné přesunout do samostatné složky. Pak budeš muset uvést cestu k&nbsp;souboru. Jako oddělovač složek použij lomítko `/` (nikoli zpětné lomítko `\` jako ve Windows).

```python
with open("data/vstup.txt") as soubor:
    obsah = soubor.read()
    print(obsah)
```

Ještě lepší je použít knihovnu `os` a použít standardní oddělovač pro aktuální platformu:

```python
import os

with open(os.sep.join(["data", "vstup.txt"])) as soubor:
    obsah = soubor.read()
    print(obsah)
```

> Nezapomeň na hranaté závorky uvnitř kulatých závorek – parametr funkce `join`!


## Kódování souborů

Pokud do vstupního souboru zapíšeš znaky s diakritikou, nejspíš se ti nezobrazí správně. Je to proto, že bys měl nastavit správné kódování souboru.

Vyzkoušej:

```python
import os

with open(os.sep.join(["data", "vstup.txt"]), encoding="utf-8") as soubor:
    obsah = soubor.read()
    print(obsah)
```

Konkrétní správné kódování se může lišit podle toho, jak soubor vytvoříš. Ale vstupní soubor vytváříš ve Visual Studiu Code, mělo by UTF-8 fungovat.

## Pro zvídavé: Proč používat with

Soubor se dá otevřít i bez `with` – pomocí `open()` a následného `close()`:

```python
soubor = open("vstup.txt")
obsah = soubor.read()
soubor.close()
```

Tenhle zápis ale funguje spolehlivě, jen když si na `close()` vždy vzpomeneš – a pokud mezi `open()` a `close()` nastane chyba, `close()` se nemusí spustit vůbec a soubor zůstane otevřený. `with` tohle riziko odstraňuje, proto se v praxi používá skoro vždy a i my ho budeme používat od začátku.

## Časté chyby
- Práce se souborem mimo odsazený blok `with` – soubor už je zavřený.
- Otevření souboru, který neexistuje, v režimu pro čtení – `FileNotFoundError`.
- Špatná cesta k souboru – pokud soubor není ve stejné složce jako skript, musíš uvést i cestu k němu.

## AI Copilot
Zkus se AI zeptat:
- „Jak otevřu soubor v Pythonu?“
- „Co znamená chyba FileNotFoundError?“
- „Proč se mi české znaky zobrazují špatně a jak to opravit?“

> I tady platí: kód od AI si vždy ověř – zkus otevřít existující i neexistující soubor a sleduj, co se stane. Pokud ti AI navrhne kód s `open()` a `close()` bez `with`, uprav si ho.
