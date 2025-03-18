'''
A radio station is analyzing unique song requests from listeners. Some songs 
are requested multiple times, while others are played only once. The station 
wants to find songs that were requested just once.

Input:
● First line contains an integer N (1 ≤ N ≤ 1000).
● Second line contains N space-separated integers representing song request IDs.

Output:
● Print all non-repeating elements in ascending order.
● If no unique element exists, print -1.

Example:
Input:  
7  
5 3 9 3 5 7 8  

Output:  
7 8 9
'''

N = int(input())
arr = list(map(int, input().split()))[:N]

def non_dupe(arr):
    freq = {}
    for num in arr:
        freq[num] = freq.get(num, 0) + 1
    
    # Find numbers that appear exactly once
    non_repeating = []
    for num in freq:
        if freq[num] == 1:
            non_repeating.append(num)
    
    # If no unique element exists, return [-1]
    if len(non_repeating) == 0:
        return [-1]
    
    # Return unique elements in ascending order
    non_repeating.sort()
    return non_repeating

print(*non_dupe(arr))


