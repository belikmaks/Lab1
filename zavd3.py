n = int(input("Введіть n: "))

while n < 1 or n > 9:
    n = int(input("Введіть n ще раз: "))

for i in range(1, n + 1):
    print("" * (n - i), end= (n-1) * "  ")
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()

for i in range(n, 0, -1):
    print("  " * (n - i), end="")
    for j in range(1, i + 1):
        print(j, end=" ")
    print()