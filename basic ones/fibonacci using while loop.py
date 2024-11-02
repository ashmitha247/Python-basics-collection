n = int(input("Number of terms to be printed: "))
a=0
b=1
print(a,b,end=' ')
i = 0
while(i < n-2):
    c = a + b
    print(c, end = ' ')
    a = b   # a = prev value of b
    b = c   #b = sum of previous two values a,b
    i+=1
    