'''
The Treasure Hunt Challenge

In the ancient city of Numerica, a grand treasure hunt is organized every year. This year, the challenge is tougher than ever! 
Participants are given a map with multiple treasure chests, each containing a different amount of gold coins.
Your task is to find the treasure chest with the maximum number of gold coins to claim the grand prize.

Rules of the Treasure Hunt:
- You will be given an array of integers, where each integer represents the number of gold coins in a treasure chest.
- You must determine the chest with the highest amount of gold and report the number of gold coins in it.

Input Format:
- The first line contains an integer N (1 ≤ N ≤ 10^6), representing the number of treasure chests.
- The second line contains N space-separated integers, where each integer represents the number of gold coins in a treasure chest.

Output Format:
Print a single integer, the maximum number of gold coins found in any chest.

Example 1:
Input:
5
12 45 78 23 56

Output:
78

Explanation:
Among the five chests, the one with 78 gold coins has the highest value.
'''

# inputs
N = int(input())
arr = list(map(int, input().split()))[:N]

def findmax(arr):
    return max(arr)

print(findmax(arr))