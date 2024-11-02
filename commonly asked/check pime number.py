num = int(input("Enter number: "))
flag = 0
'''prime no. is divisible by 1 and itself so 
we check if its divsible by any number between 1 and itself(so from 2 to n-1)
(in for loop range,2 is included and n is excluded so we get numbers from 2 to n-1 as intended )'''

for i in range(2,num):
    if num%i == 0: 
        flag=1 #we break after flag=1 cuz that indicates we found a divisor other than 1 and the no. itself.
        break #break exits the current block(if block)
if flag == 1:
    print(f"{num} is not a prime number")
else:
    print(f"{num} is a prime number")


'''output:
Enter number: 98
98 is not a prime number'''


'''in the if block, we use assignment operator '=' to assign the value 1 to flag.so flag holds value 1.
in the 11th line "if flag==1", we use the equality operator '=='. it checks if flag is equal to 1.if true, it enters the block.
It's a common mistake to use flag=1 instead of flag==1 in line 11 but the diff bw assignment and equality operator is to be noted.

Use = when you want to assign a value to a variable.
Use == when you want to check if two values are equal.'''



    
