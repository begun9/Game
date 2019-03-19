import time
import random

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