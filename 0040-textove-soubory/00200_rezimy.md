# Režimy otevření souboru

## Co je režim

Při otevírání souboru určuješ, co s ním chceš dělat – jestli ho jen číst, nebo do něj i zapisovat. Slouží k tomu druhý argument funkce `open()`.

```python
with open("data.txt", "r") as soubor:
    obsah = soubor.read()
```

## Základní režimy

| Režim | Význam | Co se stane, když soubor neexistuje |
|---|---|---|
| `r` | čtení (*read*) | chyba `FileNotFoundError` |
| `w` | zápis (*write*), přepíše celý obsah | soubor se vytvoří |
| `a` | přidání na konec (*append*) | soubor se vytvoří |

> Výchozí režim (pokud ho neuvedeš) je `r`.

## Pozor na režim w

Režim `w` smaže celý dosavadní obsah souboru, i když do něj nakonec nic nezapíšeš:

```python
with open("poznamky.txt", "w") as soubor:  # obsah je smazán hned teď
    ...
```

> Pokud chceš k souboru jen přidávat data a zachovat to, co v něm už je, použij `a`, ne `w`.

## Časté chyby
- Použití `w` místo `a` – smažeš data, která jsi chtěl/a zachovat.
- Pokus o `write()` do souboru otevřeného v režimu `r` – Python zápis odmítne.
- Pokus o `read()` ze souboru otevřeného v režimu `w` – v tu chvíli je soubor prázdný.

## AI Copilot
Zkus se AI zeptat:
- „Jaký je rozdíl mezi režimy w a a?“
- „Kdy mám použít režim a a kdy w?“

> I tady platí: kód od AI si vždy ověř – rozdíl mezi `w` a `a` má reálné důsledky, vyzkoušej si ho na testovacím souboru.
