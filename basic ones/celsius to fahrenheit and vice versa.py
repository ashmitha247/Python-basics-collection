'''Formula to convert CELSIUS TO FAHRENHEIT:
   F = (C * 9/5)+32

   Formula to convert FAHRENHEIT TO CELSIUS:
   C = (F - 32) / (9/5)'''

#FAHRENHEIT TO CELSIUS CODE:

f = float(input("Enter temp in fahrenheit: "))
c = (f-32) / (9/5)
print(f"{f} fahrenheit is {c:.3f} celsius") # .3f tells it to print only till 3 decimals. 
                                            #colon before .3f is necessary for formatted string.
'''output:
          Enter temp in fahrenheit: 26
26.0 fahrenheit is -3.333 celsius'''