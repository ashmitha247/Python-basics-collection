#for reference this is the triangle we're supposed to print:

'''  *****
      ****
       ***
        **
         *  '''



n = int(input("Enter pattern size: "))
for i in range (n):
    for j in range(i,n):
        print("*",end='')
    print()

