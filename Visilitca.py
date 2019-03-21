import time
import random
x = 0
def OpenFile():
    f = open("heroes.txt").read()
    f.write(f)
    f.close()
    my_file = open("heroes.txt", "r")
    print(my_file.read().split())
    return my_file

def level1():
    print('''Перед тобой две двери, в какую пойдешь? 1 или 2?''')
    otvet = int(input())
    i = ObrabotkaLevel(otvet)

def ObrabotkaLevel(Otvet):
    paramRandom = random.randint(0, 1)
    print(paramRandom)
    print('Ты открыл ' + str(Otvet) + ' и...')
    time.sleep(2)
    if paramRandom == 1:
        print('К тебе вылетает дракон и съедает тебя! ')
        GameOver()
    if paramRandom == 0:
        print('К тебе вылетает дракон и дает кучу золота! Поздравляю')
        levelApp('level')
        global x
        print(x)

def Move(moveNext):
    if moveNext == 'да':
        level1()

def levelApp(param):
    if param == 'level':
        global x
        x += 1

def ParamHeroes(param):
    if param == 'level':
        global x
        x += 1

def GameOver():
    print('Хочешь попробовать еще раз? да/д')
    return input()
