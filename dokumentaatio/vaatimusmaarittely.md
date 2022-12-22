# Vaatimusmäärittely

## Sovelluksen tarkoitus

Kyseessä on jäsenrekisterisovellus. Sovelluksen tarkoituksena on säilyttää jäsenyystietoa ja esittää se selkeässä muodossa. 

## Käyttäjät

Sovelluksessa on kahdenlaisia käyttäjiä: jäseniä ja järjestötoimijoita (admineita).

## Toiminnallisuudet

### Jäsenet

#### Ennen kirjautumista jäsen:
- voi luoda käyttäjätunnuksen
  - käyttäjätunnuksen tulee olla uniikki ja vähintään 3 merkkiä pitkä 
  - salasanan täytyy olla vähintään 8 merkkiä 
  - lisäksi kirjautumisen yhteydessä tulee antaa nimi
- voi kirjautua antamalla käyttäjätunnuksen ja salasanan
  - sovellus ilmoittaa, mikäli ne menivät väärin

#### Kirjautumisen jälkeen jäsen:
- voi tarkastella ja muokata omia tietojaan 
  - nimi, sähköpostiosoite, puhelinnumero, jäsenyyden voimassaolo
- voi tarkastella jäsenyyden uusimisohjeita
- voi liittyä järjestötoimijaksi (adminiksi)

### Järjestötoimijat (adminit)

#### Ennen kirjautumista järjestötoimija:
- voi kirjautua antamalla käyttäjätunnuksen ja salasanan 
  - sovellus ilmoittaa, mikäli ne menevät väärin

#### Kirjautumisen jälkeen järjestötoimija:
- voi tarkastella ja muokata omia tietojaan 
  - nimi, sähköpostiosoite, puhelinnumero, jäsenyyden voimassaolo
- voi tarkastella voimassa olevia ja voimassa olemattomia jäsenyyksiä
- voi muokata jäsenten jäsenyystietoja 
- voi hakea käyttäjiä nimellä tai käyttäjätunnuksella
- voi tarkastella jäsenyyden uusimisohjeita
- voi muokata jäsenyyden uusimisohjeita
- voi poistaa käyttäjiä
- voi palautua takaisin tavalliseksi käyttäjäksi

## Jatkokehitysideoita
Sovellukseen voi lisätä seuraavia toiminnallisuuksia:
- Useamman järjestön jäsenyyksien ylläpito samalla sovelluksella
  - Käyttäjä voi tarkastella monia jäsenyyksiä samalla käyttäjätunnuksella
- Jäsenyyden ehtojen (jäsenmaksu ja muut ehdot) tarkistamisen automatisointi

Sovellus voidaan myös integroida osaksi suurempaa järjestötoimintasovellusta
