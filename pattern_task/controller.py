from model import Jornal, Title
from views import Menu

jornal = Jornal('мой журнал')
title1 = Title('матч', 'ivan i', 890, 'матч тв', ' обзор матча')
title2 = Title('блины', 'катя к', 1000, 'кухня', 'рецепт блинов')
jornal.add_title(title1)
jornal.add_title(title2)
menu_start = Menu(jornal)
menu_start.render_menu()
print('программа завершина')