# Stunning calculator

## Opis problema

Potrebno je napraviti kalkulator koji kada se pravilno nacrtaju jednocifreni brojevi daje izbor matematickih operacija i potom na datim brojevima vrsi izabrane funkcije.

Program je podeljen na Client (Front-end) i Server(Back-end). Client ne treba da izvrsava nikakve operacije, vec salje unos serveru i ceka rezultat.

Treba neuronskom mrezom da se napravi algoritam (funkcija) koja prevodi sliku u INT, zatim da se odrade matematicke operacije na istoj.

1.
## Funkcionalna specifikacija:

  1. Unos i prepoznavanje brojeva
    1. Unos je jednocifrenog broja
    2. Unos je na prazan kanvas
    3. Kada se stisne enter unosi se u buffer i cisti se kanvas
  2. Izbor operacija i korekcija izraza
    1. Sabiranje, oduzimanje, mnozenje, deljenje
    2. Kada se izabere operacija ona se umece u buffer
    3. Klikom na backspace dugme iz buffera se brise poslednja uneta informacija (karakter)
  3. Izracunavanje izraza
    1. Izraz uvek stoji u bufferu, prilikom unosa se rezultat osvezava (ponovo racuna izraz) i upisuje se u textbox za rezultat.
    2. Postoje 2 stanja rezultata
      1. Izracunato
      2. Greska
  4. Obrada gresaka
    1. prepoznavanje greska - server za prepoznavanje ne vraca korektnu vrednost
    2. input greska - neispravan unos u buffer
    3. matematicka greska - unos zabranjene matematicke operacije
  5. Korisnicki interfejs
    1. to be link...
2.
## Nefunkcionalna specifikacija:

  1. Slika ne sme da se cuva na disk
  2. Servis za prepoznavanje slika je odvojen server sa kojim se komunicira preko HTTP API-a
  3. Potrebno je koristiti iskljucivo python (3.x)
  4. Potrebno je koristiti tkinter biblioteku
3.
## Arhitektura

  1. Client
    1. Graphical user interface
      1. U zavisnosti koje dugme je kliknuto (operacija, enter, backspace) poziva se potreban modul.
      2. Modul za komunikaciju sa serverom
      3. Modul za evaluaciju
      4. Modul za parse slike
    2. Modul za parse slike
      1. Prima &quot;canvas&quot; object
      2. Vraca image objekat koji je niz byteova duzine 784
    3. Modul za komunikaciju sa serverom
      1. Modul ce sadrzati funkcije za slanje HTTP requesta serveru
      2. Pozivanjem funkcija ce se sacekati odgovor od servera
      3. Funkcije vracaju celobrojnu vrednost (uneti broj)
    4. Modul za evaluaciju
      1. Treba da primi izraz iz buffera kao string
      2. Treba da pokusa evaluaciju stringa
      3. U slucaju greske pri evaluaciji baca exception
      4. Vraca float vrednost kao rezultat
    5. Slanje podataka serveru
      1. Salje se niz byteova koji je dugacak 784 u JSON formatu
    6. Primanje odgovora servera
      1. Odgovor servera moze biti greska ili ocekivana vrednost
      2. Pri dobijanju odgovora ako nije doslo do greske, vrednost se upisuje u buffer i poziva se modul za evaluaciju
      3. Ako je odgovor greska, client to treba dati do znanja korisniku tako sto ispisuje gresku
  2. Server
    1. Primanje podataka preko endpointa za post requestove clienta
      1. Server prima reprezentaciju slike u JSON formatu
    2. Slanje odgovora (response)
      1. U slucaju da nema greske server odgovara sa celim brojem i status kodom 200
      2. U slucaju pogresnog requesta server vraca status kod 400
      3. U slucaju greske pri prepoznavanju slike server vraca unexpected error, kod 500
    3. Server importuje modul za prepoznavanje slika
  3. Modul za prepoznavanje slika
    1. Modul uvek pretpostavlja da je dobio validan podatak.
    2. Nacin za prepoznavanje slike