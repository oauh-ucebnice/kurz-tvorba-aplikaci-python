# Co je AI agent

## Co už znáš – Copilot

Copilot v editoru navrhuje řádky nebo celé bloky kódu přímo tam, kde píšeš – ty návrh potvrdíš klávesou Tab, nebo se ho na něco zeptáš v chatu. Copilot vždy čeká na tebe u každého kroku – ty rozhoduješ, co se stane dál.

## AI agent

AI agent (například Claude Code nebo Codex) běží v terminálu (příkazové řádce, zkráceně CLI) a na rozdíl od Copilota umí pracovat samostatně – na základě jednoho zadání v přirozeném jazyce:

- přečte zdrojové kódy v projektu,
- napíše nebo upraví kód ve víc souborech najednou,
- spustí příkaz (třeba testy) a podle výsledku pokračuje, nebo se sám opraví.

Rozdíl je hlavně v samostatnosti: Copilotovi zadáváš jeden krok, agentovi klidně celý úkol – a on si kroky rozplánuje sám.

## Kdy použít co

| Situace | Lepší volba |
|---|---|
| Převážně píši kód sám, AI využívám jako výpomoc | Copilot v editoru |
| Chci se rychle na něco zeptat, aniž bych opouštěl/a editor | Copilot Chat |
| Chci sledovat cíl projektu, do kódu nahlížím jen občas | AI agent (CLI) |
| Chci, aby AI sama spustila program a opravila chybu, kterou najde | AI agent (CLI) |

> Agent není „chytřejší“ Copilot – pořád rozhoduješ, co má agent dělat a stále zodpovídáš za výsledek.

## Jak agenta spustit

Agenta typicky spouštíš z terminálu (příkazového řádku) ve složce s projektem, například příkazem `claude` nebo `codex`. Po spuštění mu napíšeš zadání v češtině nebo angličtině – stejně, jako bys ho napsal/a kolegovi, který ti má s úkolem pomoct.

## Časté chyby
- Zadání příliš obecné („udělej mi hru“) – agent neví, co přesně chceš. Čím konkrétnější zadání, tím lepší výsledek.
- Očekávání, že agent bez dohledu udělá úplně všechno správně napoprvé – i agent dělá chyby, jen je dokáže sám najít a někdy i opravit.
- Spuštění agenta mimo správnou složku s projektem – agent pak nevidí soubory, se kterými má pracovat.

## Vyzkoušej

1. Ve složce `Dokumenty` vytvoř novou složku `pokus` – klidně v Průzkumníku.
2. Spusť příkazový řádek – třeba tak, že klikneš na Start a zapíšeš `cmd`.
3. Přejdi do složky `pokus` příkazem:
   ```shell
   cd Dokumenty/pokus
   ```
4. Spusť agenta příkazem `codex` (případně `claude` či jiném podle toho, jakého agenta máš nainstalovaného).
5. Zkus agentovi zadat jednoduchý úkol, například: 
   
   Sleduj, jaké kroky agent dělá – jestli si nejdřív řekne plán, jaké soubory vytváří a jestli si na konci sám spustí kód, aby ověřil, že funguje.

Příklady zadání pro Python:

```
Vytvoř aplikaci v Pythonu, která se uživatele zeptá na jméno a pozdraví ho.
```

## Příklad zadání pro Greenfoot

```
Vytvoř projekt v Greenfootu v jazyce Java. Hráč se bude pohybovat pomocí kurzoru myši.
Hráč bude sbírat bonusy. Na začátku hry bude na hrací ploše pět bonusů.
 
Nyní přidej obrázek na pozadí a vylepši a vylepši obrázky hráče a bonusů. Hráč by mohl mít obrázek kočky a bonusy budou myši. Na pozadí bude stará zahrada s květinami.
```
