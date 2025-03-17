'''
A space research team is identifying symmetrical asteroids whose ID numbers are palindromes. 
They need a program to find all palindromic numbers in a given range.

Input:
Two integers L and R (1 ≤ L ≤ R ≤ 10⁶).

Output:
Print all palindrome numbers in the range L to R, space-separated.

Example:
Input:  
10 50  

Output:  
11 22 33 44
'''

arr = list(map(int, input().split()))[:2]

L = arr[0]
R = arr[1]

def palindrome(L,R):
    list_arr = []
    
    for num in range(L,R+1):
        r = 0
        o = num
        while num > 0:
            d = num % 10
            r = r * 10 + d
            num = num // 10
        
        if o == r:
            list_arr.append(o)
    return list_arr

print(*palindrome(L,R))

