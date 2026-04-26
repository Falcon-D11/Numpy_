"""
stacking
vstack() row wise
hstack() column wise
"""
import numpy as np

arr1= np.array([18, 15, 14])
arr2=np.array([13,11,78])
print(np.vstack((arr1,arr2)))
print(np.hstack((arr1,arr2)))

"""
spliting

np.split()- in equal parts
np.hsplit()
np.vsplit()
"""
arr= np.array([18, 15, 14,23,53,77])
print(np.split(arr,3))