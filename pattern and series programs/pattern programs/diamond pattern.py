'''Diamond pattern:

     *
    ***
   *****
  *******
 *********
  *******
   *****
    ***
     *

'''


''' STEP1: Print hill pattern
    STEP2: print reverse hill pattern
    STEP3: joining both would give us an extra row.
           As i deals with rows and j deals with columns,
           we remove 1 from i, which would give us (n-1)
           (originally it was for i in range(n), now its
           for i in range(n-1))'''

#NOTE: the code goes wrong if you put n-1 in reverse hill pattern
     #use it only in reverse pattern

n = int(input("enter the size of the diamond: "))
for i in range(n-1): #code for hill pattern
    for j in range(i,n):
        print(" ",end='')
    for j in range(i+1):
        print("*",end='')
    for j in range(i):
        print("*",end='')
    print()
for i in range(n): #code for reverse hill pattern
    for j in range(i+1):
        print(" ",end='')
    for j in range(i,n):
        print("*",end='')
    for j in range(i,n-1):
        print("*",end='')
    print()

