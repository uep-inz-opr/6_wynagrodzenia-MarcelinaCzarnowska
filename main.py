liczba_pracownikow = int(input())


class Pracownik:
    def __init__(self,imie,wyplata_brutto):
        
        self.imie = imie
        self.wyplata_brutto = wyplata_brutto
        self.wyplata = round(self.wyplata_brutto - self.skladka - self.ubezpieczenie - self.podatek,2)
        self.skladka = round(self.wyplata_brutto*0.0976,2) + round(self.wyplata_brutto*0.015,2) + round(self.wyplata_brutto*0.0245,2)
        self.podatek = round((round((round(self.wyplata_brutto-111.25 - self.skladka,2))*0.18,2)-46.33) - round((round(self.wyplata_brutto-self.skladka,2))*0.0775,2),0)
        self.ubezpieczenie = round((self.wyplata_brutto - self.skladka)*0.09,2)
        self.koszt_pracodawcy = round(self.wyplata_brutto*0.0976,2) + round(self.wyplata_brutto*0.065,2) + round(self.wyplata_brutto*0.0193,2) + round(self.wynagrodzenie_brutto*0.0245,2) + round(self.wynagrodzenie_brutto*0.001,2)

    def __repr__(self):
        #return "{} {}".format{self.imie:.2f}..
        return f"{self.imie} {self.wyplata:.2f} {self.koszt_pracodawcy:.2f} {self.wyplata_brutto+self.koszt_pracodawcy:.2f}"
    
    def koszt_koncowy(self):
        return self.wyplata_brutto + self.koszt_pracodawcy


dane_pracownikow = []
laczny_koszt = 0

for pracownik in range(liczba_pracownikow):
    dane_wejscowe = input()
    dane_pracownikow.append(dane_wejscowe)

for dane in dane_pracownikow:
    imie = dane.split(' ')[0]
    wyplata = int(dane.split(' ')[1])
    pracownik = Pracownik(imie,wyplata)
    
    laczny_koszt+=pracownik.koszt_koncowy()


print(f"{laczny_koszt:.2f}")