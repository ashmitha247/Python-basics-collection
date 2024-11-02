##for reference this is the right sided triangle we're supposed to print:
'''  *****
      ****
       ***
        **
         *  '''

#step 1: print a increasing traingle pattern with space
#step 2: print an decreasing traingle pattern with asterisk

n = int(input("Enter pattern size: "))
for i in range(n):
    for j in range(i+1):
        print(" ",end='')
    for j in range(i,n):
        print("*",end='')
    print()