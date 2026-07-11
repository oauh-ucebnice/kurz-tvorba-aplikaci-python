# Na co si dát pozor

## Halucinace

AI si někdy vymyslí něco, co neexistuje – třeba knihovnu, funkci nebo parametr, který ve skutečnosti není součástí Pythonu. Tomuto jevu se říká *halucinace*. Kód pak vypadá důvěryhodně a je napsaný sebejistě, ale při spuštění skončí chybou, protože daná věc prostě neexistuje.

> Halucinaci nepoznáš podle tónu odpovědi – AI zní stejně sebejistě, ať má pravdu, nebo ne. Jediný spolehlivý způsob, jak si být jistý/á, je kód spustit a výsledek zkontrolovat.

## Bezpečnost a soukromí

Cokoli napíšeš AI nástroji, může být uloženo na serverech firmy, která ho provozuje. Proto:
- nikdy nevkládej do promptu hesla, přístupové tokeny ani API klíče,
- nevkládej osobní údaje svoje ani spolužáků (rodná čísla, adresy, telefonní čísla),
- pokud pracuješ na školním nebo firemním projektu, ověř si, jestli je použití AI nástrojů povolené a s jakými daty smíš pracovat.

> Pokud si nejsi jistý/á, jestli je bezpečné něco AI nástroji poslat, radši to nepošli. Citlivá data z konverzace s AI se dost dobře nedají „vzít zpátky“.

## Kdy AI nepoužívat
- Když úkolu ještě nerozumíš – nech si od AI nejdřív princip vysvětlit, ne rovnou hotové řešení. Jinak se nic nenaučíš.
- Když jde o citlivá nebo důvěrná data.
- Když potřebuješ jistotu, že je výsledek stoprocentně správný, aniž bys ho sám/sama ověřoval/a – AI dělá chyby a je jen nástroj, ne konečná autorita.

## Časté chyby
- Slepé zkopírování kódu od AI bez spuštění a kontroly.
- Vložení citlivého údaje do promptu „jen na zkoušku“.
- Použití zastaralého nebo neexistujícího řešení, které AI navrhla s jistotou.

## Vyzkoušej
Zkus agentovi zadat úmyslně nesmyslný nebo neexistující požadavek, například: *„Použij v Pythonu knihovnu quicksort_visualizer_pro.“* Sleduj, jak agent zareaguje – přizná, že knihovna neexistuje, nebo se ji pokusí „vymyslet“?
