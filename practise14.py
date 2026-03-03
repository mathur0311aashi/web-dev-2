# Q. to find the repeating number and write it 1 time in new array along with the missing number
arr = [3, 1, 3]
count = 0
found = False
for i in range(0, len(arr)):
    for j in range(i+1, len(arr)):
        if arr[i] == arr[j]:
            count += 1
            found = True
            if count >= 1:
                print(arr[i])
                break
    if found:
        break
if not found:
    print("no repeating number")    
            