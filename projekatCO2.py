#ispisi ga kao dictionary
f = open("C:/Users/Comp/Desktop/pythonNaila/Emissions_copy(1).csv", "r") #pokazivac na neki fajl
sadrzaj_string = f.read() #ceo sadrzaj ce biti jedan ceo string
sadrzaj = {}

sadrzaj_list = sadrzaj_string.split('\n')


for i in range(len(sadrzaj_list)):
    sadrzaj_list[i] = sadrzaj_list[i].split(',') #od listu redova jedan red koji je string 
                                        #stavljamo kao listu stringova podeljenog na zareze
#print(sadrzaj_list)

for i in sadrzaj_list: #i ce biti podlista kao jedan red
    sadrzaj[i[0]] = i[1:] #ovo ce biti nova lista

#print(sadrzaj)

# #uzima input od korisnika kao godinu 
# #i izbaci min,max i avg za tu godinu 
# while True : #unos godine sa tastature sve dok godina nije u zadatom opsegu
#     godina = input('Unesite koju godinu 1997-2010')
#     if godina in sadrzaj['CO2 per capita']: #kada bude u opsegu trazi se redni broj kolone u kojoj je ta godina
#                                             #za pristup podacima u toj godini
#         index_godine = sadrzaj['CO2 per capita'].index(godina) #izbacuje vrednost indeksa sa prvom vrednoscu godine
#         break
#     else:
#         print('Unesite godinu u opsegu!') 


# #iz stringova brojeva zagadjenja u same double brojeve

# max_drzava = 0
# max_drzava_key = ''
# min_drzava = 0
# min_drzava_key = ''
# avg_drzava = 0
# print(list(sadrzaj.keys())) #lista kljuceva
# for i,j in sadrzaj.items(): # i su drzave(kljucevi) j su liste sa zagadjenjima
#     j[index_godine] = float(j[index_godine]) #iz stringova brojeva zagadjenja u same double brojeve
#                                              #samo kod izabrane godine, stali se ne menjaju
#     if i == list(sadrzaj.keys())[0]: #kada je kljuc CO2 per capita(zaglavlje) ono se preskace jer su godine u pitanju
#         continue

#     if i == list(sadrzaj.keys())[1]: #prva drzava
#         max_drzava = j[index_godine] #defaultne vrednosti zagadjenja max i mina 
#         min_drzava = j[index_godine]
#         min_drzava_key = max_drzava_key = i #defaultna drzava je prva drzava

#     if max_drzava < j[index_godine]: # uslov za uvecanje max i max_godine
#         max_drzava = j[index_godine]
#         max_drzava = i

#     if min_drzava > j[index_godine]: #uslov za menjaje min i min_godine uz nju
#         min_drzava = j[index_godine]
#         max_drzava_key = i
    
#     avg_drzava += j[index_godine] #suma svih zagadjenja do kraja u toj godini

# print(min_drzava,min_drzava_key)

# print(max_drzava, max_drzava_key)

# print(avg_drzava / (len(sadrzaj) - 1) ) #duzina je koliko ima kljuceva(redova) - 1(zbog co2 per capita)

# #za domaci iskomentarisati ovo

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>






# # #matplotlib

# import matplotlib.pyplot as plt
# import numpy as np

# fig, ax = plt.subplots()

# ax.plot([1,2,3,4],[1,4,2,3])

# plt.show() #kao print za ostalo,ovako ga prikaze

#unos zemlje sa tastature, sa proverom

# while True:
#     drzava = input('Unesite naziv drzave:')
#     if drzava not in sadrzaj:
#         print('Wrong input!')
#         continue
#     koeficijenti = [float(x) for x in sadrzaj[drzava]]
#     godine = [int(x) for x in sadrzaj['CO2 per capita']]
#     break

import matplotlib.pyplot as plt #importamo objekat plota
import numpy as np #za racunanje

# plt.plot(godine,koeficijenti,color = "green",linewidth = 2, linestyle = "-") #vraca listu, uzimas prvu vrednost

# plt.grid(True)   za linije u plotu
#plt.xlabel("Year")
#plt.ylabel('Emissions in ' + drzava)

#plt.xticks(parneGodine) #zubci sa strane x-ose

# plt.yticks(zaokruzenaZagadjenost) #zubci sa strane y-ose

#plt.title("Year vs Emissions in Capita") #umesto ax.set_....  
#plt.show()

while True:
    drzave = input('Unesite nazive drzava: a,b')
    drzave = drzave.split(',')
    jedna = drzave[0]
    druga = drzave[1]
    if jedna not in sadrzaj or druga not in sadrzaj:
        print('Pogresan unos!')
        continue
    koef1 = [float(x) for x in sadrzaj[jedna]]
    koef2 = [float(x) for x in sadrzaj[druga]]
    godine = [int(x) for x in sadrzaj['CO2 per capita']]
    break

plt.plot(godine,koef1,color = "blue",label = jedna) #da bi znao za koju drzavu je u legendi

plt.plot(godine,koef2,color = "orange",label = druga) #isto

plt.legend()

plt.title("Year vs Emissions in Capita")

plt.xlabel("Years")

plt.ylabel("Emissions in ")

plt.show()