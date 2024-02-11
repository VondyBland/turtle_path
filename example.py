import sys

from turtle_path_calc import TurtlePath

turtle_path = TurtlePath()

matrix = [
    [2, 4, 3, 5, 1],
    [3, 1, 2, 3, 4],
    [1, 2, 5, 2, 2],
    [1, 4, 2, 3, 4]
]

path = []

max_sum_path, max_sum = turtle_path.running(matrix)

print("Path with maximum sum of elements:", max_sum_path)
print("Sum of elements in this path:", max_sum)