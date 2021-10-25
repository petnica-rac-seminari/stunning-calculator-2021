# Test cases

## Happy path:

1. Kada se pokrene program otvori se GUI
2. Kada se nacrta jednocifran broj on se upisuje u buffer
3. Kada se upiše neželjeni broj ili operacija, izbriše se klikom na backspace
4. Provera ispravnosti prioriteta operacija:
    2*5+2-9/3

## Sad path:
1. Kada korisnik pošalje prazan kanvas, ne upisuje se ništa u buffer
2. Ako je buffer prazan, kada se klikne na backspace ne dešava se ništa
3. Kada se unese broj koji nije jednocifren, ispisuje je se jednocifren prepoznat broj
4. Kada se izabere više puta zaredom + ili - dobija se tačan rezultat
5. Kada se unese više puta zaredom * ili / dobija se obaveštenje da je upis neispravan
6. 5/0 dobija se obaveštenje da je upis neispravan
7. 5/0+1 dobija se obaveštenje da je upis neispravan
