# Q. to reverse a string
# s = "geeks"
# rev = ""
# for j in range(len(s)-1, -1, -1):
#         rev += s[j]
# print(rev)

# for 2 pointer method
# s = "geeks"
# s_list = list(s)
# left = 0
# right = len(s)-1
# while left<right:
#     s_list[left], s_list[right] = s_list[right], s_list[left]
#     left += 1
#     right -= 1
#     s = "".join(s_list)
# print(s)


# with stack method
# s = "geeks"
# stack = []
# for i in range(len(s)-1, -1, -1):
#     stack.append(s[i])
#     # rev = ""
# print(stack)


# Q. checking if 2 strings are anagram or not
# normal and long method through loop takes O(n log n) time
s1 = "listens"
s2 = "silent"
sorted_s1 = sorted(s1)
sorted_s2 = sorted(s2)
if sorted_s1 == sorted_s2:
    print("Anagram")
else:
    print("Not anagram")