def calci(a, b):
    return (a+b, a-b, a*b, a/b)

a = int(input("Enter 1st Number: "))
b = int(input("Enter 2nd Number: "))

res = calci(a, b)

print(f"Addition: {res[0]} \n Substraction: {res[1]} \n Multiplication: {res[2]} \n Division: {res[3]}")