'''
Rahul is a software engineer at a logistics company. His team is developing an automated system to track the weights 
of different parcels being shipped. To optimize the packaging process, Rahul needs to identify the lightest parcel 
from a given list of parcel weights.

Write a program to help Rahul that takes an array of integers representing the weights of parcels and finds the 
smallest weight.

Input:
The first line contains an integer N (1 ≤ N ≤ 1000), the number of parcels.
The second line contains N space-separated integers representing the weight of each parcel (1 ≤ weight ≤ 10⁶).

Output:
Print the smallest weight.

Example:
Input:  
5  
34 12 45 22 8  

Output:  
8

'''

N = int(input())
arr = list(map(int, input().split()))[:N]

def fin_min(arr):
    return min(arr)

print(fin_min(arr))
