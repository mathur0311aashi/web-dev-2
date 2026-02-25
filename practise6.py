# Write a Python program to divide the first element of a list by the second element of the list and print the result. Do this for two different lists and then add the results together and print the final sum.
# m = [3, 4]
# n = [1, 2]
# sum = 0
# for i in range (0, len(m)-1):
#     c = m[i]/m[i+1]
#     print(c)

# for j in range (0, len(n)-1):
#     d = n[j]/n[j+1]
#     print(d)

# sum = c+d
# print(sum)



# program to find the ans of a^b and the answer as the output of the kth digit entered by the user
# a = 5
# b = 2
# h = 2 
# k = 0
# res= pow(a,b)
# print(res)
# res1 = res%10  
# above function stores the remainder
# print(res1)
# res2 = res//10
# print(res2)
# arr = []
# arr = [res1 , res2]
# print(arr)
# for i in range (1, len(arr)+1):
    # if k == i:
        # print(arr[i])




# for finding the factorial of a number and then uske baad permutation find krne ka tareeka
# n = 5
# r = 2
# k = n-r
# for i in range (1, n):
#     n *= i
# print(n)

# yaha par n ki value ab 120 ho chuki h to agar yaha p k=n-r kroge to 120 ke acc change hoga vice versa pehle hi subtract krke ab kroge to values change hongi
# for j in range (1, k):
#     k *= j
# print(k)

# res = n/k
# print(res)




# for for combination of two numbers
# n = 5
# r = 2
# k = n-r
# for i in range (1, n):
#     n *= i
# print(n)

# for j in range (1, k):
#     k *= j
# print(k)

# for l in range (1, r):
#     r *= l
#     print(r)

# res = n/(k*r)
# print(res)




arr1 = [1, 2, 3]
arr2 = [6, 7]
rels = []
for a in arr1:
    for b in arr2:
        rels.append((a, b))

print(rels)


# also read the important topics of js like addevent, eventlistener, delete wala and remove, clear all cards only read 
