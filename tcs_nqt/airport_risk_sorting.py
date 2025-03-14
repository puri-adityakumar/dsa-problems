'''
Sorting Risk Levels at Airport Security

Airport security officials have confiscated various items at the security checkpoint. 
Each item is assigned a risk severity level, categorized into three levels:
    - 0 → Low risk
    - 1 → Medium risk
    - 2 → High risk

These confiscated items are placed in an unordered list. Your task is to sort the items 
based on their risk severity in ascending order, ensuring that low-risk items come first, 
followed by medium-risk items, and finally high-risk items.

Input Format:
- The first line contains an integer N (1 ≤ N ≤ 10^6), representing the number of confiscated items.
- The next N lines each contain an integer (0, 1, or 2) representing the risk severity level of an item.

Output Format:
- Print the sorted sequence of risk severity levels in a single line, separated by spaces.

Example 1:
Input:
7
1
0
2
1
1
0
2

Output:
0 0 1 1 1 2 2
'''

N = int(input())

arr = []
for num in range(N):
    arr.append(int(input()))

arr.sort()
print(*arr)