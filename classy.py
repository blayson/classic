class User:
    def __init__(self,id,name="Lecha",surname='Ermak',age=20,foto_path="/home/andrei/Загрузки/1.jpg",
                 kontakt_ref="https://www.facebook.com/profile.php?id=100010513029228&fref=hovercard&hc_location=chat"):
        self.id = id
        self.name = name
        self.surname = surname
        self.age = age
        self.foto_path = foto_path
        self.kontakt_path = kontakt_ref


class Trip:
    def __init__(self, id, dest,date,time,time_diff,max_cap = 20):
        self.id = id
        self.dest = dest
        self.date = date
        self.time = time
        self.time_diff = time_diff
        self.max_cap = max_cap



class Flight:
    def __init__(self,id,from_tmsp,to_tmsp,cost,duration,from_location):
        self.id = id
        self.from_tmsp = from_tmsp
        self.to_tmsp = to_tmsp
        self.cost = cost
        self.duration = duration
        #TODO inicialization with sygic
        self.from_location = from_location