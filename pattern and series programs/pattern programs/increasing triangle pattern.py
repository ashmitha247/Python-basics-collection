#for reference this is the triangle we're supposed to print:

'''    * 
       **
       ***
       ****
       *****  '''


n = int(input("Enter the pattern size: "))
for i in range(n):
    for j in range(i+1):
        print("*",end='')
    print()
