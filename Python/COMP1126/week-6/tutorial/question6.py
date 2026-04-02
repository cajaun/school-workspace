# def myLen(array):
  
  
#   if not array:
#     return 0
#   else:
#     return 1 + myLen(array[1:])
  
# print(myLen([1,2,5,7,6,8]))


def oddlist(arr):
    if not arr:
        return []
    
    if arr[0] % 2 != 0:
        return [arr[0]] + oddlist(arr[1:])
    

    else:
        return oddlist(arr[1:])


print(oddlist([1, 2, 3, 4, 5, 6, 7, 8, 9]))  
