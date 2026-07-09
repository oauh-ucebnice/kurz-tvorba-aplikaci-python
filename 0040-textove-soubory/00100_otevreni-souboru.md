# Otevření souboru

## Proč pracovat se soubory

Proměnné a jejich hodnoty existují jen po dobu běhu programu – jakmile skript skončí, zmizí. Pokud chceš data uchovat i po vypnutí programu, musíš je uložit do souboru.

## Otevření souboru pomocí with

Soubor otevřeš funkcí `open()`. V Pythonu se ale vždy otevírá pomocí bloku `with` – ten se postará i o to, aby se soubor po dokončení práce sám zavřel:

```python
with open("data.txt") as soubor:
    obsah = soubor.read()
    print(obsah)
```

- `open("data.txt")` otevře soubor,
- `with ... as soubor:` uloží otevřený soubor do proměnné `soubor`,
- vše, co se souborem chceš dělat, patří do odsazeného bloku pod `with`,
- jakmile blok skončí, soubor se automaticky zavře.

> Proměnná `soubor` je dostupná jen uvnitř bloku `with`. Mimo něj s ní už nemůžeš pracovat, protože soubor je zavřený.

> Pokud soubor `data.txt` neexistuje a otevíráš ho jen ke čtení, Python nahlásí chybu `FileNotFoundError`.

## Proč zrovna with

Soubor se dá otevřít i bez `with` – pomocí `open()` a následného `close()`:

```python
soubor = open("data.txt")
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
- „Jak otevřu soubor v Pythonu pomocí with?“
- „Co znamená chyba FileNotFoundError?“

> I tady platí: kód od AI si vždy ověř – zkus otevřít existující i neexistující soubor a sleduj, co se stane. Pokud ti AI navrhne kód s `open()` a `close()` bez `with`, uprav si ho.
