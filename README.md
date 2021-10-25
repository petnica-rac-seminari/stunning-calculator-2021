### FEATURES

- Kalkulator na kom se brojevi unose crtanjem 
- Cifre se unose zasebno, jedna po jedna
- Sadrzi osnovne operacije: sabiranje, oduzimanje, mnozenje i deljenje
- Moguce je napraviti slozenije brojeve(ako se izmedju unosa cifara ne unese operacija)
- Dugme ,,Recognize'' prepoznaje unetu cifru i upisuje je u izraz
- Dugme jednako racuna izraz

### STRUKTURA
- Sastoji se od dva glavna foldera: server i client
- U server folderu nalaze se fajlovi za pokretanje servera
- U server folderu se takodje nalazi i modul za machine learning(prepoznavanje cifara)
- U client folderu se nalazi GUI za kalkulator

### STARTUP
- Prvo je potrebno podici server pokretanjem fajla server.py koji se nalazi u server folderu
- Nakon podizanja servera da bi se otvorio GUI potrebno je pokrenuti gui.py koji se nalazi u client folderu
