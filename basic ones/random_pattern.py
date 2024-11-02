''' print the following pattern:
1
22
333
4444
55555 '''



n = int(input())
p=1
for i in range(n):
    for j in range(i+1):
        print(p,end='')
    p+=1
    print()
        
   
