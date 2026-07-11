# Co je AI agent

## Co už znáš – Copilot

Copilot v editoru navrhuje řádky nebo celé bloky kódu přímo tam, kde píšeš – ty návrh potvrdíš klávesou Tab, nebo se ho na něco zeptáš v chatu. Copilot vždy čeká na tebe u každého kroku – ty rozhoduješ, co se stane dál.

## Co je nového – AI agent

AI agent (například Claude Code nebo Codex) běží v terminálu (příkazové řádce) a na rozdíl od Copilota umí pracovat samostatně – na základě jednoho zadání v přirozeném jazyce:

- přečte soubory v projektu,
- napíše nebo upraví kód ve víc souborech najednou,
- spustí příkaz (třeba testy) a podle výsledku pokračuje, nebo se sám opraví.

Rozdíl je hlavně v samostatnosti: Copilotovi zadáváš jeden krok, agentovi klidně celý úkol – a on si kroky rozplánuje sám.

## Kdy použít co

| Situace | Lepší volba |
|---|---|
| Chci poradit s jedním řádkem nebo funkcí, zatímco píšu kód | Copilot v editoru |
| Chci se rychle na něco zeptat, aniž bych opouštěl/a editor | Copilot Chat |
| Chci zadat větší úkol („přidej do aplikace nové okno s formulářem“) a nechat AI, ať sama upraví víc souborů | AI agent (CLI) |
| Chci, aby AI sama spustila program a opravila chybu, kterou najde | AI agent (CLI) |

> Agent není „chytřejší“ Copilot – je to jiný způsob práce. Ty pořád rozhoduješ, co má agent dělat, a na konci vždy zkontroluješ, co udělal.

## Jak agenta spustit

Agenta typicky spouštíš z terminálu ve složce s projektem, například příkazem `claude` nebo `codex`. Po spuštění mu napíšeš zadání v češtině nebo angličtině – stejně, jako bys ho napsal/a spolužákovi, který ti má s úkolem pomoct.

## Časté chyby
- Zadání příliš obecné („udělej mi hru“) – agent neví, co přesně chceš. Čím konkrétnější zadání, tím lepší výsledek.
- Očekávání, že agent bez dohledu udělá úplně všechno správně napoprvé – i agent dělá chyby, jen je dokáže sám najít a někdy i opravit.
- Spuštění agenta mimo správnou složku s projektem – agent pak nevidí soubory, se kterými má pracovat.

## Vyzkoušej
Zkus agentovi zadat jednoduchý úkol, například: *„Vytvoř soubor pozdrav.py, který se uživatele zeptá na jméno a pozdraví ho.“* Sleduj, jaké kroky agent dělá – jestli si nejdřív řekne plán, jaké soubory vytváří a jestli si na konci sám spustí kód, aby ověřil, že funguje.
