#method 1
x = int(input("x: "))
y = int(input("y: "))
#swap the variables
temp = x
x = y
y = temp
print(f"The values of x and y after swapping are: {x} and {y}")



#method 2

x = int(input("x: "))
y = int(input("y: "))
#swap the variables
x,y = y,x
print(f"The values of x and y after swapping are: {x} and {y}")


'''output
x: 8
y: 9
The values of x and y after swapping are: 9 and 8'''