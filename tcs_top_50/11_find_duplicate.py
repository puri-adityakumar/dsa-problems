'''
A social media platform collects usernames for a contest but some users 
accidentally entered their names multiple times. The system needs to filter 
out duplicate entries to ensure fairness.

Input:
● First line contains an integer N (1 ≤ N ≤ 1000).
● Second line contains N space-separated integers representing user IDs.

Output:
● Print the array after removing duplicates while maintaining the original order.

Example:
Input:  
7  
4 5 9 5 4 8 9  

Output:  
4 5 9 8
'''

N = int(input())
arr = list(map(int, input().split()))[:N]

def remove_duplicates(arr):
    if not arr:
        return []
    
    seen = set()  # To track numbers we've seen
    unique_arr = []
    
    for num in arr:
        if num not in seen:
            unique_arr.append(num)
            seen.add(num)
            
    return unique_arr

print(*remove_duplicates(arr))


