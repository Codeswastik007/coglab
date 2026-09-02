import numpy as np

#############Q1
arr = np.array([1, 2, 3, 4, 5])
print("Original Array:", arr)

# a) Add 2 
print("After adding 2:", arr + 2)

# b) Multiply 3
print("After multiplying by 3:", arr * 3)

# c) Divide 2
print("After dividing by 2:", arr / 2)



#############Q2
arr = np.array([1, 2, 3, 6, 4, 5])

print("Original array:", arr)
print("Reversed array:", arr[::-1])


x = np.array([1, 2, 3, 4, 5, 1, 2, 1, 1, 1])
values, counts = np.unique(x, return_counts=True)  ##find the unique values and their counts
most_frequent = values[np.argmax(counts)]
indices = np.where(x == most_frequent)[0]
print("Most frequent value:", most_frequent)
print("Indices:", indices)


y = np.array([1, 1, 1, 2, 3, 4, 2, 4, 3, 3])
values, counts = np.unique(y, return_counts=True)
most_frequent = values[np.argmax(counts)]
indices = np.where(y == most_frequent)[0]
print("Most frequent value:", most_frequent)
print("Indices:", indices)


##############Q3
arr = np.array([[10, 20, 30],
                [40, 50, 60],
                [70, 80, 90]])
print("1st row, 2nd column:", arr[0, 1])
print("3rd row, 1st column:", arr[2, 0])



###############Q4
Swastik = np.linspace(10, 100, 25)
print("Array:", Swastik)
print("Dimensions:", Swastik.ndim)
print("Shape:", Swastik.shape)
print("Total elements:", Swastik.size)
print("Data type:", Swastik.dtype)
print("Total bytes:", Swastik.nbytes)
transpose = Swastik.reshape(5, 5).T
print(transpose)



################Q5
ucs420_Swastik = np.array([
    [10, 20, 30, 40],
    [50, 60, 70, 80],
    [90, 15, 20, 35]
])

print("Original Array:")
print(ucs420_Swastik)

# Mean
print("Mean:", np.mean(ucs420_Swastik))

# Median
print("Median:", np.median(ucs420_Swastik))

# Maximum
print("Maximum:", np.max(ucs420_Swastik))

# Minimum
print("Minimum:", np.min(ucs420_Swastik))

# Unique 
print("Unique elements:", np.unique(ucs420_Swastik))

# Reshape
reshaped_ucs420_Swastik = ucs420_Swastik.reshape(4, 3)

print("Reshaped Array:")
print(reshaped_ucs420_Swastik)

# Resize
resized_ucs420_Swastik = np.resize(ucs420_Swastik, (2, 3))

print("Resized Array:")
print(resized_ucs420_Swastik)
