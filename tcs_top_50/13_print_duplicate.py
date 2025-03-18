'''
A hotel booking system records the room numbers of guests. Due to system issues, 
some guests are assigned the same room multiple times. The hotel wants to identify 
repeated room numbers.

Input:
● First line contains an integer N (1 ≤ N ≤ 1000).
● Second line contains N space-separated integers representing room numbers.

Output:
● Print all repeated room numbers in ascending order.
● If no repetition is found, print -1.

Example:
Input:  
6  
101 102 103 101 104 103  

Output:  
101 103
'''


N = int(input())
arr = list(map(int, input().split()))[:N]


# Time Complexity: O(n log n) where n is the length of array (due to sorting)
# Space Complexity: O(n) for storing the frequency dictionary
def find_duplicate(arr):
    freq = {}
    duplicates = set()
    
    for num in arr:
        freq[num] = freq.get(num, 0) + 1
        if freq[num] >= 2:
            duplicates.add(num)
    result = sorted(list(duplicates))
    
    return result if result else [-1]

print(*find_duplicate(arr))

