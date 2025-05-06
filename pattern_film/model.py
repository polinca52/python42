class Film:
    def __init__(self, name_film, genre, director, year, time, studio, list_acter):
        self.name_film  = name_film
        self.genre = genre
        self.director = director
        self.year = year
        self.time = time
        self.studio = studio
        self.list_acter = list_acter
    
    def render(self):
        str_ = f'название:{self.name_film}\nжанр:{self.genre}\nрежиссер:{self.director}\nгод выпуска:{self.year}\nдлительность:{self.time}\
            \nстудия:{self.studio}'
        print(str_)
        print('в ролях:')
        for acter in self.list_acter:
            print(acter['name'],'-',acter['role'])

    
list_films = []

