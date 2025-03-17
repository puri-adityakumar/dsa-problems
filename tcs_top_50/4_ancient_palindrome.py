'''
An ancient manuscript contains secret numerical codes, and the archaeologists suspect that 
palindromic numbers hold hidden meanings. They need a tool to identify whether a given number 
is a palindrome or not.

Input:
A single integer N (1 ≤ N ≤ 10⁶).

Output:
Print "YES" if the number is a palindrome, otherwise print "NO".

Example:
Input:  
1221  

Output:  
YES  

Input:  
123  

Output:  
NO
'''

N = int(input())
o = N
r = 0

while N > 0:
    d = N % 10
    r = r * 10 + d
    N = N // 10

if o == r:
    print("YES")
else:
    print("NO")