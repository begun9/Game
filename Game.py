import time
import random

x = {'level':1, 'nameHeroes':'', 'меч':5}
listMonstors = random.sample(range(1, 25), 10)

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
# def OpenFile():

# Выбор двери
def level1(start): #
    print('Ты натыкаешься на монстра. ')
    time.sleep(2)
    if random.randint(0, 1) == 0:
        print('Он тебя замечает, теперь тебе нельзя скрыться и он идет к тебе!!!')
        i = ObrabotkaLevel(otvet, start)
    otvet = int(input())
    i = ObrabotkaLevel(otvet, start)

def Heroes():
    global x
    for key, item in x.items():
        print(str(key) + ' : '+str(item))
    print('Команды : герой - узнать характеристики героя.')
def ObrabotkaLevel(Otvet, start):
    # paramRandom = random.randint(0, 1)
    global listMonstors
    paramRandom = 1
    print('Он подошел и...')
    time.sleep(2)
    if paramRandom == 1:
        Level = Monstrs()
        SilaHeroes = Sila()
        print('Его сила '+str(Level))
        print('Твоя сила '+ str(Sila()))
        if SilaHeroes > Level:
            Vin()
            listMonstors.remove(start)
        else:
            GameOver()
    if paramRandom == 0:
        Vin()

def Move(moveNext, cikl):
    if moveNext == 'да':
        vozmHod(cikl)
        cikl = hod(cikl)

        # level1()
    elif moveNext == 'герой':
        Heroes()
    else:
        return
    return cikl

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


def vozmHod(Position):
    pyt = ''
    if Position % 5 != 0:
        pyt = pyt + "Влево "
        # print("Влево")
    if (Position + 1) % 5 != 0:
        pyt = pyt + "Вправо "
        # print("Вправо")
    if Position not in range(20, 25):
        pyt = pyt + "Вниз "
        # print("Вниз")
    if Position not in range(0, 5):
        pyt = pyt + "Вверх "
        # print("Вверх")

    print(pyt)


def hod(cikl):
    i = input().lower()
    if i == "вверх":
        cikl = cikl - 5
    elif i == "вниз":
        cikl = cikl + 5
    elif i == "влево":
        cikl = cikl - 1
    elif i == "вправо":
        cikl = cikl + 1
    else:
        print("Ой, туда я не хочу идти")

    return cikl



ListPole = [i for i in range(0, 25)]

print('''Привет, как тебя зовут?''')
x['nameHeroes'] = str(input())
print('Приветствую тебя, ' + x['nameHeroes'] + '!')
print(listMonstors)
PlayAgain = ''
start = 0
while PlayAgain != 'выход' and PlayAgain != 'нет':
    print('Что будем делать?')
    PlayAgain = input().lower()
    start = Move(PlayAgain, start)
    if start in listMonstors:
        level1(start)





