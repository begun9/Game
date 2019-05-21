import time
import random

x = {'level':1, 'nameHeroes':'', 'меч':5}
# Оружие героя
def items():
    global x
    s = random.randint(1,4)
    item = {'меч':s}
    x['меч'] = s
    return item
# Рассчет силы героя
def Sila():
    global x
    SilaHeroes = x['level']+x['меч']
    return SilaHeroes

# Уровнь монстара
def Monstrs():
    lev = random.randint(1,4)
    return lev
# Загрузка в файл
def OpenFile():
    f = open("heroes.txt").read()
    f.write(f)
    f.close()
    my_file = open("heroes.txt", "r")
    print(my_file.read().split())
    return my_file
# Выбор двери
def level1(): #
    print('''Перед тобой две двери, в какую пойдешь? 1 или 2?''')
    otvet = int(input())
    i = ObrabotkaLevel(otvet)

def Heroes():
    global x
    for key, item in x.items():
        print(str(key) + ' : '+str(item))
    print('Команды : герой - узнать характеристики героя.')
def ObrabotkaLevel(Otvet):
    # paramRandom = random.randint(0, 1)
    paramRandom = 1
    print('Ты открыл ' + str(Otvet) + ' и...')
    time.sleep(2)
    if paramRandom == 1:
        Level = Monstrs()
        SilaHeroes = Sila()
        print('К тебе вылетает дракон, его сила '+str(Level))
        print('Твоя сила '+ str(Sila()))
        if SilaHeroes > Level:
            Vin()
        else:
            GameOver()
    if paramRandom == 0:
        Vin()

def Move(moveNext):
    if moveNext == 'да':
        level1()
    elif moveNext == 'герой':
        Heroes()
    else:
        return

def Vin():
    print('К тебе вылетает дракон и дает кучу золота! Поздравляю')
    for key, item in items().items():
        print('Так же ты находишь ' + str(key) + ', его сила ' + str(item))
    print('Забрать '+str(key)+'?')

    levelApp('level')

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
    PlayAgain = input().lower()
    Move(PlayAgain)

def Pole():
    listMonstors = random.sample(range(0, 24), 10)
    ListPole = [c for c in 24]



