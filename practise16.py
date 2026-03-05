# Q. program for wihtout using push
# arr = [1, 3, 7, 0, 0, 4, 6, 8]
# new_arr = []
# arr0 = []
# arr1 = []
# for i in range(0, len(arr)):
#     if arr[i] == 0:
#         arr0.append(arr[i])

#     elif arr[i] != 0:
#         arr1.append(arr[i])
# print(arr1)
# print(arr0)
# new_arr = arr1+arr0
# print(new_arr)


# Q.to find the largest number in the array
# arr = [1, 1, 2, 1, 3, 5, 1]
# freq = {}
# for num in arr:
#     if num in freq:
#         freq[num] += 1
#     else:
#         freq[num] = 1

# max_num = None
# max_count = 0
# for key, value in freq.items():
#     print(f"{key} appears {value} times")

#     if value>max_count:
#         max_count = value
#         max_num = key
# print(f"The largest number is {max_num}   and it appears {max_count} times")



# Q. palindrome new method
# s = "oopmasamajhamasampoo"
# left = 0
# right = len(s)-1
# while left < right:
#     if s[left] != s[right]:
#         print("Not a palindrome")
#         break
#     left += 1
#     right -= 1
# else:
#     print("Is a palindrome")



# Q. FizzBuzz if i % 3 == 0 fizz, if i % 5 == 0 buzz, if i%15==0 fizzbuzz
# for i in range(1, 16):
#     if i%3==0:
#         print("Fizz")
#     elif i%5==0:
#         print("Buzz")
#     elif i%15==0:
#         print("FizzBuzz")
#     else:
#         print(i)

# the other approach for the same program is that you add up the variables varifying with the condition that it is divisible by 3, 5 and 15 eg
# for i in range(1, 21):
#     s = ""
#     if i%3==0:
#         s+="Fizz"
#         elif i%5==0:
#         s+="Buzz"
#     if i%15==0:
#         s="FizzBuzz"
#     print(s or i)


