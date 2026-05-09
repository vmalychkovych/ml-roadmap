import numpy as np

numbers = np.array([1, 2, 3, 4, 5])

print(numbers)

print(numbers + 10)

print(numbers * 2)

print(numbers / 2)

print(numbers.mean())

print(numbers.max())
print(numbers.min())

print(numbers.sum())

matrix = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(matrix)
print(matrix[0])
print(matrix[1])
print(matrix[0][1])

print(matrix.shape)

random_numbers = np.random.randint(1, 100, size=10)

print(random_numbers)