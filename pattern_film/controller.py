from model import Film, list_films
from views import menu

film1 = Film('1test','1test','1test','1test','1test','1test',[{'name':'ivan','role':'boss'}])
film2 = Film('test','test','test','test','test','test',[{'name':'ivan','role':'boss'}])
list_films.append(film1)
list_films.append(film2)
menu(list_films)