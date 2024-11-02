'''Hill:
              *
             ***
            *****
           *******
          *********  '''


'''step 1: print decreasing pattern triangle with spaces
   step 2: print two increasing triangles with asterisks
   step 3: change (i+1) to (i) in one of the increasing triangles
           reason for step3: printing two increasing triangles together would give us an extra column.
           so to remove that column, we remove 1 from j.
           so (i+1) becomes (i).'''

'''note: you can change 
                        for j in range(i+1)
                        to
                        for j in range(i)

                        for any one of the two increasing patterns,
                        wont matter which parrticular one it is.
'''



n = int(input("enter the size of the hill: "))
for i in range(n):
    for j in range(i,n):
        print(" ",end='')
    for j in range(i+1):
        print("*",end='')
    for j in range(i):
        print("*",end='')
    print()