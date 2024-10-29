num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

if num1 >num2 and num1> num3:
    print(f"{num1} is the largest number")
if num2>num1 and num2>num3:
    print(f"{num2} is the largest number")
else:
    print(f"{num3} is the largest number")

'''output
Enter the first number: 10
Enter the second number: 20
Enter the third number: 30
30 is the largest number'''