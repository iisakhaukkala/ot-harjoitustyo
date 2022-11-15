# Vaatimusmäärittely

## Sovelluksen tarkoitus

Kyseessä on jäsenrekisterisovellus. Sovelluksen tarkoituksena on säilyttää jäsenyystietoa ja esittää se selkeässä muodossa. 

## Käyttäjät

Sovelluksessa on kahdenlaisia käyttäjiä: jäseniä ja järjestötoimijoita.

## Toiminnallisuudet

### Jäsenet

#### Ennen kirjautumista jäsen:
- voi luoda käyttäjätunnuksen
  - käyttäjätunnuksen tulee olla uniikki
  - salasanan täytyy olla vähintään 8 merkkiä
- voi kirjautua antamalla käyttäjätunnuksen ja salasanan
  - sovellus ilmoittaa, mikäli ne menivät väärin

#### Kirjautumisen jälkeen jäsen:
- voi muokata omia tietojaan
  - nimi, sähköpostiosoite, puhelinnumero
- näkee, mihin saakka hänen jäsenyytensä on voimassa
- näkee, miten jäsenyyden voi uusia
- näkee jäsenyysyhteyshenkilön yhteystiedot

### Järjestötoimijat

Järjestötoimijan roolin saa sovelluksen ylläpitäjältä

#### Ennen kirjautumista järjestötoimija:
- voi kirjautua antamalla käyttäjätunnuksen ja salasanan
  - sovellus ilmoittaa, mikäli ne menevät väärin

#### Kirjautumisen jälkeen järjestötoimija:
- voi tarkastella voimassa olevia ja voimassa olemattomia jäsenyyksiä
- voi muokata jäsenten jäsenyystietoja
- voi hakea jäseniä nimellä tai käyttäjätunnuksella
- näkee, kuinka monta jäsenyyttä on voimassa
- voi muokata jäsenille näkyviä uusimisohjeita sekä jäsenyysyhteyshenkilön yhteystietoja

## Jatkokehitysideoita
Sovellukseen voi lisätä seuraavia toiminnallisuuksia:
- Useamman järjestön jäsenyyksien ylläpito samalla sovelluksella
  - Käyttäjä voi tarkastella monia jäsenyyksiä samalla käyttäjätunnuksella
- Jäsenyyden ehtojen (jäsenmaksu ja muut ehdot) tarkistamisen automatisointi

Sovellus voidaan myös integroida osaksi suurempaa järjestötoimintasovellusta
