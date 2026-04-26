import numpy as np
"""
inserting array
np.insert(array,index,value,axis)
array-original array
index-
value-
axis=0 row wise
axis=1 column wise
"""
arr= np.array([18, 15, 14])
new_arr=np.insert(arr,2,100)
print(new_arr)

arr_2d = np.array([
    [18, 15, 14],
    [19, 15, 18]])
new_arr=np.insert(arr_2d,1,[2,66,55],axis=0)
print(new_arr)
new_arr=np.insert(arr_2d,1,[2,66],axis=1)
print(new_arr)

# append
arr= np.array([18, 15, 14])
new_arr=np.append(arr,[22,32,23])
print(new_arr)

# concatenate
arr1= np.array([18, 15, 14])
arr2=np.array([13,11,78])
new_arr=np.concatenate((arr1,arr2))
print(new_arr)

# removing 
arr=np.array([18, 15, 14 ,13 ,11, 78])
new_arr=np.delete(arr,1)
print(new_arr)

arr_2d = np.array([
    [18, 15, 14],
    [19, 15, 18]])
new_arr=np.delete(arr_2d,0,axis=0)
print(new_arr)