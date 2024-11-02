num = int(input("Enter a number: "))
fact=1
if num<0:
    print("Factorial doesn't exist for negative numbers")
if num==0:
    print("Factorial is 1")
if num>0:
    for i in range(1,num+1):
        fact=fact*i
print("factorial is",fact)