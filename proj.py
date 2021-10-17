username = 'admin' #Podrazumevano ime korisnika da je admin
password = 'admin' #POdrazumevana sifra korisnika da je admin

users = { 
    'Petar' : {'username' : 'Petar','sifra': '02145', 'tip' : 'vlasnik'},
	'Marko' : {'username' : 'Marko','sifra': '04879','tip' : 'prodavac'},
	'Janko' : {'username' : 'Janko','sifra': '78456', 'tip' : 'prodavac'}
} #Recnik sa korisnicima sa svojim imenima i sifrom organizovanim u recnike


objekti = {
    1 : {'name' : 'Maxi', 'tip' : 'supermarket', 'artikli' : {}}
}


#artikal : { name : artikal, kolicina : 32, cena : 565, tip : hrana }
activeUser = None #Recnik koji ce sadrzati ime i sifru trenutnog korisnika
while True: #BEskonacna petlja koja se prekida kad se unese opcija 2
    print('1) Login')
    print('2) Izlaz')
    opcija = int(input('Unesite opciju'))
    if opcija == 1: #korisnik je usao u program
        
        while True: # Beskonacna petlja za unos imena i sifre koja se prekida kad se poklopi ime sa sifrom
            usern = input('Unesite username:')
            passw = input('Unesite sifru')
            if usern in users.keys() and passw == users[usern]['sifra']: #ako je uneseno ime u kljucevima korisnika i sifra u vrednostima sifri od korisnika
                activeUser = users[usern] #Aktivni korisnik postaje recnik sa podacima korisnika pod kljucem imena korisnika
                print('Uspesno ste login!')
                break #zavrsava se petlja za unos
        if activeUser and activeUser['tip'] == 'vlasnik': #ako je tip u korisniku vlasnik
            while True: #Beskonacna petlja kojom korisnik radi sta hoce
                print('login: ', activeUser['username'])
                print('1) Kreirati objekat')
                print('2) Izbrisati objekat')
                print('3) Kreirati artikal')
                print('4) Izbrisati artikal')
                print('5) dodaj korisnika')
                print('6) ukloni korisnika')
                print('7) log out')
                opc = input('Unesite opciju: ') #nakon cega se pita da li hoce da se izloguje
                if opc == '1': 
                    podaciObjekta = {}
                    podaciObjekta['name'] = input('Unesite naziv objekta')
                    podaciObjekta['tip'] = input('Unesite tip objekta')
                    podaciObjekta['artikli'] = {}
                    objekti[max(objekti.keys()) + 1] = podaciObjekta
                    print(objekti)
                if opc == '2':
                    for i,j in objekti.items():
                        print(i, j['name']) #kljuc broj i ime iz dicta
                    nazivObjekta = int(input('Unesite broj objekta koje treba za izbrisete'))
                    objekti.pop(nazivObjekta)
                    print(objekti)
                if opc == '3':
                    podaciArtikla = {}
                    nazivArtikla = input('Unesite naziv artikla')
                    podaciArtikla['name'] = nazivArtikla
                    podaciArtikla['tip'] = input('Unesite tip artikla')
                    podaciArtikla['cena'] = int(input('Unesite cenu artikla'))
                    for i,j in objekti.items():
                        print(i, j['name'])
                    brojObjekta = int(input('Unesite broj objekta u koji cete ubaciti artikal'))
                    objekti[brojObjekta]['artikli'][nazivArtikla] = podaciArtikla
                    print(objekti[brojObjekta]['artikli'])
                if opc == '4':
                    objekti[input('Uneiste naziv objekta')]['artikli'].pop(input('Unesite naziv artikla'))
                if opc == '6':
                    for i,j in objekti.items():
                        print(i, j['username'])
                    users.pop(input('Unesite username koji hocete da izbrisete'))
                    
                if opc == '5':
                    korisnik = {} 
                    korisnik['username'] = input('Unesite username')
                    korisnik['sifra'] = input('Unesite sifru')
                    korisnik['tip'] = input('Unesite tip')
                    users[korisnik['username']] = korisnik

                if opc == '7': #log out 
                    break    #prekida se petlja za rad korisnika i ponavlja se unos imena i sifre korisnika odnosno login
        #Prodaje = Uklanja kolicinu, Da ima log out da izadje, da unese na stanje 
        elif activeUser and activeUser['tip'] == 'prodavac':
            while True:
                print('1) Prodaje artikal')
                print('2) Unesi na stanje')
                print('3) Kreirati objekat')
                print('4) Izbrisati objekat')
                print('5) Kreirati artikal')
                print('6) Izbrisati artikal')
                print('7) log out')
                opc = input('Unesite opciju')
                if opc == '7':
                    break
    
    
    elif opcija == 2: #ovde se prekida petlja
        print('Izlaz')
        break
