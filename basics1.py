import numpy as np

# Creating a 1D array
marks = np.array([18, 15, 14])
print(marks)

# Creating a 2D array
marks_2d = np.array([
    [18, 15, 14],
    [19, 15, 18]
])
print(marks_2d)

# Creating an array filled with ones
ones_array = np.ones((3, 4))
print(ones_array)

# Creating an array filled with zeros
zeros_array = np.zeros((3, 4))
print(zeros_array)

# Creating a sequence using arange(start, stop, step)
sequence_array = np.arange(1, 10, 2)
print(sequence_array)

# Creating an identity matrix
identity_matrix = np.eye(5)
print(identity_matrix)