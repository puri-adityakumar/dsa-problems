# https://www.geeksforgeeks.org/problems/sum-of-all-divisors-from-1-to-n4738/1

def sumOfDivisors(n):
    # count = 0
    # for j in range(1, n+1):
    # 	sum = 0 
    #     for i in range(1, j+1):
    #         if j % i == 0:
    #             sum = sum + i
    #     count = count + sum
    # return count             

    if n <= 0:
        return 0
    div_sum = 0

    for i in range(1, n + 1):
        k = n // i
        div_sum += i * k

    return div_sum