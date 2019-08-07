def merge_sorted(arr1, arr2):
    sorted_arr = []
    i, j = 0, 0
    if arr1[i] < arr2[j]:
        sorted_arr.append(arr1[i])
    else:
        sorted_arr.append(arr2[j])
    return sorted_arr


l1 = [1,4,6,8,10]
l2 = [2,3,5,7,8,9]