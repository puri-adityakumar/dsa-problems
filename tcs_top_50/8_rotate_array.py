'''
A conveyor belt system at an airport needs to cycle luggage handling, shifting each piece 
K positions left to optimize distribution. Write a program that rotates an array left by K 
positions using the Block Swap Algorithm.

Input:
First line contains two integers N (1 ≤ N ≤ 1000) and K (0 ≤ K ≤ N).
Second line contains N space-separated integers representing luggage IDs.

Output:
Print the rotated array.

Example:
Input:  
5 2  
10 20 30 40 50  

Output:  
30 40 50 10 20
'''

arr1 = list(map(int, input().split()))[:2]
N = arr1[0]
K = arr1[1]
arr = list(map(int, input().split()))[:N]

def logic(N,K, arr):
    new_arr = []
    for i in range(K, N):
        new_arr.append(arr[i])
    for i in range(K):
        new_arr.append(arr[i])
    return new_arr

print(*logic(N, K, arr))