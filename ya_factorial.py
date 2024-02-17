
def factorial(n):
    if n < 0:
        return "The factorial of a negative number is undefined"
    elif n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result
num = int(input("Input number: ")) 
detail = factorial(num)
deatail_fact = "{:,}".format(detail).replace(",",".")

print (f"The factorial of {num} equals {deatail_fact}")
