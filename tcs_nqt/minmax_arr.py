def minmax(arr):
    min = arr[0]
    max = arr[0]
    
    for num in arr:
        if num > max:
            max = num
        if num < min:
            min = num
    return f"{min} {max}"

def min_max(arr):
    return f"{min(arr)} {max(arr)}" # One line solution using min & max function

arr = [3,5,1,6,2,8]

# print(minmax(arr))
print(min_max(arr))
            