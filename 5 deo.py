# #TODO ovaj komentar mozes staviti za kasnije sta treba da se radi

# a = 'Hello world'
# #'H e l l o   w o r l d'
# # 0 1 2 3 4 5 6 7 8 9 10
# #               -4 -3 -2 -1


# if a == a[::-1]:
#     print('rec je palindrom')

# #a [pocetni_indeks: krajnji_indeks: korak]
# #Samo u slucaju kad je prazan string bice false 
# b = bool(a)
# #true


#domaci 
# #765 => 7 6 5
# broj = int(input('Unesite broj'))
# suma = 0
# for i in str(broj):
#     suma += int(i)

# print('Suma je: ', suma)

#preko f-je len za lenght duzinu 

# broj = '345'
# print(str(broj))

# print(len(str(broj))) #ispise 3
# suma = 0

# for i in range(len(str(broj))): # koliko ih ima ali od 1 broji, range(3) i = 0 1 2
#     suma = suma + int(str(broj)[i]) #pretvaras broj u string, to je niz pa od toga pod indeksom 

# #sve isti zadatak

# while broj > 0 :
#     cifra = broj % 10
# #     suma += cifra
# #     broj //= 10

# # print(suma)


# for i in range(7):
#     if i == 0 :
#         print(' ', '* '*3,' ')
#     elif i == 3:
#         print('* '*5)
#     else:
#         print('* ',' '*4, '* ')


# for i in range(7):
#     if i == 0 or i == 6:
#         print(' ',"* "*3,' ')
#     elif i == 2:
#         print("*")
#     elif i == 3:
#         print("*",' ','*'*3)
#     else :
# #         print('*', ' '*3,'*')


# prvi = int(input('Unesite prvi broj'))
# drugi = int(input('Unesite drugi broj'))

# suma = prvi + drugi 

# strsuma = str(suma)
# duzina = len(strsuma)
# if int(strsuma[duzina - 1]) > 5:
#     strsuma[ duzina - 2 ] = str((int(strsuma[duzina - 2]))+1)
# else :
    

# #moze i ovako 

# cifra = suma % 10

# if cifra >= 5:
#     suma = suma - cifra + 10
# else 
#     suma = suma - cifra

# # print(suma)

# mesec = int(input('Unesite mesec'))
# dan = int(input('Unesite dan'))

# broj = 
# if mesec == 1 and dan <= 31 or mesec == 2 and dan <= 28 or mesec == 3 and dan <= 31 or mesec == 4 and dan <= 30 or mesec == 5 and dan <=31 or mesec == 6 and dan <= 30 or mesec == 7 and dan <=31 or mesec == 8 and dan <= 31 or mesec == 9 and dan <=30 or mesec == 10 and dan <= 31 or mesec == 11 and dan <= 30 or mesec == 12 and dan <= 31:
#     if mesec == 1 or mesec == 2 or mesec == 3 and dan < 21:
#         print('zima')
#     elif mesec == 3 or mesec == 4 or  mesec == 5 or mesec == 6 and dan < 22:
#         print('prolece')
#     elif mesec == 6 or mesec == 7 or mesec == 8 or  mesec == 9 and dani < 23:
#         print('leto')
#     elif mesec == 9 or mesec == 10 or mesec == 11 or mesec == 12 and dan < 12:
#         print('jesen')
# else:
#     print('Niste uneli ispravan dan niti mesec')

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# 6. cas

# for i in broj:
# paran = 1

# for i in range (100,401):
#     for j in range(0,len(i)):
#         if int(str(i)[0]) % 2 == 0:
#               paran = 0
#     if paran:
#         print(i,',')

# #Svi brojevi od 1 do 50, ako je broj deljiv sa 3 ispisi Fizz na svaki broj koji se deljiv sa 5 ispisi buzz
# #ako je deljiv sa oba ispisi FizzBuzz

# # for i in range(1,51):
# #     if i%3 == 0:
# #         print('fizz')
# #     if i%5 == 0:
# #         print('buzz')

# # #Unesi sifru koja ima najmanje 2 cifre, bar 1 od ($#@), da ima minimum 6 i maksimum 16 karaktera

# sifra = input('Unesite sifru')
# brojCifara = 0
# brojSimbola = 0
# if len(sifra) >= 6 and len(sifra) <= 16:
#     for i in '123456789':
#         if i in sifra:
#             brojCifara += 1
#     for i in '$#@':
#         if i in sifra:
#             brojSimbola += 1

# if brojCifara > 2 and brojSimbola :
#     print('Uspesno kreirana sifra')
# else 
#     print('POnovo pokrenite program')

# # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# # 7. cas while petlja

# # for i in range(36):
# #     print('Hello world')

# # #uslov dok kojeg se izvrsava neki deo koda

# # a = 1

# # while a < 10:
# #     print(a)
# #     a += 1


# #Uneti input, ako je jednak sifri 

# password = '12345'
# sifra = '' 
# while sifra != password: 
#     unos = input('Unesite nesto')


# #funkcije iz biblioteke 
# from random import randint

# broj = randint(1,10)
# vrednost = int(input('Unesite neku vrednost, 0 za kraj'))
# while True:
#     if broj > vrednost:
#         print('Veci je')
#     elif broj < vrednost:
#         print('Manji je')
#     elif broj == vrednost:
#         print('YAAY')
#         break
#     vrednost = int(input('Unesite oper vrednost'))



# while True :
#     broj = int(input('Unesite broj'))
#     if broj > 10 and broj <= 20:
#         print('Cestitamo')
#         break
#     else:
#         print('POkusajte ponovo')


# #KAd imamo input prazan prekinuti unosenje vrednost
# #zbir prethodno unetih vrednosti 
# #srednju vrednost 

# suma = 0
# broj_b = 0
# while True:
#     broj = input('Unesite vrednost')
#     if broj != '' :
#         suma += int(broj)
#         broj_b += 1
#     else :
#         print(suma / broj)
#         break
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# #Nadji najveci broj koji je palindrom koji se dobija kada se pomnoze dva trocifrena broja
# #Postavljanje promenljive u koju cemo da cuvamo najveci, na nulu kao neutralnu vrednost
# maks = 0
# #U njoj cemo cuvati vrednost prvog broja koji mnozenjem sa drugim daje maksimum
# cifra1 = 0
# #Cuvamo vrednost drugog broja
# cifra2 = 0

# #Da ne bismo posmatrali ceo skup trazeci maksimum, krecemo od dela sa kraja, ako ne nadjemo, vracamo ka pocetku
# for polovina in range (9000,1000,-1000):
#     #Trazimo prvi broj
#     for i in range(polovina,polovina + 1001):
#         #drugi broj
#         for j in range(polovina,polovina+1001):
#             #Kad je drugi broj manji od prvog, njihov prozivod smo uracunali prethodnim vrednostima i-a 
#             if j < i:
#                 continue
#             #Proveravamo da li je broj kao string palindrom i ako je veci od prethnodne vrednosti maksa, on postaje maks
#             if str(i * j) == str(i * j)[::-1] and i * j > maks:
#                 maks = i*j
#                 cifra1 = i
#                 cifra2 = j
#     #Ako nadjemo u odredjenom delu sa kraja maks, prekidamo povecanje dela trazenja
#     if maks != 0:
#         break 
        

# print(maks,cifra1,cifra2)
 
# #float isto kao int sece nule do prve nenulte cifre

# if 55 == str(55):
#     print('Broj jeste palindrom')
# else:
#     print('Uvek ce biti ispunjen uslov, jer nisu jednaki')
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#ispisi tablicu mnozenja 

# #za ispis u istom redu
# for i in range(1,11):
#     for j in range(1,11):
#         print(i*j, end = '\t') #kad ispises idi u space
#     print()

##Postavljanje vrednosti na pocetnu cije cemo inkremente ispisati 
# broj = 1
##BROj redova
# for i in range(4):
## BRoj kolona
#     for j in range(i+1):
        ##Ispis sadrzaja, odvojeni tabom
#         print(broj, end='\t')
        ##Samo inkrementiranje
#         broj += 1
    #Novi red
#     print()

#za domaci za tablicu mnozenja i ovaj gore zadatak komentarisemo svaku liniju koda

# #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# #LISTEEEE
# a = 10
# mylist = ["apple","apple","banana","cherry", [23453, "banana"], True, 34.54, a]
# #            0        1        2       3      4     5
# #dozvoljava duplikate
# #promenljiva je
# print(mylist[0][3])
# print("apple"[3])

# print(mylist[1:])
# print(mylist[1:3])
# print(mylist[0:3])

# print(mylist[0:3:2])

# #dodavanje na poslednje mesto 
# mylist.append('Nova vrednost')

#python je interpreterski
#transpiler iz jedne verzije jezika u stariju

# mylist.insert(1, 'Nova vrednost') #Na indeksu 1 novu vrednost

# mylist.remove(True) #Prva vrednost sa Trueom se uklanja 

# mylist.pop(1) Sa indeksom 1 uklanja

# mylist.count('Apple') #Koliko puta se pojavljuje 

# for i in mylist: #I ce uzimati vrednost svake vrednosti liste
#     print(i)

# print(len(mylist) + 10)

# for i in range(len(mylist)):
#     print(mylist[i]) 


# niz = []
# #Nema 
# for i in range(10):
#     niz.append(int(input('Unesite vrednost')))

# for i in niz:
#     if i%2 == 0:
#         print(i)

# #Za domaci da iskomentarisemo sve

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# #Ne koristiti 
# #for i in list:
# i je lokalna promenljiva koja poprima vrednost elementa liste
#ne mozes direktno menjati element liste
# koristi 
#for i in range():
# #Pokazivaci su poazivaci u virtuelnu memoriju

# #domaci 

# niz = []
# brojac = 0
# for i in range(10):
#     niz.append(brojac)
#     brojac += 4

# niz.reverse()

# print(niz)



# niz = [] #Ima nula elementa cija je duzina 0 pa ne postoji niz[0]
# suma = 0
# for i in range(0,10):
#     niz.append(int(input('Unesite element')))
#     suma += niz[i]

# print(suma)
#print(sum(niz))

#prviNiz = []

# drugiNiz = []

# for i in range(10):
#     prviNiz.append(int(input('Unesite element niza')))
#     drugiNiz.append(prviNiz[i]**2)

# print(prviNiz)
# print(drugiNiz)

# prviNiz = [1,2,3,4,5,6,7,8,9,10]
# maks = prviNiz[0]
# mini = prviNiz[0]

# for i in range(len(prviNiz)): #Moze i for i in lst: i > max ? max = i elif i < min ? min = i
#     if(prviNiz[i] > maks):
#         maks = prviNiz[i]
#     elif(prviNiz[i] < min):
#         mini = prviNiz[i]

# print(maks,mini)

# print(30*'=') #=====================================

# lista = ['abc','xyz','aba','1221']
# brojac = 0
# for i in lista:
#     if len(i) >= 2 and i[0] == i[-1] and i == str(i):
#         brojac += 1

# print(brojac)

# #kod stringa ne moze reverse jer je string prost tip podataka kontantan, lista je struktura kojom moze da se manipulise


# #kad napises i u for zaglavlju, ona ce da vazi i van nje zbog C-a

# # za domaci ova lista, da se uklone duplikati

# lst = ['Red', 'Green', 'Pink', 'White', ' Black', 'Green', ' Green', 'Pink', 'Yellow']
# prazna = []

# for i in lst:
#         if lst.count(lst[i]) > 1:
#                 lst.remove(i)
# print(lst)
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

#Setovi ne dozvoljavaju duplikate

#lst = list(set(lst))

# prvaL = ['Red', 'Green', 'Pink', 'White', ' Black', 'Green', ' Green', 'Pink', 'Yellow']

# drugaL = ['Green', False, True, 23, 34.3443, 'Hello']

# zajEle = False
# for i in prvaL:
# 	if i in drugaL:
# 		zajEle = True
# 		break

# if zajEle:
# 	print('Postoje zajednicki elementi')
# else:
# 	print('Ne postoje zajednicki elementi')


# kvadrati = []

# for i in range(1,31):
# 	if i < 6 or i > 25:
# 		kvadrati.append(i**2)

# print(kvadrati)

# prvaL = ['Red', 'Green', 'Pink', 'White', 'Black', 'Green', 'Green', 'Pink', 'Yellow']

# drugaL = ['Green', False, True, 23, 34.3443, 'Hello']

# for i in prvaL:
# 	if i not in drugaL:
# 		print(i)

# lista = []

# from random import randint


# for i in range(1,10):
# 	lista.append(randint(-50,50))

# lista.sort()
 
# print(lista)

# print(lista[1], lista[-2])

# n = int(input('Unesite n'))

# lista = ['p','q','r']
# nova = []

# for broj in range(1,n+1):
#         for c in lista:
#                 nova.append(c + str(broj))

# print(nova)

# lista = [0,1,2,3,4,5]

# #Da bismo izvrsili provere unosa
# prviIndeks = -1
# drugiIndeks = -2

# while prviIndeks < 0 or  prviIndeks > 5:
#     prviIndeks = int(input('Unesite indeks onoga koga hocete da menjate')) - 1

# while drugiIndeks < 0 or drugiIndeks > 5: 
#     drugiIndeks = int(input('Unesite drugi indeks')) - 1

# temp = lista[prviIndeks]
# lista[prviIndeks] = lista[drugiIndeks]
# lista[drugiIndeks] = temp
# # Moze i ovako

# lista[prviIndeks], lista[drugiIndeks] = lista[drugiIndeks], lista[prviIndeks]

# print(lista) 

# a  = 10

# b = 12

# a, b = b, a

# stri = input('Unesite strint')
# # for i in input('Unesite strint'):
# # 	lista.append(i)
# stri=list(stri)
# print(stri)

# prva = [1,3,5,7,9]

# druga = [2,4,6,8]

# prva.pop(-1)
# prva.extend(druga)

# # for i in druga:
# # 	prva.append(i)
# # prva = prva + druga

# # print(prva)
# # # Dodati na kraj
# # lst.insert(len(lst), 'Nova vrednost')
# # lst.pop() #Bez navodnika uklanja poslednji element

# lst = ['Red', 'Green', 'Pink', 'White', 'Black', 'Pink', ' Yellow']

# indeks  = lst.index('Pink')

# # for i in range(indeks + 1,len(lst)):
# # 	if lst[i] == 'Pink':
# # 		lst.pop(i)
# # 		break

# lst[indeks + 1:].remove('Pink')
# print(lst)


# # domaci 

# lista = [3,4,0,0,0,6,2,0,6,7,6,0,0,0,9,10,7,4,4,5,3,0,0,2,9,7,1]

# for i in lista:
# 	if i == 0:
# 		lista.remove(i)
# 		lista.append(i)



# lista.sort()
# lista.reverse()
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# a = ['Hello', False, 645]
# lst = [223, 'Pink', a, [4, 5, 6,[7, 8, 9]], True, 'White', 453.23]

# print(lst[2][0])


# l1 = [1,2,3]
# l2 = [4,5,6]
# l3 = [7,8,9]
# l4 = [10,11,12]

# glavna = [l1,l2,l3,l4]

# print(glavna)


# maks = 0
# l = [] #koja je lista
# for i in glavna: #i postaje manja lista
# 	if sum(i) > maks:
# 		maks = sum(i)
# 		l = i

# print(maks, l)


# lista = []

# element = '1'
# while element != '0':
# 	element = input('Unesite string, 0 za kraj')
# 	if element == '0':
# 		break
# 	lista.append(element)

# abeceda = []
# slovo = '1'
# while slovo != '0':
# 	slovo = input('Unesite slovo, 0 za kraj')
# 	if slovo == '0':
# 		break
# 	abeceda.append(slovo)

# listaSlovo = []

# for i in lista:
# 	for j in abeceda:
# 		if i[0] == j:
# 			listaSlovo.append(i) 
# 			print(j)
# 	print(listaSlovo)
# 	listaSlovo = []
	

# lista = [0, 10, [20,30],40,50,[60,70,80],[90,100,110,120]]

# nova = []
# for i in lista:
# 	if type(i) is list:
# 	#	for j in i:
# 	#		nova.append(j)
# 		nova.extend(i) #produzi listu za elemente druge liste
# 	else:
# 		nova.append(i)

# print(nova)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# lista = [ 1, 2, 3, 4, 5, 6, 7, 8, 9]
# konacna = []

# for i in lista:
# 	for j in lista:
# 		if i == j:
# 			continue
# 		nova = []
# 		nova.append(i)
# 		nova.append(j)
# 		konacna.append(nova)


# print(konacna)

# matrica = []
# for i in range(3):
# 	niz = []
# 	for j in range(1,4):
# 		niz.append(j)
# 	matrica.append(niz)


# print(matrica)

# for i in range(len(matrica)):
# 	for j in range(len(matrica[i])):
# 		print(matrica[i][j], end = '\t')
# 	print()


#domaci

# matrica = [[1,2,3], [6,7,8],[2,5,8]]

# # for i in matrica:
# # 	print(f'Suma reda {i} je {sum(i)}')

# sumaKolona = []
# for i in range(len(matrica)):
#  	suma = 0
#  	for j in range(len(matrica[i])):
#  		suma += matrica[j][i]
# 	sumaKolona.append(suma)
#  	print(f'Suma {i+1} kolone je {suma}')

# print(sumaKolona)

# for kolona in range(3):
# 	for niz in matrica:



# prva = [[0],[1],[2],[1,2,3], [2,3,4]]
# druga = [[4,5,6]]

# matrica = prva + druga

# print(matrica)


# for i in range(4):
# 	for j in range(4):
# 		print(f'{i}{j}', end = ' ')
# 	print()

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# #Izracunati sumu i prikazati glavnu dijagonalu matrice 

# matrica = [[1,2,3], [6,7,8],[2,5,8]]

# # suma = 0
# # for i in range(len(matrica)):
# # 	for j in range(len(matrica[i])):
# # 		if i == j:
# # 			suma += matrica[i][j]
# # 			print(matrica[i][j], end = " ")
# # 		else:
# # 			print(" ", end = " ")
# # 	print()

# # print(suma)

# suma = 0
# for i in range(len(matrica)):
# 	j = len(matrica[i]) - 1 - i
# 	print(" " * j, matrica[i][j])
# 	suma += matrica[i][j] 
# 	#mozes i drugu petlju i uslov j+i = len(matrica) - 1

# print("Suma je", suma)

# 00 01 02
# 10 11 12
# 20 21 22

# lst = ['H','e','l','l','o',' ','w','o','r','l','d']

# helloWorld = '' #Jer pravis string

# for i in lst:
# 	helloWorld += i

# print(helloWorld)

# #napisati python program koji stavlja u podlistu susedne elemente

# lista = [0,0,1,2,3,4,4,5,6,6,6,7,8,9,4,4]
# nova = []

# #probaj samo sa for i in range, tjt

# print(lista)
# privremeniStorage = []
# privremeniStorage.append(lista[0])
# lista.remove(lista[0])
# for i in lista:
# 	if i in privremeniStorage:
# 		privremeniStorage.append(i)
# 	else: #Kad naidje na ne susede, odradi posao
# 		nova.append(privremeniStorage)
# 		privremeniStorage = []
# 		privremeniStorage.append(i) #dodaj suseda

# if len(privremeniStorage) > 1: #Ne zavrsava se lista sa jednim nego sa susedima
# 	nova.append(privremeniStorage)
# print(nova)

# njegovo resenje 



	# if i in susedni:
	# 	susedni.append(i)
	# 	print(susedni)
	# else:
	# 	if susedni != [] and len(susedni) > 1:
	# 		nova.append(susedni)
	# 	print(susedni)
	# 	susedni = []
	# 	susedni.append(i)
	# 	nova.append(i)

# print(nova)


# domaci da se liste u njoj sortiraju po duzini 

# lst1 = [[1,3,4,8],[5,7],[9,11,4,6,2],[13,15,17],[0]]

# # #moj nacin

# print(lst1)
# duzine = []

# for i in lst1:
# 	duzine.append(len(i))

# print(duzine)

# sortiraneDuzine = sorted(duzine)
# print(sortiraneDuzine)
# sortiranaLista = []
# for i in sortiraneDuzine:
# 	sortiranaLista.append(lst1[duzine.index(i)])

# print(sortiranaLista)

# #Isto samo drugacije

# lst1.sort(key=len)

# #Isto drugacije 

# for i in range(len(lst1)):
# 	mini = len(lst1[i])
# 	for j in range(i, len(lst1)): #i je ovde indeks
# 		if len(lst1[i]) < mini:
# 			mini = lst1[j]
# 			el = lst1.pop(j)
# 			lst1.insert(i, el)

# print(lst1.sort) 

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# #Imamo dve liste, saberemo prvu i prvu,drugu i drugu, trecu i trecu

# lst1 = [[1,3],[5,7],[9,11]]
# lst2 = [[2,4],[6,8],[10,12,14]]
# konacna = []
# for i in range(len(lst1)):
# 	konacna.append(sorted(lst1[i] + lst2[i]))

# print(konacna)

# #domaci 

# prva = [1,1,3,4,4,5,6,7]
# druga = [0,1,2,3,4,4,5,7,8]

# suma = 0


# for i in prva+druga:
# 	suma += i

# print("prosek je", suma/ len(prva+druga))

# #domaci 

# lista = [1,'abcd',3,1.2,4,'xyz',5,'pqr',7,-5,-12.22]

# brojIntova = 0

# for i in lista:
# 	if type(i) == int:
# 		brojIntova += 1

# print(brojIntova)

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# #izbrisi odredjenu kolonu

# kolona = int(input("Unesite koja kolona")) -1 #Brojanje pocinje od nule

# matrica = [[1,2,3],[-2,4,-5],[1,-1,1]]

# for i in matrica:
# 	i.pop(kolona)

# print(matrica)

# #Hocemo li levo ili desno i koliko cemo da rotiramo 

# lista = [1,2,3,4,5,6,7,8,9,10]

# dire = input('Unesite pravac')
# koliko = int(input("Unesite koliko pozicija"))
# if dire == 'l':
# 	for i in range(koliko):
# 		el1 = lst.pop(i)
# 		lista.append(el1)
# elif dire == 'r' :
# 	for i in range(koliko): #ovoliko puta
# 		el1 = lista.pop(-1) #sa kraja
# 		lista.insert(0,el1) #na pocetak

# print(lista)

# lista = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]

# matrica = [[12,18,23,25,45],[7,11,19,24,28],[1,5,8,18,15,16]]


# for i in matrica:
# 	newList = []
# 	for j in i:
# 		if j in lista:
# 			newList.append(j)
# 	i.clear() # po referenci
# 	i.extend(newList) #po referenci

# print(matrica)
	
# lista = [[12,23,25,18,45],[7,12,18,24,28],[1,5,8,12,15,16,18]]

# zajednicki = []
# #Posmatramo elemente prve liste, ako oni postoje u sve tri to je to
# for izPrve in lista[0]:
# 	flag = True
# 	# Ako elementa nema u ostalim listama, cuvamo u memoriji da ga nema
# 	for j in lista: #svaka lista iz matrice
# 		if izPrve not in j:
# 			flag = False
# 	#ako elementa prve liste ima u ostalim listama, dodaj u listu zajednickih
# 	if flag == True:
# 		zajednicki.append(izPrve)

# print(zajednicki)

# #za domaci detaljno da se ispise sta se desavalo

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>.

# lista = ['Red color','Orange#','Green','Orange @','White']

# karakteri = ['#','@','color']


# # for i in range(len(lista)):
# # 	for j in range(len(lista[i])):
# # 		if lista[i][j] in karakteri:
# # 			lista[i] = lista[i][:j]
# # 			break
# # #			lista[i].replace(lista[i][j],'')
# # #			izbaceni.join(lista[i][j])
# # 		elif lista[i][j] == ' ':
# # 			lista[i] = lista[i][:j]
# # 			break

# # print(lista)

# for i in range(karakteri): #Za svaki karakter da l se nalazi u svim stringovima
# 	for j in range(len(lista)):
# 		if karakteri[i] in lista[j]:
# 			lista[j] = lista[j].replace(karakteri[i],'') #zameni vrednost karaktera u stringu sa ''
# 			lista[j] = lista[j].strip() #Ako ima nekih nepotrebnih spaceova

# print(lista)




# listaKaraktera = ['4','12','45','7','0','100','200','-12','-500']

# for i in range(len(listaKaraktera)):
# 	listaKaraktera[i] = int(listaKaraktera[i])

# #moze i ovako 
# listaKaraktera = [ int(x) for i in listaKaraktera]

# listaKaraktera.sort()

# print(listaKaraktera)


# lista = [10,20,4,-5,'b',70,'a']

# suma = 0

# for i in lista:
# 	if type(i) == int:
# 		i = str(abs(i)) #ako su neagitvni
# 		for j in i:
# 			suma += int(j)

# print(suma)




# prva = [2,4,7,0,5,8]
								 
# druga = [3,3,-1,7]

# # sabirci = []
# # minDuzina = min(len(prva),len(druga))

# # vecaDuzina = max(len(prva),len(druga))

# # for i in range(minDuzina):
# # 	sabirci.append(prva[i] + druga[i])

# # for i in range(minDuzina,vecaDuzina):
# # 	if len(prva) == vecaDuzina:
# # 		sabirci.append(prva[i])
# # 	else:
# # 		sabirci.append(druga[i])

# # print(sabirci)

# #Moze ovako

# for i in range(len(druga)):
# 	prva[i] = prva[i] + druga[i]

# print(prva)


# # # sa desne strane saberi dve liste

# for i in range(1,len(druga)): #dont know why + 1
# 	prva[-i] = prva[-i] + druga[-i]

# print(prva)

# # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# #Tuples su nepromenljivi i redosled/indeks

# #Liste i Tuplesi dozvoljavaju duplikate

# #PRetvaras u Tuples kad ti treba da nesto ne pormenis i ne zeznes 

# #Pretvaras u listu da promenis pa pretvoris u tuples da ostane nepromenjeno

# Tuple = ("Apple","Banana","cherry")

# print(Tuple)

# for i in Tuple:
# 	print(i)

# for i in range(len(Tuple)):
# 	print(Tuple[i])

# y = list(Tuple)

# y[1] = "kiwi"

# x = tuple(y)

# #ako hoces da izbrises koristi del

# fruit = ("Apple","Banana","Cherry")

# (green, yellow, red) = fruits

# print(green)

# print(yellow)

# print(red)

# fruits = ("apple","mango","papaya","pineapple","cherry")

# (green, *tropic, red) = fruits

# print(tropic) #Bice lista od 3 elementa

# #MOze konkatenacije

# fruits = (((((((("apple")))))))) #Bice string

# fruits = ("apple",) #da stavimo da je prvi element 

# fruits = tuple() 
# #isto je sa
# fruits = ()

# tpl = ()
# tpl = list(tpl)

# for i in range(5):
# 	tpl.append(input('Unesite el: '))

# print(tuple(tpl))

# tpl.reverse

# print(tuple(tpl))

# tpl = tuple(tpl)

# MOze del i na liste

# a = [1,2,3]

# del a

# print(a)


# #Zameni poslednju vrednost iz tupleova liste

# lista = [(10,20,30),(40,50,60),(70,80,90)]


# for i in range(len(lista)):
# 	lista[i] = list(lista[i])
# 	lista[i][-1] = 100
# 	lista[i] = tuple(lista[i])

#Olaksica
# for i in range(len(lista)):
	# lista[i] = lista[i][:-1] + (100,) #bez poslednjeg elementa


# print(lista)






# #uklinu prazne tuplove iz liste

# lista = [(),(),('',),('a','b'),('a','b','c'),('d',)]
# nova = []

# for i in range(lista.count(())):
# 	lista.remove(())
# print(lista)




# string = input("Unesite nesto")

# string = tuple(string)

# print(string)

# print(tuple(input("Unesite nesto")))



# tuples = ((10,10,10,12),(30,45,56,45),(81,80,39,32),(1,2,3,4))

# lista = []
# for i in tuples:
# 	lista.append(sum(i)/len(i))

# print(lista)


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

#SETOVI

#{}

#ne podrzavaju duplikate


#  myset = {"apple","banana","cherry","banana"}

# # print(myset)

# #nema indeksiranja

# #nemaju redosled, non stop se menja raspored

# #nepromenljivi su, ali mozes dodavati element

# #mozes for petljom proci kroz elemente

# for x in myset:
# 	print(x) #svaki put razlicit raspored

# if "babana" in myset: 
# 	print("banana")


# myset.add("nesto")

# myset.clear() #brise sve elemente


# x = {"apple","banana","cherry"}

# y = {"google","microsoft","apple"}

# z = x.difference(y) #elementi koji se nalaze u x a ne u y

# x.difference_update(y) #u x su ostali elemnti koji ne postoje u y

# myset.discard() #das mu koju vrednost da ukloni

# z = x.intersection(y) # zajednicki i za jednu i za drugu

# x.intersection_update(y) #ostavlja u prvoj presek sa drugom

# x = {"apple","banana","cherry"}

# y = {"apple","banana"}

# print(y.issubset(x)) #da li se y sadrzi ceo u x

# #pop() funkcija uklanja random element

# x = {"apple","banana","cherry"}

# y = {"google","microsoft","apple"}

# z = symmetric_difference(x,y) #spoljasnji join 

# mojset = set() #samo ovako moze
# for i in range(5):
# 	mojset.add(int(input("Unesite element:"))) #dodavanje elemenata u set

# print(min(mojset),max(mojset)) #mora u listu

# #moze i ovako

# minn = maxx = None #vrednost none je nista
# mojset = list(mojset) #po svojoj logici promenio je polozaj elemenata i stavio u listu

# for i in range(len(mojset)):
# 	if i == 0:
# 		minn = maxx = mojset[i]
# 	if mojset[i] > maxx:
# 		maxx = mojset[i]
# 	if mojset[i] < minn:
# 		minn = mojset[i]








# # udruzi dva seta

# set1 = {10,20,30,40,50}

# set2 = {30,40,50,60,70}

# set3 = set(list(set1) + list(set2))

# # a moze i ovako

# set3 = set1.union(set2)

# print(set3)

# set1.difference_update({10,20,30})

# print(set1)

# set1.symmetric_difference_update(set2) #u set1 pretvara u spoljasnji join set2 i set1 
# print(set1)




# set1 = {65,42,78,83,23,57,29}

# set2 = {67,73,43,48,83,57,29}
# # uklanja zajednicke

# set1.difference_update(set1.intersection(set2))

# print(set1)




# set1 = {27,43,34}

# set2 = {34,93,22,27,43,53,48}

# print(set1)

# print(set2)

# print('Prvi set je subset drugog', set1.issubset(set2))
# print('Drugi set je subset prvog', set2.issubset(set1))

# print('PRvi set je superset drugog', set1.issuperset(set2))
# print('Drugi set je superset drugog', set2.issuperset(s1))

# set1.clear()

# print('Prvi set', set1)
# print('Drugi set', set2)



# #ovako sam ja uradila
# prviNadDrugim = False

# drugiNadPrvim = False

# if set1.issubset(set2) : #podskup
# 	set1.clear()
# 	prviNadDrugim = True	
# 	print("Prvi set = ", set1)
# elif set2.issubset(set1) :
# 	set2.clear()
# 	drugiNadPrvim = True
# 	print("Drugi set = ", set2)

# print("prviNadDrugiim = ",prviNadDrugiim, "drugiNadPrvim = ", drugiNadPrvim)

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# definicija je kakvog ce oblika da bude 

# deklaracija koje ce vrednosti biti


#Dictionaries ili recnici

#ima indeksiranje


# lista  = ['Green',False,True,23,34.3443, 'Hello']

# thisdict = {
# 	"brand" : "Ford", #jedan item,element, moze biti i lista
# 	"model" : "Mustang", #kljuc je model (kao indeks), Mustang je vrednost
# 	"year" : 1964
# }

# print(lista[0])

# print(thisdict['brand'])

# print(thisdict.keys()) #dobije se lista kljuceva

# print(thisdict.values()) #dobije se lista vrednosti

# print(thisdict.items()) #lista tuplova sa kljucevima i svojim vrednostima


# for i in thisdict.keys():
# 	if i == "brand":
# 		print("Recnik ima brend")
# 	print(thisdict) #ispisuje kljuceve
# 	print(thisdict[i]) #ispisuje vrednosti


# var1 = ('Hello',45)
# a, b = var1[0], var1[1]

# #moze i ovako

# a, b = ('Hello', 45)


# for k,v in thisdict.items():
# 	print(k,v)

# for i in thisdict:
# 	print("prolazimo kroz listu kljuceva")

# thisdict['model'] = 'audi'

# #kljucevi moraju da budu unique

# #ako imamo dva ista kljuca gleda ce se poslednji 

# # thisdict = {
# # 	"brand" : "Ford", #jedan item,element, moze biti i lista
# # 	"model" : "Mustang", #kljuc je model (kao indeks), Mustang je vrednost
# # 	"year" : 1964,
# # 	"model" : "Novi Model"
# # }

# thisdict.update({
# 	"year": 2020
# 	}) #dodali smo jos jedan ceo element,recnik i onda ce ovo da se override-a

# print(thisdict)

# thisdict['novkljuc'] = 'nov model' #ako kljuc ne postoji dodace ga i sa svojom vrednoscu

# thisdict.pop("kljuc") #uklanja element pod ovim kljucem 

# del thisdict #izbrise ceo recnik 

# del thisdict["kljuc"] #pod kljucem

# myfamily = {
# 	"child1" : { 
# 		"name" : "Emil",
# 		"year" : 2004
# 	},
	
# 	"child2" : {
		
# 		"name" : "Emil",
# 		"year" : 2004
# 	},

# 	"child3" : {
# 		"name" : "Emil",
# 		"year" : 2004}
# }

# thisdict.clear() #isprazni recnik,ostavlja varijablu

# print(myfamily["child3"]['name'])

# sampleDict = {
# 	"class" : {
# 		"student" : {
# 			"name" : "Mike",
# 			"marks" : {
# 				"physics" : 70,
# 				"history" : 80
# 			}
# 		}
# 	}
# }

# print(sampleDict["class"]["student"]["marks"]["history"])

# employees = ['Kelly','Emma','John']

# defaults = {'designation' : 'Application Ddeveloper','salary' : 8000}


# newEmp = {}

# for i in range(len(employees)):
# 	newEmp[employees[i]] = dict(defaults)  #da bismo pravili novi recnik svaki put 
# 											#kreira se novi objekat sa vrednoscu od defaultsa posto je sve objekat

# print(newEmp)

# newEmp['Kelly']['salary'] = 123456789








# #domaci promeniti ime kljuca

# dictt = { "name" : "Kelly", "age" : 25, "salary" : 8000, "city" : "New york"}

# dictt["location"] = dictt.pop("city") #uklanja i kljuc

# print(dictt)

# #dobiti kljuc najmanje vrednosti u recniku 

# dictt = {
# 	'Physics' : 82,
# 	'Math' : 65,
# 	"history" : 75}


# minn = ('Physics', 82)

# for i,j in dictt.items():
# 	if j < minn[1]:
# 		minn = (i,j)

# print(minn[0]) #moze indeksiranje kod tuplova

# print(minn[1]) 



#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

#for i in range(len(trazeni := min(dictt.items()))) #kad hoces da koristis return value od = onda koristi :=



#print(trazeni := 5) moze ovako da ispise 5 nevezano za zadatak


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# fruits = ("apple","banana","cherry","strawberry","raspberry")

# (green,yellow,*p,nesto) = fruits # nesto = "raspberry"


# #promeni Bradov salary 

# sampleDict = {
#      'emp1': {'name': 'Jhon', 'salary': 7500},
#      'emp2': {'name': 'Emma', 'salary': 8000},
#      'emp3': {'name': 'Brad', 'salary': 6500}
# }

# for i in sampleDict.values():
# 	if i['name'] == "Brad":
# 		i['salary'] = 8500

# print(sampleDict)



# FirstList = [2, 3, 4, 5, 6, 7, 8]
# SecondList = [4, 9, 16, 25, 36, 49, 64]



# sett = set()

# for i in range(len(FirstList)):
# 	sett.add((FirstList[i] , SecondList[i])) #setovi dodamo par tuplova

# print(sett)




# speed = {'jan':47, 
# 		 'feb':52, 
# 		 'march':47, 
# 		 'April':44, 
# 		 'May':52, 
# 		 'June':53, 
# 		 'july':54, 
# 		 'Aug':44, 
# 		 'Sept':54}

# print(list(set(speed.values())))


# rollNumber = [47, 64, 69, 37, 76, 83, 95, 97]

# sampleDict ={'Jhon':47, 'Emma':69, 'Kelly':76, 'Jason':97}

# # rollNumber = set(rollNumber)

# dictValues = set(sampleDict.values())

# rollNumber = list(set(rollNumber).intersection(set(sampleDict.values()))) #kad ti zatreba

# print(rollNumber)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


# for i in range(5):
# 	print(i)

# print(i) #i vazi i ovde

#iz liste u dictionary 

# lista =[[1,'Jean Castro','v'],[2,'Lula Powell','V'],[3, 'Brian Howell', 'VI'], [4, 'Lynne Foster','VI'],[5,'Zachary Simon','VII']]

# rezultat = {}

# for i in lista:
# 	rezItem = {}
# 	rezItem['name'] = i[1]
# 	rezItem['year'] = i[2]
# 	rezultat[i[0]] = rezItem

# print(rezultat)


# #Duzinu svih stringova

# recnik = {'#FF0000' : 'Red',
# 		  "#800000" : 'Maroon',
# 		  "#FFFF00" : 'Yellow',
# 		  '#808000' : 'Olive'}

# duzina = 0


# for i,j in recnik.items():
# 	if type(i) == str: #za slucaj da neki nije string da ne pukne program
# 		duzina += len(i) 
# 	if type(j) == str:
# 		duzina += len(j)

# # for i in recnik:
# # 	duzina += len(recnik[i]) + len(i)

# print(duzina)




# # Imamo tri maloprodaje Market Trafika Apoteka 
# #U svakoj maloprodaji imamo artikle
# #imamo meni u Consoli idemo redom 
# #Kreiramo tri maloprodaje 
# #Kad unesemo ispravnu sifru i korisnicko ime mi cemo kreirati malorpodaju iz naziva,tipa artikla i kolicina



# artikli = {}

# maloprodaje = { 'market' : {'brArtikala ' : 0}, 'trafika' : {'brArtikala' : 0}, 'apoteka' : {'brArtikala' : 0}}

# korisnici = { 'Petar' : {'sifra':'02145', 'tip' : 'vlasnik'},
# 			  'Marko' : {'sifra': '04879','tip' : 'prodavac'},
# 			  'Janko' : {'sifra': '78456', 'tip' : 'prodavac'}}

# #vlasnika koji dodaje i uklanja prodavce kreira artikal da menja sve
# #prodavac koji dodaje artikle


# while True :
# 	print("Dobrodosli u meni")
# 	print(">>>>>>>>>>>>>>")
# 	ime = input('Unesite ime')
# 	sifra = input('Unesite sifru')
# 	if ime in korisnici.keys() and korisnici[ime]['sifra'] == sifra:
# 		korisnik = korisnici[ime] #koristi ceo dictionary sa imenom
# 		if korisnik['tip'] == 'vlasnik':
# 			dodajUkloni = int(input("Unesite 1 za dodavanje, 0 za uklanjanje"))
# 			kojiMarket = input('Koji market zelite')
# 			if dodajUkloni == 1:

# 				dodajArtikal = {}
# 				dodajArtikal['naziv'] = input('Unesite naziv')
# 				dodajArtikal['tip'] = input("Unesite tip")
# 				dodajArtikal['adresa'] = input("Unesite adresu")
# 				maloprodaje[str(kojiMarket)]['brArtikala'] += 1
				


# 			else:
# 				ukloniArtikal = input("Koji artiakl zelite da uklonite") 

# lista = [[1,2],3,4,5,6,7,8,9,10]

# nova = []
# for i in lista:
# 	#dodajes ob,jekat ali zadrzavas referencu na njega x = 3 lista1 = [x,4] lista2 = [x,5] i kad primenis funkciju ona vazi za sve
# 	nova.append(i)
# 	i.clear()
# 	break
# 	#i jeste pokazivac na element liste i mozes funkcijama da radis sa njim sta god hoces
# 	i.remove(1) 
# 	break
# 	#medjutim, operatorom = kad stavis na i kreira se novi objekat i brise se referenca na clana niza
# 	i = 5

# print(nova)

# nesto = [1,2,3]

# for i in nesto:
# 	i = i + 1 #assignment operator kreira nove objekte sa vrednostima *i + 1

# print(nesto)
	

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# dictionary = {'Cierra Vega' : 175,
# 			  'Alden Cantrell' : 180, 
# 			  'Kierra Gentry' : 165, 
# 			  'Pierre Cox' : 190
# 			}


# min = 170
# for i,j in dict(dictionary).items(): #kroz ovaj novokomponovani prolazi, iz pravog uklanja
# 	if j < 170:
# 		dictionary.pop(i)
		

# print(dictionary)



# dictt = {'Science' : [88,89,62,95], 'Language' : [77,78,84,80]}

# listaDicta = []
# for i in range(len(dictt['Science'])): #0 1 2 3
# 	manjiDict = {} #Science 
# 	for j in dictt.keys(): #'Science', 'Language'
# 		manjiDict[j] = dictt[j][i]
# 	listaDicta.append(manjiDict)

# print(listaDicta)


# lista = [11,45,8,11,23,45,23,45,89]

# res = {}

# for i in lista:
# 	if i not in res.keys():
# 		res[i] = lista.count(i)

# print(res)

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# rollNumber = [47,64,69,37,76,83,95,97]

# sampleDict = {'Jhon' : 47, 'Emma': 69, 'Kelly' : 76, 'Jason' : 97}

# brojevi = list(rollNumber)

# for i in rollNumber:
# 	if i not in sampleDict.values():
# 		brojevi.remove(i)

# rollNumber = brojevi

# print(rollNumber)


# #moze i ovako

# print(list(set(rollNumber).intersection(set(sampleDict.values))))


# prvi = 1
# drugi = 2
# #print(prvi)
# #print(drugi)

# suma = drugi
# while prvi + drugi < 4_000_000:
# 	prvi = prvi + drugi
# #	print(prvi)
# 	drugi = prvi + drugi
# #	print(drugi)
# 	if prvi % 2 == 0:
# 		suma += prvi
# 	if drugi % 2 == 0:
# 		suma += drugi

# print(suma)  

# #moze i ovako

# fib = [1,2]
# el1 = 1
# el2 = 2
# while True:
# 	pom = el1 
# 	el1 = el2
# 	el2 = pom + el2
# 	if el2 < 4_000_000:
# 		fib.append(el2)
# 	else:
# 		break

# suma = 0
# for i in fib:
# 	if i % 2 == 0:
# 		suma += i

# print(suma)






# sumaKvadrata = 0
# kvadratSume = 0
# for i in range(1,101):
# 	sumaKvadrata += i**2
# 	kvadratSume += i

# print(kvadratSume**2 - sumaKvadrata)

# import math

# for i in range(1,1000):
# 	for j in range(i,1000):
# 		if round(math.sqrt(i**2 + j**1)) > j:
# 			c = round(math.sqrt(i**2 + j**2))
# 			if i + j + c == 1_000:
# 				print(i*j*c)



# lista = []
# for i in range(1,1000): #jer ne moze 1000 + 0 + 0
# 	 lista.append(i)

# #print(lista)

# for i in lista:
# 	for j in lista[i::]:
# 		if math.sqrt(i**2 + j**2) in lista[j::]: #zasto en radi kad stavim int(math.....)?   zato sto int ce cepit decimale
# 			c = int(math.sqrt(i**2 + j**2)) #da l ovo ovde da stavim jer ce ga cepit po decimalama
# 			if i + j + c == 1_000:
# 				print(i*j*c)


# a = 5.0000000000000001 #double standard predvidja 15-16 tacnih cifara, kasnije cifre se grubo optimizuju pa je ovo 5.0

# #ako su cifre manje od 15-16 onda ostavlja takvim kakvi jesu

# lista = [5,10]
# b = 9.999999999999999999999999 #isti slucaj i za ovo
# if b in lista:
# 	print(b) #ako su sve nule on ih gleda kao int, ako nisu nista, ne zaokruzuje


# class Nesto: #zamisli ovo proslo ovako,a ja lupetala sintaksu
# 	glava = 5
# 	noge = 4

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>




































# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# brojevi = []


# for i in range(2,101):
# 	for j in range(2,101):
# 		if i**j not in brojevi: #moze i bez ovog uslova zbog ole printa
# 			brojevi.append(i**j)

# #print(brojevi)
# print(len(list(set(brojevi))))


# a = 585

# print(a)

# print(bin(a)) #0b...... b je flag za binarno #povratan tip je string
# print(oct(a))
# print(hex(a))


# sum = 0
# for i in range(1_000_000):
# 	if str(i) == str(i)[::-1] and bin(i)[2::] == bin(i)[:1:-1]: #do drugog
# 		sum = sum + i 
# print(sum)

# #eulerProject problem 11
# stringMatrice ='''08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
# 49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
# 81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
# 52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
# 22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
# 24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
# 32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
# 67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
# 24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
# 21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
# 78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
# 16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
# 86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
# 19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
# 04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
# 88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
# 04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
# 20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
# 20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
# 01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48'''

# red = []

# matrica = []

# broj = ''
# for i in stringMatrice:
# 	if i == ' ':
# 		red.append(int(broj))
# 		broj = ''
# 	elif i  == '\n':
# 		red.append(int(broj))
# 		matrica.append(red)
# 		red = []
# 		broj = ''
# 	else:
# 		broj += i
# #poslednji red i kolona posto u pythonu nema end of string		
# red.append(int(broj))
# matrica.append(red)


# # print(matrica)

# # maxProizvod = 1
# # proizvod = 1
# # maxPoRedu = []
# # doCetiri = 1
# # for i in matrica:
# # 	for j in i:
# # 		maksBroj = max(i)
# # 		proizvod *= maksBroj
# # 		maxPoRedu.append(maksBroj)
# # 		i.remove(maksBroj)
# # 		doCetiri += 1
# # 		if doCetiri == 4:
# # 			break
# # 	print(proizvod)
# # 	if proizvod > maxProizvod:
# # 		maxProizvod = proizvod
# # 	proizvod = 1

# # print(maxProizvod)







# #po redovima	
# maxProizvod = 1
# #proizvod2 = red[1] * red[2] * red[3] * red[4]
# for i in range(20): #0 1 2 3
# 	for j in range(3,20): #3 4 5 6
# 		#red
# 		proizvod = matrica[i][j] * matrica[i][j-1] * matrica[i][j-2] * matrica[i][j-3]
# 		if proizvod > maxProizvod:
# 			maxProizvod = proizvod
# 		#kolone
# 		proizvod = matrica[j][i] * matrica[j-1][i] * matrica[j-2][i] * matrica[j-3][i]
# 		if proizvod > maxProizvod:
# 			maxProizvod = proizvod

# 		#dijagonala glavna 
# 		proizvod = matrica[j][j] * matrica[j-1][j-1] * matrica[j-2][j-2] * matrica[j-3][j-3]
# 		if proizvod > maxProizvod:
# 			maxProizvod = proizvod

# 		#iznad dijagonale
# 		#TODO
# 		#ispod dijagonale
# 		#TODO  
# 		proizvod = matrica[j][j] * matrica[j-1][j-1] * matrica[j-2][j-2] * matrica[j-3][j-3]
# 		if proizvod > maxProizvod:
# 			maxProizvod = proizvod
# 		#dijagonale u desno
# 		if j + i > 19:
# 			continue
# 		proizvod = matrica[j][j + i] * matrica[j-1][j-1 + i] * matrica[j-2][j-2 + i] * matrica[j-3][j-3 + i] #glavna dijagonala
# 					# matrica[3][4] * matrica[2][3] * matrica[1][2] * matrica[0][1]
# 		if proizvod > maxProizvod:
# 			maxProizvod = proizvod
# 		proizvod = matrica[j + i][j] * matrica[j-1 + i][j-1] * matrica[j-2 + i][j-2] * matrica[j-3 + i][j-3] #glavna dijagonala
# 		if proizvod > maxProizvod:
# 			maxProizvod = proizvod
# #dijagonale u levo
# 		proizvod = matrica[-(j)][-(j + i)] * matrica[-(j-1)][-(j-1 + i)] * matrica[-(j-2)][-(j-2 + i)] * matrica[-(j-3)][-(j-3 + i)] #glavna dijagonala
# 					# matrica[3][4] * matrica[2][3] * matrica[1][2] * matrica[0][1]
# 		if proizvod > maxProizvod:
# 			maxProizvod = proizvod
# 		proizvod = matrica[-(j + i)][-(j)] * matrica[-(j-1 + i)][-(j-1)] * matrica[-(j-2 + i)][-(j-2)] * matrica[-(j-3 + i)][-(j-3)] #glavna dijagonala
# 		if proizvod > maxProizvod:
# 			maxProizvod = proizvod
						
# print(maxProizvod)


# # for i in range(10):
# # 
# # else:
# # 
# # uvek se ovaj deo koda izvrsi
# # 


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# f = open("demofile.txt") #otvorimo file 

# f = open("demofile.txt","rt") #procitaj u tekstualnom formatu


f = open("C:/Users/Comp/Desktop/pythonNaila/testfile.txt","r") #ovako ces sa /

print(f.read())
print(f.readline()) #samo jednu liniju ce procitati

for x in f:
	print(x) #procitace i \n i sam print ima svoj \n
	#jedna linija je jedan string


