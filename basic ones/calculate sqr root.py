#Method 1- using exponentiation

a = int(input("Enter any number: "))
c = a**(1/2)
print(f"The square root of {a} is {c}")




#method 2 - using math module

import math
a = int(input("Enter any number: "))
sqr_root = math.sqrt(a)
print("The sqaure root is",sqr_root)



'''output:
   Enter any number: 64
   The square root of 64 is 8.0'''