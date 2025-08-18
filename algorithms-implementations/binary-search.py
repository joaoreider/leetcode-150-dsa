
def binarySearch(arr, target):

    l, r = 0, len(arr)-1

    while l <= r: 
        mid = (l + r) // 2

        if target > arr[mid]:
            l = mid+1
        elif target < arr[mid]:
            r = mid-1
        else:
            return mid 
        
    return -1


print(binarySearch([1, 2, 3, 4, 5, 6, 7, 8], 8))