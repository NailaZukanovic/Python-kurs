# class Ucenik:
# # Staticke varijable
#     # ime = ''
#     # prezime = ''
#     # datum = ''
#     # student = False

#     def __init__(self, i, p, d, s): #u trenutku kreiranja varijable, ovo ce se izvrsiti    self znaci da kad se izvrsi to je za tu varijablu
# #        print('Izvrsavanje __init__')
# # obicne varijable
#         self.ime = i
#         self.prezime = p
#         self.datum = d
#         self.student = s

# # Nikad ne koristi defaultne vrednosti

# #Ako koristis onda Ucenik(i='Dzemil',d='04.07') ostali ostaju ne inicijalizirani

#     def ispisati_ime(self):
#         print('Moje ime je', self.ime)







# dzemil = Ucenik('Dzemil','Dupljak','04.07', True)


# dzemil.ispisati_ime()

# dzemil.ime = 'Novo ime'

# petar = Ucenik()

# petar.ime = "Petar"

# petar.prezime = 'Vucinic'

# petar.datum = "11.02."

# petar.student = False

# print(petar.ime, petar.prezime)

# print(type(petar))

# print(type(petar.ime))

# var1 = Ucenik()

# var1.ime = 'Hamza'

# print(var1.ime, var1.prezime)



# class Radnik:

#     def __init__ (self,ime,prezime,radno_mesto,satnica,vrsta_posla,br_radnih_dana ):
#         self.ime = ime
#         self.prezime = prezime
#         self.radno_mesto = radno_mesto
#         self.satnica = satnica
#         self.vrsta_posla = vrsta_posla
#         self.br_radnih_dana = br_radnih_dana 
#         self.plata = self.satnica * 8 * 24

#     def ispisi_platu(self):
#         print('Moja plata je', self.plata)


#     def izvestaj_meseca(self):
#         print('Zaradio je', self.br_radnih_dana * self.satnica)

#     def __str__(self): #Umesto defaultnog u kome ispisuje adresu
#         return f'Ime radnika: {self.ime}, prezime radnika: {self.prezime}'

# class Ucitelj(Radnik):
#     def __init__(self,broj_c):
#         self.broj_casova = b


# ja = Radnik('Neko','Nesto','Negde',50,'radi',4)

# ja.izvestaj_meseca()

# print(ja)

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# #onaj projekat kroz OOP

# countries = []

# from classes import Drzava

# # ##################################################################

# head, countries = Drzava.set_state_of_countries("C:/Users/Comp/Desktop/saDesktopa/pythonNaila/Emissions.csv")

# y = 2000

# mini, maxi, avg = Drzava.get_min_max_avg_by_year(head.godine.index(y), countries)

# print(mini,maxi,avg)

# # for i in countries:
# #     print(i)


# var1 = [-5,-4,-3,-2,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,100]

# min_num = None
# min_val = max(var1)
# for i in var1:
#     #zbog negativnog ide i - avg
#     if abs(i - sum(var1) / len(var1)) < min_val:
#         min_val = abs(i - sum(var1) / len(var1))
#         mun_num = i

# print(sum(var1) / len(var1))

# print(min_num)

# #update ovo u f-ji

# #matplotlib pogledaj
 
# #da se prikazuje drzava po godinama, drzave po godinama, godine po drzavama min,max,avg 

# class Predmet:
    
#     _nazivPredmeta
#     _imeProfesora
#     _prezimeProfesora
#     _fontCasova
#     _brUcenika
#     _brOdrzanihCasova
#     _udzbenik

# class Geografija(Predmet):
#     __terenskiRad

#     __init__(self,ime,prezime,font, ucenici, casovi, udzbdenik, terenskiRad):
#         self._nazivPredmeta
#         self._imeProfesora = ime 
#         self._prezimeProfesora = prezime
#         self._fontCasova = font 
#         self._brUcenika = ucenici
#         self._brOdrzanihCasova = casovi
#         self._udzbenik = udzbenik 
#         self.__terenskiRad = terenskiRad

#     __str__(self):
#         return f"{_imeProfesora} {_prezimeProfesora}"

    

# class Lekar():

#     def __init__(self,ime,lbo,bolnica,brPacijenta,fakultet):
#         self._imeIPrezime = ime 
#         self._lbo = lbo
#         self._bolnica = bolnica
#         self._brPacijenta = brPacijenta
#         self._fakultet = fakultet


