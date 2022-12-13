# Jäsenrekisterisovellus

Sovellus on harjoitustyö, joka on tehty osana Helsingin yliopiston kurssia Ohjelmistotekniikka. Sovelluksen tarkoituksena on helpottaa järjestön tai muun vastaavan toimijan jäsenrekisterin ylläpitoa.

## Releaset

- [viikko5](https://github.com/iisakhaukkala/ot-harjoitustyo/releases/tag/viikko5)
- {viikko6](https://github.com/iisakhaukkala/ot-harjoitustyo/releases/tag/viikko6)

## Dokumentaatio

- [Changelog](https://github.com/iisakhaukkala/ot-harjoitustyo/blob/master/dokumentaatio/changelog.md)

- [Arkkitehtuurikuvaus](https://github.com/iisakhaukkala/ot-harjoitustyo/blob/master/dokumentaatio/arkkitehtuuri.md)

- [Vaatimusmäärittely](https://github.com/iisakhaukkala/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)

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
