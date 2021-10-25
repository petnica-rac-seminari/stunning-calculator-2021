Program prepoznaje nacrtane cifre pomoću neuronske mreže, metode mašinskog učenja.
Koristi MNIST bazu podataka koja sadrži 7000 slika dimenzija 28*28 piksela (svaka u obliku vektora dužine 768 sa toliko float vrednosti) i uči na osnovu trening i testing seta.

Neuronska mreža sadrži 2 skrivena sloja (500 i 100 vrednosti) i na kraju određuje verovatnoće za 10 cifara. Cifra kroju definiše najveća verovatnoća se šalje kao krajnji rezultat.

