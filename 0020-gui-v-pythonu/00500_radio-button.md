# Radio button

## Co je Radio button

Radio button (přepínač) umožňuje uživateli vybrat právě jednu možnost z několika nabízených.

## Vytvoření skupiny přepínačů

Všechny přepínače ve skupině musí sdílet stejnou proměnnou:

```python
jazyk = tk.StringVar()

tk.Radiobutton(okno, text="Python", variable=jazyk, value="Python").pack()
tk.Radiobutton(okno, text="Java", variable=jazyk, value="JavaScript").pack()
tk.Radiobutton(okno, text="Jiný", variable=jazyk, value="jiny").pack()
```

- `StringVar()` drží aktuálně vybranou hodnotu.
- `value=` určuje, co se do proměnné uloží, když uživatel zvolí právě tento přepínač.
- Vybranou hodnotu zjistíš stejně jako u checkboxu: `jazyk.get()`.

> Pokud přepínače nesdílí stejnou proměnnou (`variable=`), budou fungovat jako samostatné checkboxy a půjde zaškrtnout víc najednou.

## Úkol: Oblíbený programovací jazyk

1. Vytvoř okno s výběrem oblíbeného programovacího jazyka.
2. Přidej tlačítko _Potvrď_.
3. Přidej popisek (label) – na začátku s textem _Zatím nevybráno_.
3. Když uživatel zmáčkne tlačítko, zobraz na popisku text _Vybral jsi jazyk: ..._ (místo tří teček zobraz vybraný jazyk).

<!-- TODO: Show the GUI output -->

## Časté chyby
- Různé proměnné u přepínačů ve stejné skupině – jde pak zvolit víc možností najednou.
- Chybějící `value=` – Python neví, jakou hodnotu do proměnné při výběru uložit.

## AI Copilot
Zkus se AI zeptat:
- „Jak vytvořím skupinu přepínačů, ze kterých jde vybrat jen jeden?“
- „Jaký je rozdíl mezi `Checkbutton` a `Radiobutton`?“

> I tady platí: kód od AI si vždy ověř – vyzkoušej, že jde vybrat vždy jen jedna možnost.
