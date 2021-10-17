# #funkcija

# def naziv_funkcije(var1):
#     print(30*'=')
#     print('Telo funkcije')
#     print('Vrednost var1(lokalne varijable)', var1)


# naziv_funkcije(23)
# naziv_funkcije(43)
# naziv_funkcije(65)


# a = 10
# b = 20

# c = a + b

# print(c)

# a = 54
# b = 24

# c = a + b

# print(c)

# def jelParan(broj):
#     if broj % 2 == 0:
#         print('Paran je')
#     else:
#         print('Neparan je')

# jelParan(int(input))


# def ispisiImeIGodinu(ime,godina):
#     print(ime,godina)

# ime = input('Unesite ime')
# godina = int(input('Unesite godinu'))

# ispisiImeIGodinu(ime,godina) 

# useri = {}

# # jedna * kreira pokazivac na tuple , ** kriera pokazivac na dictionary

# def kreiranje_usera(ime, *args,**kwargs):
#     useri[ime] = kwargs

# novi_arg = 5
# kreiranje_usera('dzemil',novi_arg,'jos_jedna_vrednost',prezime = 'dupljak',godine = 25, skola = 'gimnazija')

# broj = int(input('Unesite broj'))
# def jelParan(broj):
#     if broj % 2 == 0:
#         print('Paran je')
#     else:
#         print('Neparan je')

# def jelNegativan(broj):
#     if broj < 0:
#         print('Negativan je')
#     elif borj == 0:
#         print('BRoj jw nula')
#     else:3
#         print('BRoj je pozitivan')


# jelParan(broj)
# jelNegativan(broj)


# def unosListe():
#     kor_lista = []
#     print('Unesite elemente niza, '' za kraj')
#     while True:
#         element = input('Unesite element')
#         if not element: #ako element ne postoji
#             break
#         kor_lista.append(int(element))
#     return kor_lista

# def ispis_elemenata(lista):
#     for i in lista:
#         print(i,end = ' ')
#     print()

# def obrnutiIspis(lista):
#     lista.reverse()
#     ispis_elemenata(lista)
    

# def ispisiParne(lista):
#     for i in lista:
#         if i % 2 == 0:
#             print(i,end = ',')

# def napraviti_matricu():
#     matrica = []
#     print('Unesite dimenzije matrice')
#     brRedova= int(input('Red:'))
#     brKolona = int(input('Kolona:'))
#     for i in range(brRedova):
#         red = []
#         for j in range(brKolona):
#             element = int(input('Unesite element'))
#             red.append(element)
#         matrica.append(red)
#     return matrica

# def ispisati_matricu(matrica):
#     for i in matrica:
#         for j in i:
#             print(j, end=' ')
#         print()

# def ispisati_red_matrice(matrica):
#     kojiRed = int(input('Koji red hocete da se ispise')) - 1
#     for i in matrica[kojiRed]: print(i, end = ' ')

# def ispisati_kolonu_matrice(matrica):
#     kojaKolona = int(input('Koju kolonu hocete')) - 1
#     for i in matrica:
#         print(i[kojaKolona], end=' ')

# lista = []
# matrica = []
# while True:
#     print(50*'=')
#     opcija = int(input('''Unesite opciju
#                         1 Ispis
#                         2 Obrnuti ispis
#                         3 Unos elemenata
#                         4 ispis parnih elemenata
#                         5 pravljenje matrice
#                         6 ispis matrice
#                         7 ispis reda matrice
#                         8 ispis kolone matrice
#                         0 Kraj'''))
#     if opcija == 1:
#         ispis_elemenata(lista)
#     elif opcija == 2:
#         obrnutiIspis(lista)
#     elif opcija == 3:
#         lista = unosListe()
#     elif opcija == 4:
#         ispisiParne(lista)
#     elif opcija == 5:
#         matrica = napraviti_matricu(matrica)
#     elif opcija == 6:
#         ispisati_matricu(matrica)
#     elif opcija == 7:
#         ispisati_red_matrice(matrica)
#     elif opcija == 8:
#         ispisati_kolonu_matrice(matrica)
#     elif opcija == 0:
#         break
#     else:
#         print('Pogresan unos, pokusaj ponovo')

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# def formatiranje_sadrzaja(path = 'C:\Users\Comp\Desktop\pythonNaila\Emsissions_copy.csv'):
#     f = open(path)
#     sadrzaj_string = f.read()
#     f.close()

#     lista_redova = sadrzaj_string.split('\n')

#     for i in range(len(lista_redova)):
#         lista_redova[i] = lista_redova[i].split(',')

#     sadrzaj_recnik = {}

#     for i in lista_redova:
#         if i[0] == 'CO2 per capita':
#             sadrzaj_recnik[i[0]] = [int(x) for x in i[1:]]
#         else:
#             sadrzaj_recnik[i[0]] = [float(x) for x in i[1:]]
#     print(sadrzaj_recnik)

#     return sadrzaj_recnik



# def min_vrednost_po_godini(godina,podaci):
#     if not godina in podaci['CO2 per capita']:
#         print('Nije godina u opsegu')
#         return
#     indeks = podaci['CO2 per capita'].index(godina)
#     lista_koeficijenata = []
#     for i,j in podaci.values():
#         if i == 'CO2 per capita':
#             continue
#         lista_koeficijenata.append(j[indeks])
#     return min(lista_koeficijenata)

# #max i avg i godina

# data = formatiranje_sadrzaja()
# min_koef = min_vrednost_po_godini(2000,data) 

# # # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# import matplotlib.pyplot as plt
# import numpy as np

# co2 = {}
# fi = open("D:\Predavanje SmartStart\python ucenje\Emissions_copy.csv", 'r')
# for i in fi:
#     line = i[:-1].split(',')
#     co2[line[0]] = [line[j] if line[0]=="CO2 per capita" else float(line[j]) for j in range(1, len(line))] # var1 if cond else var2 
# fi.close()
# while True:
#     opc = input("""Choose an option:\n
# - 0 List of states
# - 1 General Statistics
# - 2 Graph Visual
# - 3 Subset Management
# - 4 Exit\n
# Choice: """)
#     print("- "*20)

#     if opc == "1":
#         while True:
#             year = input('Enter a year 1997-2010: ')
#             if year in co2['CO2 per capita']:
#                 year_index = co2['CO2 per capita'].index(year)
#                 break
#             else:
#                 print('Enter a year in the range provided.')

#         coeficient = []
#         for i, j in co2.items():
#             if i == 'CO2 per capita':
#                 continue
#             coeficient.append(j[year_index])
#         print(f"""{"- "*20}\nGeneral statistics in {year}:
# {list(co2)[1:][coeficient.index(min(coeficient))]}: {min(coeficient)} # list[]
# {list(co2)[1:][coeficient.index(max(coeficient))]}: {max(coeficient)}
# Average: {sum(coeficient) / len(coeficient)}\n{"- "*20}""")
#     elif opc == "2":
#         kof = []
#         kofs = []
#         states_G = []
#         while True:
#             user_state = input("Enter a state the graph of which you want: ")
#             user_stateG = input("Enter more states (Empty to skip): ")
#             while user_stateG:
#                 user_stateG = input("Enter more states (Empty to skip): ")
#                 if user_stateG in co2.keys():
#                     states_G.append(user_stateG)
#                 else:
#                     print("State not in the list.")

#             if user_state and user_state in co2:
#                 kof = [x for x in co2[user_state]]
#             else:
#                 print("You must specify at least one state that is in the list.") 

#             if states_G:
#                 kof_matrix = []
#                 for i in states_G:
#                     kof_matrix.append([n for n in co2[i]])

#             if kof:
#                 break

#         god = [int(n) for n in co2["CO2 per capita"]]
#         plt.plot(god, kof)
#         plt.xlabel("Years")
#         plt.ylabel("Emissions")
#         plt.title(f"Emissions per year in {user_state}")
#         plt.legend([user_state])
#         if kofs:
#             for i in kofs:
#                 plt.plot(god, i)
#             plt.legend([user_state], [n for n in kof_matrix])
#         plt.show()
#     elif opc == "3":
#         clearing = input("""Do you wish to clear the file?\n       
# - Y Clear
# - N Continue\n        
# Choice: """)
#         if clearing == "y":
#             f = open("D:\Predavanje SmartStart\python ucenje\Emissions_subset", "r+")
#             f.truncate(0)
#             print(f"""{"- "*20}\nList sucessfully cleared.\n{"- "*20}""")
#         else:
#             print(f"""{"- "*20}\nClearing cancelled.\n{"- "*20}""")
            
#         f = open("Emissions_subset", "a")
#         subset = f
#         for i in [input(f"Enter the state {n+1}: ")  for n in range(3)]:
#             if i in co2.keys():
#                 subset.write(f"{i}: {co2[i]}\n")                          
#             else:
#                 print("Invalid input:")      
#         subset.write(" ")              
#         print(f"""{"- "*20}\nStates successfully added to Subset.\n{"- "*20}""")
#         subset.close()
#     elif opc == "4":
#         print("End.")
#         exit()
#     elif opc == "0":
#         for ime in co2.keys():
#             print(ime)
#         print(f"""{"- "*20}\nThose are the states in the list.\n{"- "*20}""")
#     else:
#         print(f"""Invalid input.\n{"- "*20}""")

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# from random import randint

# def hotel_cost(nights):
#     return 140 * nights

# def plane_ride_cost(city):
#     gradovi = {}
#     f = open(r"C:\Users\Comp\Desktop\pythonNaila\Emissions_copy(1).csv","r") #zbog \ on ga pise kao \\
#     for i in f:
#         gradovi[i.split(',')[0]] = randint(50,100) 
#     print(gradovi)
#     return gradovi[city]


# def rental_car_cost(days):
#     if days >= 7:
#         return 50
#     elif days >= 3:
#         return 20
#     else:
#         return 40*days

# def trip_cost(city,days,spending_money):
#     return rental_car_cost(days) + plane_ride_cost(city) + hotel_cost(days) + spending_money

# # print(trip_cost(input('Unesite koji grad'),int(input("Unesite koliko noci")),float(input("Unesite spending money"))))

# print(plane_ride_cost(input("Unesite drzavu")))

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

