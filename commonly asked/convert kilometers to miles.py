k = int(input("Enter the no of km: "))
mile = 1.609
m = k/mile
print(f"{k}km = {m:.3f}miles")


'''output:
Enter the no of km: 5
5km = 3.108miles'''



#additional info about formatting and rounding off:

'''When you create an f-string, you can embed expressions inside curly braces {}.
 If you want to format the output of a variable, you can do so by placing a colon (:) followed by
   the desired format specification right after the variable name inside the curly braces.

m is the variable you want to format.
The colon : indicates that what follows will be a format specifier.
.3f is the format specifier itself:
3 specifies that you want three digits after the decimal point.
f indicates that the number is a floating-point number

So, the colon is necessary because it signals the beginning of the format specification for the variable m. 
Without it, Python would not know that you intend to format the variable and would simply output the raw value of m.

#round():

# Rounding to the nearest integer
rounded_value = round(3.6)  # Output: 4
print(rounded_value)

# Rounding to 2 decimal places
rounded_value = round(3.14159, 2)  # Output: 3.14
print(rounded_value)'''
