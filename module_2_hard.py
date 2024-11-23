def generate_password(n):
    result = ""
    for i in range(1, n):
        for j in range(2, n):
            if j <= i:
                continue
            if n % (i + j) == 0:
                result += str(i) + str(j)
    return result

n = int(input("Введите число от 3 до 20: "))
if 3 <= n <= 20:
    print("Пароль:", generate_password(n))
else:
    print("Неправильный ввод!")