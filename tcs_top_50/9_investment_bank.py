'''
An investment bank needs to analyze the median stock price over a period to make financial decisions. 
Write a program to help them.

Input:
● First line contains an integer N (1 ≤ N ≤ 1000).
● Second line contains N space-separated integers (sorted in ascending order).

Output:
Print the median value (if N is odd, print the middle element; if even, 
print the average of two middle elements).

Example:
Input:  
5  
10 20 30 40 50  

Output:  
30  

Input:  
6  
10 20 30 40 50 60  

Output:  
35
'''

N = int(input())
arr = list(map(int, input().split()))[:N]

def find_median(N):
    mid = N // 2
    print(mid)
    if N % 2 == 0:
        return ((arr[mid] + arr[mid+1]) // 2)
    else:
        return arr[mid]
    
print(find_median(N))