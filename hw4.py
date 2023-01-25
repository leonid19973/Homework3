n = float(input("Введите целое число: "))
s = 0
i = 1
while i <= n:
    s += i**3
    i += 1
print(s)



n = float(input("Введите целое число: "))
s = 0
for i in (1, n):
    s += i**3
print(s)

