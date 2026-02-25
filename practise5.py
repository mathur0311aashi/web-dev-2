# for greatest common factor of two numbers
n = 6
k = 8
arr1 = []
arr2 = []
arr = []
for i in range (1, n+1):
    if n % i == 0:
        print("the factor of n is", i)
        arr1.append(i)

        for j in range (1, k+1):
            if k % j == 0:
                print("the factor of k is", j)
                arr2.append(j)
arr = arr1+arr2
print(arr)

print(max(arr))

# if i == j:
#     print("the common factor of n and k is", i)

# for heighest common factor of two numbers

