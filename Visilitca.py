import time
import random
x = {'level':1, 'nameHeroes':'', 'меч':int}
def Bitva(Monstor, Heroes):
    if Heroes > Monstor:
        print('Поздравляю, вы выиграли')
    else:
        rand = random.randint(1,6)
        if rand > 4:
            print('Тебе повезло, ты смог смыться')
        else:
            print('Тебе не удалось смыться..')
            GameOver()
        print('Вы проиграли, ')
def ProverkaSklada():
    print()
def GameOver():
    print('Хочешь попробовать еще раз? да/д')
    return input()
def vozmHod(Position):
    if Position%5==0:
        print("Право")
    if (Position+1)%5 == 0:
        print("Лево")
    if Position in range(0, 5):
        print("Вниз")
    if Position in range(20, 25):
        print("Вверх")
def hod(x):
    i = str(input().lower())
    if i == "вверх":
        x = x+5
    if i == "вниз":
        x = x-5
    if i == "влево":
        x = x-1
    if i == "вправо":
        x = x+1
    return х


listMonstors = random.sample(range(0, 25), 10)
# ListPole = [c for c in range(0, 25) if c not in listMonstors]
ListPole = [i for i in range(0, 25)]

print(ListPole)
print(listMonstors)
x = 0
while x!=17:
    vozmHod(x)
    x = hod(x)
    print(x)





