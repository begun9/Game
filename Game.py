import Visilitca



print('''Привет, как тебя зовут?''')
nameUser = str(input())
print('Приветствую тебя, ' + nameUser + '!')

def level1():
    print('''Перед тобой две двери, в какую пойдешь? 1 или 2?''')
    otvet = int(input())
    #i = ObrabotkaLevel(otvet)
    i = Visilitca.ObrabotkaLevel(otvet)

def GameOver():
    print('Хочешь попробовать еще раз? да/д')
    return input()
PlayAgain = 'да'
while PlayAgain == 'да' or PlayAgain == 'д':
    level1()
    PlayAgain = GameOver()




