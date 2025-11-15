# Function 1: Lists - Finding the Maximum and Second Maximum in a List
# This function takes a list of numbers as input and returns the maximum and second maximum values.
def max_two_in_list(numbers):
    if not numbers:
        return (None, None)
    if len(numbers) == 1:
        return (numbers[0], None)
    
    first = max(numbers)
    second = None
    
    for num in numbers:
        if num != first:
            if second is None or num > second:
                second = num

    return (first, second)

# Function 2: Lists - Removing Duplicates and Sorting
# This function takes a list of numbers and returns a sorted list with duplicates removed.
def remove_duplicates_and_sort(numbers):
    unique = []  
    for num in numbers:
        if num not in unique: 
            unique.append(num)

    unique.sort() 
    return unique

# Function 3: Single-Dimensional Arrays - Cumulative Sum
# This function takes an array (list) of numbers and returns a new list where each element is the cumulative sum of the previous elements.
def cumulative_sum(arr):
    result = []
    total = 0

    for num in arr:  
        total += num
        result.append(total) 

    return result

# Function 4: Two-Dimensional Arrays - Matrix Transpose
# This function takes a 2D list (matrix) and returns its transpose.
def transpose_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    transpose = []

    for j in range(cols):  
        new_row = []
        for i in range(rows):
            new_row.append(matrix[i][j])
        transpose.append(new_row)

    return transpose

# Function 5: Slicing - Extracting Every Nth Element
# This function takes a list and a step value N and returns every Nth element.
def slice_every_nth(lst, step):
    result = []

    for i in range(0, len(lst), step):
        result.append(lst[i])

    return result

# Function 6: Arithmetic Operations with Arrays - Dot Product
# This function takes two lists of the same length and returns their dot product.
def dot_product(list1, list2):
    total = 0

    for i in range(len(list1)):
        total += list1[i] * list2[i] 

    return total

# Function 7: Arithmetic Operations with Arrays - Matrix Multiplication
# This function takes two 2D lists (matrices) and returns their matrix product.
def matrix_multiplication(matrix1, matrix2):
    rows_A = len(matrix1)
    cols_A = len(matrix1[0])
    cols_B = len(matrix2[0])
    result = []

    for i in range(rows_A):
        new_row = []
        for j in range(cols_B):
            sum_product = 0
            for k in range(cols_A):
                sum_product += matrix1[i][k] * matrix2[k][j]
            new_row.append(sum_product)
        result.append(new_row)
        
    return result