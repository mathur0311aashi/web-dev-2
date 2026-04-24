# arr = [-5, -2, 0, 1, 3, 4]
# Q. to arrange the array in such a way that all negative numbers come first and then positive numbers
# for i in range(0, len(arr)):
#     for j in range(0, len(arr)-i-1):
#         if arr[j] > arr[j+1]:
#             arr[j], arr[j+1] = arr[j+1], arr[j]
# print(arr)


# low = 0
# high = len(arr) - 1 
# mid = low + (high - low) // 2
# if arr[mid] == x:
#     return mid:
# elif arr[mid] < x:



# to find the second largest number in the array
arr = [3, 1, 4, 2, 5]
for i in range(len(arr)-2, -1, -1):
    if arr[i] != arr[len(arr)-1]:
       return arr[i]
return -1
