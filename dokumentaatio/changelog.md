## Viikko 3
- Alustava yksinkertainen käyttöliittymä
- Tietokannan alustaminen toimii
- Tietokantaan voi luoda käyttäjän
- Käyttäjät voidaan tulostaa
- Testattu, että käyttäjien luonti sekä tulostaminen toimii

## Viikko 4
- Toiminnot on jaoteltu järkevästi luokkiin
- Ohjelma tarkistaa, että uuden käyttäjän käyttäjätunnus sekä salasana ovat määritellyn kaltaisia ennen käyttäjän luomista
- Käyttäjä voi kirjautua sisään (kirjautuneena ei voi toki tehdä vielä mitään järkevää)
- RegisterRepository -luokalla on enemmän toimintoja, osa niistä testattu
- RegisterService -luokalla on enemmän toimintoja, ei testattu
- Käyttöliittymä toimiii tarkoituksenmukaisesti nykyisillä toiminnoilla

## Viikko 5
- RegisterRepository -luokan toiminnot valmiit, luokan testikattavuus 100 %
- RegisterService -luokalla suurin osa toiminnoista, luokan testikattavuus 54 %
- Käyttöliittymä toimii
- Käyttäjä voi kirjautuneena tarkastella ja muokata omia tietojaan
- Käyttäjä voi liittyä adminiksi
- Admin voi tehdä samat asiat kuin tavallinen käyttäjä
- Admin voi poistaa itseltään admin-oikeudet

## Viikko 6
- Määrittelydokumentin toiminnot toimivat, lukuun ottamatta voimassa olevien (ja olemattomien) jäsenyyksien tulostamista
- Ongelman korjaantuminen vaatii membership-tietojen tallentamisen date-olioina merkkijonon sijaan
- Testikattavuus nykyisillä toiminnoilla 97 %
