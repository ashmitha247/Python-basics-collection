'''
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
4 4 4 4
3 3 3
2 2
1      '''

x = int(input("x: "))
p=1

for i in range(x):
    for j in range(i+1):
        print(p,end=" ")
    p+=1
    print()
p=x-1
for i in range(x-1,0,-1):
    for j in range(i):
        print(p,end=" ")
    p-=1
    print()