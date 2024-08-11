def cubeN(val=2):
    return val**3

def checkS(str1, str2):
    return str1 == str2

choice = int(input("Enter (1) to find cube of a number \n Enter (2) to check if two strings are equal: "))

if choice == 1:
    num = int(input("Enter a number: "))
    print(f"The cube of {num} is {cubeN(num)}")

elif choice == 2:
    str1 = input("Enter first string: ")
    str2 = input("Enter second string: ")
    print(checkS(str1, str2))

else:
    print("Not a valid choice, exiting")