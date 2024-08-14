a = int(input("Введіть a: "))
while a < 1 or a > 100:
    a = int(input("Введіть a ще раз: "))

b = int(input("Введіть b: "))
while b < 1 or b > 100:
    b = int(input("Введіть b ще раз: "))

if a > b:
    r = a / b + 31
elif a == b:
    r = -25
else:
    r = (a * 5 - 1) / a

print("Результат обчислення виразу: ", r)
