# Prohlížeč zákazníků

> Vytvoř aplikaci, která načte údaje o zákaznících ze souboru a umožní mezi nimi listovat.

## Level 1: Připrav data a načti je

Vytvoř soubor `zakaznici.json` s údaji o několika zákaznících. Každý záznam bude mít položky `jmeno` a `datum_nakupu`, například:

```json
[
    {"jmeno": "Karel Novák", "datum_nakupu": "2026-03-12"},
    {"jmeno": "Petra Svobodová", "datum_nakupu": "2026-05-02"}
]
```

Vytvoř skript `zakaznici.py`, který soubor načte a vypíše všechny záznamy do konzole.

## Level 2: Zobraz záznamy v okně

Uprav skript tak, aby:
- otevřel okno s popiskem, který ukáže jméno a datum nákupu prvního zákazníka,
- přidal tlačítka „Předchozí“ a „Další“ pro listování mezi záznamy,
- po kliknutí na tlačítko se popisek aktualizoval na sousední záznam.

## Level 3: Ošetři okraje

- Zajisti, aby kliknutí na „Další“ u posledního záznamu nebo na „Předchozí“ u prvního záznamu nezpůsobilo chybu.
- Využij AI Copilota k vylepšení vzhledu okna.
