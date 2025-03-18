'''
A hospital database records patient IDs but due to a system glitch, duplicate IDs were stored. 
The hospital needs a way to remove duplicates. Write a program to remove duplicates from a 
sorted list of patient inventory and print the unique elements.

Input:
● First line contains an integer N (1 ≤ N ≤ 1000).
● Second line contains N space-separated integers (sorted in non-decreasing order).

Output:
Print the array after removing duplicates.

Example:
Input:  
6  
1 1 2 2 3 3  

Output:  
1 2 3
'''


N = int(input())
arr = list(map(int, input().split()))[:N]

# using set: Time: O(n), Space: O(n)
def set_approach(arr):
    my_set = set(arr)
    return my_set

# using two pointer: Time: O(n), Space: O(1)
def two_pointer(arr):
    if not arr:
        return[]
    
    unquie_arr = [ arr[0]]
    for i in range(1, len(arr)):
        if arr[i] != arr[i - 1]:
            unquie_arr.append(arr[i])
    return unquie_arr

print(*two_pointer(arr))