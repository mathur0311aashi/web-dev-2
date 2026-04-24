# # program for sorting the array in descending order using bubble sort algorithm
# arr = [4, 1, 3, 9, 7]
# for i in range(0, len(arr)):
#     for j in range(0, len(arr)-1):

#         if arr[j] < arr[j + 1]:
#             arr[j], arr[j+1] = arr[j+1], arr[j]
# print(arr)


# code with o(n^2) time complexity for finding the two numbers in the array that add up to a target value
# arr = [2, 7, 11, 15]
# target = 9
# for i in range(0, len(arr)):
#     for j in range(i + 1, len(arr)):
#         if arr[i] + arr[j] == target or arr[j] - arr[i] == target:
#             print([i], arr[j])


# time complexity of O(nlogn) for finding the sum by the pair method by two pointers
# arr = [2, 7, 11, 15]
# left, right = 0, len(arr) - 1
# target = 18

# while left < right:
#     current_sum = arr[left] + arr[right]
#     if current_sum == target:
#         print([left+1, right+1])
#     elif current_sum < target:
#         left += 1
#     else:
#         right -= 1
#         print("-1, -1")




