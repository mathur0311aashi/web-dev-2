# sorting
# arr = [10, 30, 20, 40, 5]
# is_sorted = True
# for i in range(0, len(arr)-1):
#     if (arr[i] <= arr[i+1]):
#         is_sorted = False
#         break
    
# if is_sorted:
#     print("The array is soroted")
# else:
#     arr.sort()
#     print("The array is now sorted", arr)

# move all zeros to the end of the array    
# arr = [0, 21, 0, 0, 15, 6, 0]
# arr1 = []
# arr2 = []
# count = 1
# for i in range (0, len(arr)):
#     if (arr[i] == 0):
#         count += 1
#         arr1.append(0)
#     else:        
#         arr2.append(arr[i])

# arr = arr2 + arr1
# print(arr)


# for reversing the array
# arr = [2, 4, 7, 9, 1]
# j = len(arr)
# for i in range(len(arr) // 2):
#     j = len(arr) - 1 - i
#     arr[i], arr[j] = arr[j], arr[i]

# print(arr)  # Output: [1, 9, 7, 4, 2]



# for finding the same elements in the array
arr = [2,2,2,2,2,2]
for i in range(0, len(arr)):
    if (arr[i]==arr[i]+1):
        print("the same elements are", arr[i])
    