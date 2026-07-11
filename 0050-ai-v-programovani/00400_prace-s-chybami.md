# Práce s chybovými hláškami

## Proč se chyb nebát

Chybová hláška (*traceback*) není trest – je to informace, kde přesně a proč program selhal. AI agent umí tuhle informaci využít mnohem rychleji, než bys hledal/a chybu ručně, ale musíš mu ji dát k dispozici.

## Jak předat chybu agentovi

Když program spadne, zkopíruj celou chybovou hlášku (ne jen poslední řádek) a vlož ji agentovi spolu s popisem, co jsi očekával/a:

```
Traceback (most recent call last):
  File "poznamky.py", line 12, in <module>
    pocet = int(radek)
ValueError: invalid literal for int() with base 10: ''
```

> „Dostávám tuhle chybu, když spouštím poznamky.py a soubor je prázdný. Oprav to, prosím.“

## Co agent (obvykle) udělá
- najde soubor a řádek, kde chyba nastala,
- najde příčinu (v příkladu výše: pokus o převod prázdného textu na číslo),
- navrhne opravu – a u CLI agenta ji rovnou může do souboru zapsat.

> I opravený kód si vždy spusť znovu. Agent tvrdí, že je to opravené – jediný důkaz je funkční program.

## Když chyba přetrvává

Pokud oprava nezabrala, dej agentovi vědět přesně, co se stalo teď – novou chybovou hlášku, nebo popis špatného chování („program běží, ale poznámka se neuloží“). Postupné upřesňování funguje lépe než opakování stejného zadání pořád dokola.

## Časté chyby
- Vložení jen části chybové hlášky – agent nemusí vidět, kde přesně problém vznikl.
- Popis chyby jako „nefunguje to“ bez chybové hlášky nebo popisu, co se skutečně stalo.
- Přijetí opravy bez opětovného spuštění programu.

## Vyzkoušej

Do své aplikace z předchozí lekce úmyslně zaveď chybu (například přejmenuj proměnnou jen na jednom místě) a nech agenta, ať ji najde a opraví jen na základě chybové hlášky, kterou mu pošleš.
