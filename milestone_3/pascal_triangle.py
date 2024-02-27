# 1 task
from typing import List

def get_triangle(rows: int) -> List[List[int]]:
    triangle = []
    for i in range(rows):
        row = [1] * (i + 1)
        triangle.append(row)
        for j in range(1, len(row) - 1):
            triangle[i][j] = triangle[i-1][j-1] + triangle[i-1][j]
    max_width = len(str(triangle[-1][-1]))  
    formatted_triangle = []
    for row in triangle:
        formatted_row = [f"{num:>{max_width}}" for num in row] 
        formatted_triangle.append(formatted_row)
    return formatted_triangle


def print_triangle(triangle: List[List[int]]):
    print("[")
    for row in triangle:
        print("    " + str(row) + ",")
    print("]")

triangle = get_triangle(5)
print_triangle(triangle)

# 2 task
from math import factorial
n = 11
max_coefficient=max(factorial(n)//(factorial(i)*factorial(n-i)) for i in range(n))
max_width = len(str(max_coefficient)) + 1  

for i in range(n):
    print("  " * (n - i), end="")
    
    for j in range(i + 1):
        coefficient = factorial(i) // (factorial(j) * factorial(i - j))
        print(f"{coefficient:{max_width}}", end=" ")
    
    print()