#1
from datetime import datetime

def render():
    print('*'*10)
    timer() #создать функцию
    print('*'*10)
def timer():
    time = datetime.now()
    time = time.strftime('%H:%M')
    print(time)
render()