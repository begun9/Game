import time
import random
# x = {'level':1, 'nameHeroes':'', 'меч':int}
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
    pyt = ''
    if Position%5!=0:
        pyt = pyt+"Влево "
        # print("Влево")
    if (Position+1)%5 != 0:
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
        cikl = cikl-5
    if i == "вниз":
        cikl = cikl+5
    if i == "влево":
        cikl = cikl-1
    if i == "вправо":
        cikl = cikl+1
    return cikl


listMonstors = random.sample(range(0, 25), 10)
# ListPole = [c for c in range(0, 25) if c not in listMonstors]
ListPole = [i for i in range(0, 25)]

print(ListPole)
print(listMonstors)
cikl= 0
while cikl!=17:
    vozmHod(cikl)
    cikl = hod(cikl)
    if cikl in listMonstors:
        print("Монстор")
    print(cikl)





