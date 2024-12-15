#Write a Python program to get the binary form of a given number.

n = int(input("n: "))
empty_string=''
while(n>>0):
    r = n%2
    empty_string=str(r)+empty_string
    n//=2
empty_string = '0' + empty_string
print(empty_string)
