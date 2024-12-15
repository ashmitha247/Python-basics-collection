#write a function to find the factorial of n, where n is the parameter

def calc_fact(n):
    fact = 1
    for i in range(1,n+1):
        fact*=i
    return fact
#=int(input("Enter number: "))
#calc_fact(n)