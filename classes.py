
class Zaglavlje:

    def __init__(self,co2,godine):
        self.co2 = co2
        self.godine = godine
    
    def __str__(self):
        return f"{self.co2} sa godinama {self.godine}"


class Drzava:

    def __init__(self,zemlja,zagadjenje):
        self.zemlja = zemlja
        self.zagadjenje = zagadjenje

    def __str__(self):
        return f"Drzava {self.zemlja}, sa zagadjenjem {self.zagadjenje}"

    def get_value_by_year(self,year_index):
        return self.zagadjenje[year_index]

    #staticna f-ja, moze da se pozove nad klasom, ne instancom

    def set_state_of_countries(path):
        
        f = open(path,'r')
        
        countries = []
        
        for i in f:
            el = i.split(',')

            if el[0] == 'CO2 per capita':
                head = Zaglavlje(el[0], [int(x) for x in el[1:]])
                continue
            country = Drzava(el[0], [float(x) for x in el[1:]])
            countries.append(country)
        
        f.close()

        return head, countries
    
    #nema self,staticna je
    def get_min_max_avg_by_year(index,countries):
        val_by_year = [i.zagadjenje[index] for i in countries]
        min_index = val_by_year.index(min(val_by_year))
        max_index = val_by_year.index(max(val_by_year))

        avg = sum(val_by_year) / len(val_by_year)
    # Avg zemlja
        razlikeDrzava = []

        for i in val_by_year:
            razlikeDrzava.append(abs(i - avg))

        indeksMinimalne = razlikeDrzava.index(min(razlikeDrzava))

        return (countries[min_index].zemlja, min(val_by_year)),(countries[max_index].zemlja, max(val_by_year)), (avg, countries[indeksMinimalne].zemlja)



