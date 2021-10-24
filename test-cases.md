Test cases
Happy path:
Kada se pokrene program otvori se GUI
Kada se nacrta jednocifran broj on se upisuje u buffer
Kada se upiše neželjeni broj ili operacija, izbriše se klikom na backspace
Provera ispravnosti prioriteta operacija:
2*5+2-9/3

Sad path:
Kada korisnik pošalje prazan kanvas, ne upisuje se ništa u buffer
Ako je buffer prazan, kada se klikne na backspace ne dešava se ništa
Kada se unese broj koji nije jednocifren 
Kada se izabere više puta zaredom + ili - dobija se tačan rezultat
5 ++++ 2 = 7
5 ------- 2 = 3
Kada se unese više puta zaredom * ili / dobija se obaveštenje da je upis matematički neispravan
2 ** 5 
2 // 5 
5/0 dobija se obaveštenje da je upis matematički neispravan
5/0+1 dobija se obaveštenje da je upis matematički neispravan
