n = int(input("Enter number of terms to be printed in fibonacci: "))
a = 0
b = 1
if n == 1:
    print(a)
else:
    print(a,b,end=' ')
    for i in range(2,n):
        c = a + b
        a = b
        b = c
        print(c,end=' ')        