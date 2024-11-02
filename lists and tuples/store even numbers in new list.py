#given a list of integers, find all even numbers and store them in a new list

input_list = list(map(int,input("Enter numbers (space-separated): ").split()))

even_numbers = []

for number in input_list:
    if number % 2 == 0:
        even_numbers.append(number)

print(even_numbers)  # Output: [2, 4, 6, 8, 10]