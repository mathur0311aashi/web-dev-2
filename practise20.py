# to check if the number is greater than n/3 or not
# arr = [2, 2, 3, 1, 3, 2, 1, 1]
# count = 0
# for i in range(0, len(arr)):
#     for j in range(i+1, len(arr)):
#         if arr[i] == arr[j]:
#             count += 1
#             if count > len(arr)/3:
#                 print(arr[i])


# arr1 = []
# arr = [1, 5, 8, 10]

# k = 2
# for i in range(0, len(arr)):
#     if len(arr) % 2 == 0:
#         arr1.append(arr[i]-k)
#     else:
#         arr1.append(arr[i]+k)   
 
# arr1 = sorted(arr1)
# # print(arr1)
# print(max(arr1)-min(arr1))



arr = [10, 3, 5, 6, 2]
arr1 = []
# product = 1
for i in range(0, len(arr)-2):
    product = 1
    for j in range(len(arr)-2):
        if i!=j:
            product *= arr[j]
            arr1.append(product)
        print(arr1)