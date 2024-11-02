number = int(input("Enter number: "))
temp = number
reverse = 0

while (number > 0):
    digit = number % 10
    reverse = reverse * 10 + digit 
    number = number // 10
if temp == reverse:
    print("Palindrome")
else:
    print("Not palindrome")