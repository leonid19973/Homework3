
while True:
    name = str(input("введите имя: "))
    age = str(input("Введите возраст: "))
    if int(age) <= 0:
        print("Ошибка, повторите ввод: ")
    elif int(age) >= 1 and int(age) < 10:
        print("Привет шкет", name)
    elif int(age) >= 10 and int(age) < 18:
        print("Как жизнь", name)
    elif int(age) >= 18 and int(age) < 100:
        print("Что желаете", name, '?')
    else:
        print(name, " ,вы лжете - в наше время столько не живут...")




