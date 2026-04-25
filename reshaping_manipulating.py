import numpy as np

# Reshaping array
marks = np.array([18, 15, 14, 19, 15, 18])

reshaped_arr = marks.reshape(2, 3)
print(reshaped_arr)


# Flattening array
marks_2d = np.array([
    [18, 15, 14],
    [19, 15, 18]
])

"""
.ravel() -> may affect the original array (returns a view when possible)
.flatten() -> creates a copy and changes do not affect original array
"""

print(marks_2d.ravel())
print(marks_2d.flatten())