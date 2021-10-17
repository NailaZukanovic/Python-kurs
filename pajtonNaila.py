var = 'Hello world'
#'H e l l o w o r l d'
#0 1 2 3 4 5 6 7 8 9 10
# -11 .............. -1

#print(var1[3:9])
#[3:] do kraja
#[:9] od pocetka do 8
#print(var1[2::2])
#::2
#var1[pocetni_index: krajnji_indeks:korak]

#3 4 5 6 7 8

#int float boolean string
#char posmatramo kao deo niza

#da li postoji string a u drugoj prom

# print(a in var1)
# za komentar ctrl /
# a = 10

# a = a + 1
# a += 1

# print(a) #12

# print(a > 5)
# ==

# if a > 10: #Pocinje blok koda
#     print('A je vece od 10')
#     print('A je vece od 10')
#     print('A je vece od 10')
    #uvucen je
#nece se ispisati 
    #greska
#izvrsice se uvek 

#def function():
    #spada pod funkcijom
    #daaaa

# if a == 10: #if true:
#     print('A je jednako 10')
# else:
#     print('a je razlicito od 10')

# print('Unesite broj')


#Unesi neko prirodan broj i proveri da li je deljiv sa sedam

# a = int(input('Unesite broj')) #!!! #Defaultni je string
# if a%7 :
#     print('Nije deljiv sa sedam')
# else :
#     print('Broj', a, 'je deljiv sa 7') #nema pluseva vec zarez jer nabrajas bukvalno

#sledeci cas taktika mali stocici

# realniBroj = float(input('Unesite realni broj'))

# if realniBroj < 0 :
#     print('Broj',realniBroj,'je negativan')
# else :
#     print('Broj ',realniBroj,' je pozitivan')


# ne koristi spaceee 
# a !!!!!!!!!!! dont

#isto je kao " " i ' '

#print("'I' m Dzemil'")

# \' kao karakter ga cita 
#print('I\'m Dzemil')

#viselinijski string 

#var1 = """Ovde pravimo neku vrednost koja
#moze da ide
#u vise redova
#i kako je mi napravimo 
#tako ce se 
# #prikazati"""

# prviBroj = int(input('Unesite prvi broj \n'))
# drugiBroj = int(input('Unesite drugi broj \n'))

# if prviBroj + drugiBroj == prviBroj * drugiBroj :
#     print('umnozak i zbroj 2 broj su jednaki')
# else :
#     print('Umnozak i zbroj 2 broja su razniciti')

#prviBroj = int(input('Unesite prvi broj'))
#drugiBroj = int(input('Unesite drugi broj'))

# if prviBroj == drugiBroj :
#     print('Povrsina kvadrata je ',prviBroj**2) #stepen
# else :
#     print('Povrsina pravougaonika je ',drugiBroj*prviBroj)

# rec = input('Unesite rec')
# a = 'a'
# jeste = False
# for slovo in rec:
#     if slovo == a :
#         jeste = True 

# if jeste :
#     print('Nalazi se')
# else 
#     print('Ne nalazi se')

rec = input('Unesite rec')
# samoglasnici = 'aeiou'
# nalaziSe = True VELIKO SLOVOOOOO
# for samoglasnik in samoglasnici
#     if samoglasnik in rec : #!!!!!!!
#     else : 
#         nalaziSe = False

# if nalaziSe :
#     print('Svi se nalaze')
# else :
#     print('Ne nalaze se')

if 'a' in rec or 'e' in rec or 'i' in rec or 'o' in rec or 'u' in rec:
    print('samoglasnici se nalazi u zadatoj reci')
else 
    print('samoglasnici se ne nalazi u zadatoj reci')
