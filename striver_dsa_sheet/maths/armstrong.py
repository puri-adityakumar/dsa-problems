# https://www.geeksforgeeks.org/problems/armstrong-numbers2727/1

def armstrongNumber(n):
    num = n
    sum = 0
    while n > 0:
        digit = n % 10
        sum = sum + (digit ** 3)
        n = n // 10

    return sum == num

print(armstrongNumber(100))