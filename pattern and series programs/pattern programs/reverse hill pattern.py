'''Reverse hill:

 *********
  *******
   *****
    ***
     *

          '''

         

''' step1: print increasing triangle pattern
    step2: print two decreasing triangles patterns
    step3: there is an extra coloumn when we join two decreasing patterns.
           to remove that column, we decrease one in j range
           (because i handles rows and j handles colunms).
           so (i,n) becomes (i,n-1).'''

'''note: you can change 
                        for j in range(i,n)
                        to
                        for j in range(i,n-1)

                        for any one of the two decreasing patterns,
                        wont matter which parrticular one it is.
'''

n = int(input("Enter the size of reverse hill: "))
for i in range(n):
    for j in range(i+1):
        print(" ",end='')
    for j in range(i,n):
        print("*",end='')
    for j in range(i,n-1):
        print("*",end='')
    print()
    


