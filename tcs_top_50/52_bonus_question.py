# TCS NQT 15-3-25 

'''
Problem Statement:
You are given three integers P, Q, and R. You can perform the following operation any number of times:
- Select any two numbers and increase both by 1.
- Decrease the third number by 1.
Your task is to determine the minimum number of operations required to make all three numbers equal.

Examples:
Input: 
4 <- number of test cases
1 2 3
4 4 4
3 2 6
1 1 7

Output:
-1
0
-1
3
'''

def min_operations_to_make_equal(p, q, r):
    """
    Calculate minimum operations to make three integers equal.
    Returns -1 if it's impossible.
    """
    # If all numbers are already equal
    if p == q == r:
        return 0
        
    # Calculate the sum and target
    total = p + q + r
    
    # For all numbers to be equal, the final sum must be divisible by 3
    if total % 3 != 0:
        return -1
    
    target = total // 3
    
    # Calculate differences from target
    diff = [p - target, q - target, r - target]
    
    # Count positive and negative differences
    pos = sum(1 for d in diff if d > 0)
    neg = sum(1 for d in diff if d < 0)
    
    # If all differences are positive or all negative, impossible
    if pos == 3 or neg == 3:
        return -1
    
    # Calculate operations needed
    return sum(abs(d) for d in diff) // 2

# Read all inputs at once
t = int(input())  # Number of test cases

results = []
for _ in range(t):
    p, q, r = map(int, input().split())
    results.append(min_operations_to_make_equal(p, q, r))

# Print all results
for result in results:
    print(result)