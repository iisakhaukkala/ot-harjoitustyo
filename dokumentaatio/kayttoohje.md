# Käyttöohje

Projektin lähdekoodi löytyy pakattuna tiedostona [viimeisimmästä releasesta](https://github.com/iisakhaukkala/ot-harjoitustyo/releases/tag/v1.0.0) _Assets_ osion alta. Pura tiedosto ennen sen käyttämistä.

## Konfigurointi

Tiedon pysyväistallennuksessa käytettävien tiedostojen nimiä voi muokata päähakemiston _.env_-tiedostossa. Tiedostot luodaan automaattisesti _data_-hakemistoon, jos niitä ei siellä vielä ole. _.env_-tiedoston muoto on seuraava:

```
DATABASE_FILENAME = register.sqlite
INFO_FILENAME = info.txt
```

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

## Käyttäminen

Sovelluksessa on tekstikäyttöliittymä, jota käytetään komentoriviltä. Eri näkymissä komennolla 'k' saa näkyviin komennot.
