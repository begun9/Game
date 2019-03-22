import time
import random
x = {'level':1, 'nameHeroes':'', 'меч':''}

def items():
    global x
    s = random.randint(1,4)
    item = {'меч':s}
    x['меч'] = s
    return item
def Monstrs():
    lev = random.randint(1,4)
    return lev

def OpenFile():
    f = open("heroes.txt").read()
    f.write(f)
    f.close()
    my_file = open("heroes.txt", "r")
    print(my_file.read().split())
    return my_file

def level1(): #
    print('''Перед тобой две двери, в какую пойдешь? 1 или 2?''')
    otvet = int(input())
    i = ObrabotkaLevel(otvet)

def Heroes():
    global x
    for key, item in x.items():
        print(str(key) + ' : '+str(item))

def ObrabotkaLevel(Otvet):
    # paramRandom = random.randint(0, 1)
    paramRandom = 0
    print('Ты открыл ' + str(Otvet) + ' и...')
    time.sleep(2)
    if paramRandom == 1:
        print('К тебе вылетает дракон и съедает тебя! ')
        GameOver()
    if paramRandom == 0:
        print('К тебе вылетает дракон и дает кучу золота! Поздравляю')
        for key, item in items().items():
        # item = items().keys()

            print('Так же ты находишь ' + str(key) + ', его сила ' + str(item))
        levelApp('level')

def Move(moveNext):
    if moveNext == 'да':
        level1()
    elif moveNext == 'Герой':
        Heroes()
    else:
        return

def levelApp(param):
    if param == 'level':
        global x
        x['level'] += 1
        print('Твой уровень: '+str(x['level']))

def GameOver():
    print('Хочешь попробовать еще раз? да/д')
    return input()

print('''Привет, как тебя зовут?''')
x['nameHeroes'] = str(input())
print('Приветствую тебя, ' + x['nameHeroes'] + '!')

PlayAgain = ''
while PlayAgain != 'выход' and PlayAgain != 'нет':
    print('Идем открывать дверь?')
    PlayAgain = input()
    Move(PlayAgain)




