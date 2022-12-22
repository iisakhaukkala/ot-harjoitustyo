# Jäsenrekisterisovellus

Sovellus on harjoitustyö, joka on tehty osana Helsingin yliopiston kurssia Ohjelmistotekniikka. Sovelluksen tarkoituksena on helpottaa järjestön tai muun vastaavan toimijan jäsenrekisterin ylläpitoa.

## Release

[Viimeisin release](https://github.com/iisakhaukkala/ot-harjoitustyo/releases/tag/22.12.2022)

## Dokumentaatio

- [Käyttöohje](https://github.com/iisakhaukkala/ot-harjoitustyo/blob/master/dokumentaatio/kayttoohje.md)
- [Vaatimusmäärittely](https://github.com/iisakhaukkala/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)
- [Arkkitehtuurikuvaus](https://github.com/iisakhaukkala/ot-harjoitustyo/blob/master/dokumentaatio/arkkitehtuuri.md)
- [Testausdokumentti](https://github.com/iisakhaukkala/ot-harjoitustyo/blob/master/dokumentaatio/testaus.md)
- [Changelog](https://github.com/iisakhaukkala/ot-harjoitustyo/blob/master/dokumentaatio/changelog.md)
- [Tuntikirjanpito](https://github.com/iisakhaukkala/ot-harjoitustyo/blob/master/dokumentaatio/tuntikirjanpito.md)
 
## Asennus ja käynnistäminen

1. Asenna riippuvuudet komennolla:

```bash
poetry install
```

2. Suorita alustustoimenpiteet komennolla:

```bash
poetry run invoke build
```

3. Käynnistä sovellus komennolla:

```bash
poetry run invoke start
```

## Muut komentorivikomennot

### Testikattavuusraportti

Testikattavuusraportin voi koostaa komennolla:

```bash
poetry run invoke coverage-report
```

Testikattavuusraportti koostetaan _htmlcov_-hakemistoon

### Pylint

Pylint-raportin voi koostaa komennolla: 

```bash
poetry run invoke lint
```
