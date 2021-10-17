# print('1-saboranje')
# print('ostali brojevi mnozenje')


# izbor = int(insert(print('Unesite broj')))

# prviBroj = int(insert(print('Unesite prvi broj')))
# drugiBroj = int(insert(print('Unesite drugi broj')))


# if izbor == 1 :
#     print('Zbir je',prviBroj+drugiBroj)
# else :
#     print('Umnozak je',prviBroj*drugiBroj)

# jeLKec = int(input('Unesite 0 ili 1'))
# jeLNula = int(input('Unesite 0 ili 1'))

# if jeLKec and jeLNula:
#     print('True')
# else:
#     print('False')


# prvi = int(input('Unesite prvi broj'))
# drugi = int(input('Unesite drugi broj'))

# if prvi > 0 and drugi < 0 :
#     print('TRUE')
#     if prvi <= drugi and drugi <= 0 :
#         print('False')
#     else :
#         print('True')
# else :
#     print('False')


# a = float(input('Unesite prvu stranicu'))
# b = float(input('Unesite drugu stranicu'))
# c = float(input('Unesite trecu stranicu'))

# print(a,b,c)
# if a + b > c and c + b > a and a + c > b: #ako trougao postoji sve tri stranice moraju da imaju ovaj uslov
#     if a == b and a == c : #zbog i kao da si napisao a == b == c uporedjuje odjednom sva tri
#         print('Jednakostranican')
#     else if a == b != c or a == c != b or b == c != a :
#         print('Jednakokraki')
#     else 
#         print('Raznostranican')
# else :
#     print('Trougao ne postoji')

# if broj == 1:
#     print('Broj je 1')
# elif broj == 2:
#     print('Broj je 2')
# elif broj == 3:
#     print('Broj je 3')
# else:
#     print('BRoj je veci od 3')

# broj = input(print('Unesite broj'))

# if broj > 0:
#     print('Pozitivan')
# elif broj < 0:
#     print('Negativan')
# else 
#     print('Jednak nuli')


# broj1 = int(input('Unesite broj'))
# broj2 = int(input('Unesite broj'))

# operacija = input(print('Unesiite operaciju'))

# if operacija == '+':
#     print(broj1+broj2)
# elif operacija == '-':
#     print(broj1+broj2)
# elif operacija == '*':
#     print(broj1*broj2)
# elif operacija == '/':
#     print(broj1/broj2)
# else:
#     print('Niste uneli validan znak')


Izracunati psece godine u ljudske 

pravilo 1
    u prve dve godine jedna pseca je kao 2.5 ljudskih 
nakon 2 godine 
    jedna pseca je kao 1.5 ljudskih 
uneti psece godine i izracuati koliko je u ljudskim godinama

godine = input('Unesite psece godine')
if(godine < 2)
    print(godine * 2.5)
else 
    print(godine * 1.5)
