# Proměnné

## Co je proměnná

Proměnná je pojmenované místo v paměti počítače, kam si Python uloží hodnotu. Vytvoříš ji přiřazením pomocí `=`:

```python
jmeno = "Karel"
vek = 15
```

> Nalevo je název proměnné, napravo hodnota, kterou do ní ukládáš. Python si sám odvodí, jaký typ dat proměnná obsahuje.

### Pravidla pro název proměnné
- smí obsahovat písmena, čísla a podtržítko `_`,
- nesmí začínat číslem,
- rozlišují se malá a velká písmena (`vek` a `Vek` jsou dvě různé proměnné).

### Jak vybrat názvy proměnných
- piš názvy tak, aby bylo jasné, co proměnná obsahuje (`pocet_bodu` je lepší než `cislo1`),
- nepoužívej jednopísmenné názvy (`a`, `x`, `m`),
- v Pythonu se obvykle používá styl `snake_case`, tedy slova oddělená podtržítkem (`jmeno_uzivatele`, `pocet_bodu`),
- názvy piš všemi písmeny malými,
- velká písmena se používají hlavně pro konstanty, například `MAX_POCET`.

Příklady:

```python
jmeno_uzivatele = "Karel"
pocet_bodu = 15
MAX_POCET_BODU = 100
```

> Dodržování pravidel (konvencí) je důležité pro spolupráci a čitelnost kódu.

## Práce s proměnnými

Proměnné můžeš používat ve výpočtech i je přepisovat:

```python
vek = 15
vek = vek + 1
print(vek)  # 16
```

## Časté chyby
- Použití proměnné dřív, než jí přiřadíš hodnotu.
- Překlep v názvu proměnné (`vek` vs. `věk` vs. `Vek`) – Python hlásí, že proměnná neexistuje.

## AI Copilot
Zkus se AI zeptat:
- „Proč mi Python hlásí, že proměnná není definovaná?“
- Vysvětli mi označený kód,
- Navrhni dobrý název pro proměnnou, do které budu ukládat...

> I tady platí: kód od AI si vždy ověř. Zkontroluj, jestli navržené názvy proměnných dávají smysl a odpovídají konvencím.
