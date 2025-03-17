'''
A sports analytics team is analyzing the scores of players in a tournament. 
They want to find the second-best and second-worst scores to evaluate performance trends.

Input:
First line contains an integer N (2 ≤ N ≤ 1000), the number of players.
Second line contains N space-separated integers representing scores (0 ≤ score ≤ 10⁶).

Output:
Print the second smallest and second largest element space-separated.

Example:
Input:  
6  
12 35 1 10 34 1  

Output:  
10 34

Example:
Input:  
6  
12 35 0 1 34 3  

Output:  
1 34
'''
N = int(input())
arr = list(map(int, input().split()))[:N]

min = arr[0]
max = arr[0]

for num in arr:
    if num < min:
        min = num
    if num > max:
        max = num
second_max = max
second_min = 0
for num in arr:
    if num < max:
        second_max = num
    if num > min:
        second_min = num

    

print(f"{min} {max}")
print(f"{second_max} {second_min}")
    
