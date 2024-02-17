
def factorial(n):
    if n < 0:
        return "Факториал отрицательного числа не определен"
    elif n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result
num = int(input("Введите чисто: ")) 
detail = factorial(num)
deatail_fact = "{:,}".format(detail).replace(",",".")

print (f"Факториал числа {num} равен {deatail_fact}")