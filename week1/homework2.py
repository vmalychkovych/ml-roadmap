import numpy as np

scores = np.array([95, 88, 76, 100, 67, 84, 91, 73, 89, 78])
print(scores.mean())
print(scores.max())
print(scores.min())
print(scores.sum())
update_scores = scores - 50
print(update_scores)
scores[3] = 20
print(scores)

matrix = np.array([
    [95, 88, 76, 100, 67, 84, 91],
    [5, 8, 6, 10, 7, 4, 1],
])
print(matrix)
print(matrix.shape)
print(matrix[0])
print(matrix[1])
print(matrix[1][3])


random_numbers = np.random.randint(1, 100, size=20)
print(random_numbers)

print(random_numbers.mean())
print(random_numbers.max())
print(random_numbers.min())

filtered_numbers = random_numbers[random_numbers > 50]
print(filtered_numbers)

small_numbers = random_numbers[random_numbers < 30]
print(small_numbers)

count_numbers = (random_numbers > 50).sum()
print(count_numbers)
