'''
A package delivery service maintains a record of packages sent and received. 
They want to identify matching sender-receiver pairs where (A, B) exists 
along with (B, A). Write a program to solve this problem.

Input:
● First line contains an integer N (1 ≤ N ≤ 1000), the number of sender-receiver pairs.
● Next N lines contain two space-separated integers representing the sender and receiver IDs.

Output:
Print all symmetric pairs in ascending order of the first ID.

Example:
Input:  
4  
10 20  
20 10  
30 40  
50 60  

Output:  
(10, 20)
'''

N = int(input())

pairs = []
for _ in range(N):
    sender, receiver = map(int, input().split())
    pairs.append((sender, receiver))

# Find symmetric pairs
symmetric = set()
for sender, receiver in pairs:
    # Check if the reverse pair exists
    if (receiver, sender) in pairs:
        # Add the pair with the smaller first element
        symmetric.add((min(sender, receiver), max(sender, receiver)))

# Print results in ascending order
for pair in sorted(symmetric):
    print(f"({pair[0]}, {pair[1]})")
