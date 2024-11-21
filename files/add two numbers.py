# Open the file in append mode and write the data
with open("file1.txt", "a") as file:
    first_number = int(input("Enter first number: "))
    second_number = int(input("Enter second number: "))
    result = first_number + second_number
    
    # Write results to the file
    file.write(f'First Number = {first_number}\tSecond Number = {second_number}\tAddition = {result}\n')

    # Print the output in the desired format
    print(f'Addition = {result}')  # Print the result directly

# Optional: Read and print the contents of the file to verify
print("\nContents of file1.txt:")
with open("file1.txt", "r") as file:
    content = file.read()
    print(content)