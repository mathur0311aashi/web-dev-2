#bubble sort
#in bubble sort we compare adjacent elements and swap them if they are in the wrong order.
#time complexity: O(n^2)
# Space complexity: O(1)

arr = [-5, 3, 2, 1, -3, -3, 7, 2, 2]

def bubble_sort(arr):
    n = len(arr)
    flag = True
    while flag:
        flag = False
        for i in range(1, n):
            if arr[i] < arr[i-1]:
                arr[i], arr[i-1] = arr[i-1], arr[i]
                flag = True
    return arr

print(bubble_sort(arr))



#insertion sort
#in this we start the i loop from index 1 and the other loop j from i in backward direction till 0 to compare all the elements if they are in decreasing order or not and swap them if they are in wrong order. in this 2 sections are handled in this manner and this is how it is different from others.
#time complexity: O(n^2)
# Space complexity: O(1)

arr = [-5, 3, 2, 1, -3, -3, 7, 2, 2]
def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        for j in range(i, 0, -1):  
            # for making the j point move backwards in comparison to i
            if arr[j-1] > arr[j]:
                arr[j-1], arr[j] = arr[j], arr[j-1]
            else:
                break
    return arr

print(insertion_sort(arr))


#Selection sort
#Time complexity: O(n^2)    
#space complexity: O(1)
# in this we actually assume one number as the very smallest and compare it with the rest. and then from i to the end that smallest number is compared with the help of j


arr = [-5, 3, 2, 1, -3, -3, 7, 2, 2]
def selection_sort(arr):
    n = len(arr)
    for i in range(0, n):
        min = i
        for j in range(i+1, n):
            if arr[j] < arr[min]:
                arr[j], arr[min] = arr[min], arr[j]
    return arr

print(selection_sort(arr))



#merge sort
#time complexity: O(Nlog base 2 N)
#space complexity: O(N)


# arr = [-5, 3, 2, 1, -3, -3, 7, 2, 2]
# def merge_sort(arr):
#     n = len(arr)
#     if n <= 1:
#         return arr
#     mid = n//2
#     l_half = arr[ :mid]
#     r_half = arr[mid: ]
#     l_half = merge_sort(l_half)
#     r_half = merge_sort(r_half)
#     return merge(l_half, r_half)

# def merge(l_half, r_half):
#     new = []
#     i, j = 0, 0
#     while i<len(left_half) and j<len(right_half):
#         if left[i]<right[j]:


s = "geeksforgeeks"
p = "ks"
n = len(s)
q = len(p)
count = 0

for i in range(0, n):
    for j in range(0, q):
        while s[i] == p[j]:
            # do something
            count += 1
            if count == q:
                print("found")
            
                print(j)
                

