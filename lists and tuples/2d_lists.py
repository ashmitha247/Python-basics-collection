#Write a statement that creates a two-dimensional list with 5 rows and 3 columns.
#Then write nested loops that get an integer value from the user for each element in the list.

'''
        matrix = [
    [1, 2, 3],  # Row 0
    [4, 5, 6],  # Row 1
    [7, 8, 9]   # Row 2
]


Row 0: This is the first row of the matrix, and it contains the elements [1, 2, 3].
Row 1: This is the second row of the matrix, and it contains the elements [4, 5, 6].
Row 2: This is the third row of the matrix, and it contains the elements [7, 8, 9].

Accessing Elements
To access an element in a 2D list, you use two indices: the first index refers to the row, and the second index refers to the column.

Accessing the Element at Row 1, Column 2:
The first index 1 refers to the second row (Row 1).
The second index 2 refers to the third element in that row (Column 2).
So, when you write matrix[1][2], you are accessing:

matrix[1]: This gives you the entire second row, which is [4, 5, 6].
Then, within that row, matrix[1][2] accesses the third element (index 2) of that row, which is 6.

syntax for creating a 2 list using list comprehension:
two_dimensional_list = [[expression for j in range(columns)] for i in range(rows)]   '''


# Step 1: Create a two-dimensional list with 5 rows and 3 columns
rows = 5
columns = 3
two_dimensional_list = [[0 for j in range(columns)] for i in range(rows)]


# Step 2: Use nested loops to get integer values from the user
for i in range(rows):
    for j in range(columns):
        # Prompt the user for an integer value
        value = int(input(f"Enter an integer for element [{i}][{j}]: "))
        two_dimensional_list[i][j] = value

# Optional: Print the filled two-dimensional list
print("The two-dimensional list is:")
for row in two_dimensional_list:
    print(row)

'''

#before assignment: (after step1 u get this:)

two_dimensional_list = [
    [0, 0, 0],  # Row 0
    [0, 0, 0],  # Row 1
    [0, 0, 0],  # Row 2
    [0, 0, 0],  # Row 3
    [0, 0, 0]   # Row 4
]

#after assignment: (two_dimensional_list[1][2] = 5):

two_dimensional_list = [
    [0, 0, 0],  # Row 0
    [0, 0, 5],  # Row 1 (updated)
    [0, 0, 0],  # Row 2
    [0, 0, 0],  # Row 3
    [0, 0, 0]   # Row 4
]

'''

#output:
'''
Enter an integer for element [0][0]: 5
Enter an integer for element [0][1]: 4
Enter an integer for element [0][2]: 2
Enter an integer for element [1][0]: 3
Enter an integer for element [1][1]: 6
Enter an integer for element [1][2]: 7
Enter an integer for element [2][0]: 8
Enter an integer for element [2][1]: 9
Enter an integer for element [2][2]: 2
Enter an integer for element [3][0]: 4
Enter an integer for element [3][1]: 5
Enter an integer for element [3][2]: 6
Enter an integer for element [4][0]: 7
Enter an integer for element [4][1]: 3
Enter an integer for element [4][2]: 4
The two-dimensional list is:
[5, 4, 2]
[3, 6, 7]
[8, 9, 2]
[4, 5, 6]
[7, 3, 4]           '''