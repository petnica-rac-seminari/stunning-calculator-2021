# BACKEND ZA ,,STUNNING CALCULATOR''

### INTRODUCTION:

Backend(server) za program ,,stunning calculator''

### FEATURES:
- Sastoji se od pet fajlova
- Pokretanje servera se odvija poktrtanjem fajla server.py
- Server prima listu sa frontenda(GUI-a)
- response.py modul prima i obradjuje podatke
- pretvara listu u numpy array tipa uint8 i salje ML modulu
- Povratnu vrednost funkcije salje clientu nakon provere da li je cifra.

### TABLE OF CONTENTS:
- [imageObject.py](imageObject.py) 
- [response.py](response.py)
- [server.py](server.py)
- [status_codes.py](status_codes.py)

### REQUIREMENTS:
pydantic</br>
flask</br>
numpy



# MACHINE LEARNING README

## INTRODUCTION:
machine learning algoritam za porgram ,,stunning calculator"

## FEATURES:
- Sastoji se od 4 fajla i jednim koji se sastoji od parametara
- Prima podatke sa frontenda koje je poslao server u obliku numpy arraya
- Učitava vrednosti piksela (28*28) i preko neuronskih mreža (MNIST baza podataka sa 70000 slika cifara) uči da prepoznaje nacrtane cifre
- Cifru za koju odredi da je naujveća verovatnoća je je ucrtana šalje dalje serveru

## TABLE OF CONTENTS:
- [dataset.py](dataset.py)
- [prepoznavanje.py](prepoznavanje.py)
- [ucenje.py](ucenje.py)
- [utils.py](utils.py)
- [parameters]

## REQUIREMENTS:

numpy
pydentic
mlxtend

( MNIST database: http://yann.lecun.com/exdb/mnist/ ) (učitati, unzipovati i staviti u server.py)





