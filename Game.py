import time
import random

print('''Привет, как тебя зовут?''')
nameUser = str(input())
print('Приветствую тебя, ' + nameUser + '!')

def ObrabotkaLevel(Otvet):
    paramRandom = random.randint(1, 2)
    if paramRandom == 1:
        print('Ты открыл '+ str(Otvet) + ' и...')
        time.sleep(2)
        print('К тебе вылетает дракон и съедает тебя! ')
    if paramRandom == 2:
        print('Ты открыл '+ str(Otvet) + ' и...')
        time.sleep(2)
        print('К тебе вылетает дракон и дает кучу золота! Поздравляю')


def level1():
    print('''Перед тобой две двери, в какую пойдешь? 1 или 2?''')
    otvet = int(input())
    i = ObrabotkaLevel(otvet)

level1()



