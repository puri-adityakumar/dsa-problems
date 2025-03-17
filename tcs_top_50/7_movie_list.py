'''
A movie streaming platform wants to analyze user preferences by counting 
how many times each movie was watched in a week. Write a program that takes 
an array of movie IDs and counts the frequency of each movie watched.

Input:
First line contains an integer N (1 ≤ N ≤ 1000), the number of watch records.
Second line contains N space-separated integers, each representing a movie ID.

Output:
Print each movie ID along with its count, sorted in ascending order of movie ID.

Example:
Input:  
7  
101 102 101 103 101 102 104  

Output:  
101 3  
102 2  
103 1  
104 1
'''

from collections import Counter
N = int(input())
arr = list(map(int, input().split()))[:N]

frequency = Counter(arr)
for key, value in frequency.items():
        print(f"{key} {value}")
