# Vaatimusmäärittely

## Sovelluksen tarkoitus

Kyseessä on jäsenrekisterisovellus. Sovelluksen tarkoituksena on säilyttää jäsenyystietoa ja esittää se selkeässä muodossa. 

## Käyttäjät

Sovelluksessa on kahdenlaisia käyttäjiä: jäseniä ja järjestötoimijoita (admineita).

## Toiminnallisuudet

### Jäsenet

#### Ennen kirjautumista jäsen:
- voi luoda käyttäjätunnuksen (tehty)
  - käyttäjätunnuksen tulee olla uniikki ja vähintään 3 merkkiä pitkä (tehty)
  - salasanan täytyy olla vähintään 8 merkkiä (tehty)
- voi kirjautua antamalla käyttäjätunnuksen ja salasanan (tehty)
  - sovellus ilmoittaa, mikäli ne menivät väärin (tehty)

#### Kirjautumisen jälkeen jäsen:
- voi muokata omia tietojaan (tehty)
  - nimi, sähköpostiosoite, puhelinnumero (tehty)
- näkee, mihin saakka hänen jäsenyytensä on voimassa (tehty)
- näkee, miten jäsenyyden voi uusia (tehty)
- näkee jäsenyysyhteyshenkilön yhteystiedot (tehty)
- voi liittyä järjestötoimijaksi (adminiksi) (tehty)

### Järjestötoimijat (adminit)

#### Ennen kirjautumista järjestötoimija:
- voi kirjautua antamalla käyttäjätunnuksen ja salasanan (tehty)
  - sovellus ilmoittaa, mikäli ne menevät väärin (tehty)

#### Kirjautumisen jälkeen järjestötoimija:
- voi muokata omia tietojaan (tehty)
  - nimi, sähköpostiosoite, puhelinnumero (tehty)
- voi tarkastella voimassa olevia ja voimassa olemattomia jäsenyyksiä
- voi muokata jäsenten jäsenyystietoja (tehty)
- voi hakea käyttäjiä nimellä tai käyttäjätunnuksella (tehty)
- voi muokata jäsenille näkyviä uusimisohjeita sekä jäsenyysyhteyshenkilön yhteystietoja (tehty)
- voi palautua takaisin tavalliseksi käyttäjäksi (tehty)

## Jatkokehitysideoita
Sovellukseen voi lisätä seuraavia toiminnallisuuksia:
- Useamman järjestön jäsenyyksien ylläpito samalla sovelluksella
  - Käyttäjä voi tarkastella monia jäsenyyksiä samalla käyttäjätunnuksella
- Jäsenyyden ehtojen (jäsenmaksu ja muut ehdot) tarkistamisen automatisointi

Sovellus voidaan myös integroida osaksi suurempaa järjestötoimintasovellusta
