'''
A meteorological department is tracking the highest recorded temperatures across different cities. 
To analyze global warming trends, they need to determine the maximum temperature from a given dataset.

Write a program that finds the highest temperature recorded in a given list.

Input:
First line contains an integer N (1 ≤ N ≤ 1000), the number of cities.
Second line contains N space-separated integers representing temperatures (−100 ≤ temp ≤ 100).

Output:
Print the highest temperature recorded.

Example:
Input:  
4  
-5 23 19 30  

Output:  
30
'''

N = int(input())
arr = list(map(int, input().split()))[:N]


def fin_max(arr):
    return max(arr)

print(fin_max(arr))
