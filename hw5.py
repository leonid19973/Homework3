import random
a = random.randrange(0, 100)
#print(a)
print('Играем в игру угадай число!\nВведите число от 0 до 100:')



while True:
    n = str(input())
    if int(n) > int(a):
        print('Ваше число больше, попробуйте еще раз:\n')
    elif int(n) < int(a):
        print('Ваше число меньше, попробуйте еще раз:\n')
    else:
        print('Вы выиграли!')
        break