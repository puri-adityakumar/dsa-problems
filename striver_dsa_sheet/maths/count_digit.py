# https://www.geeksforgeeks.org/problems/count-digits5716/1

def evenlyDivides(n):
    num = n
    count = 0
    while n > 0:
        digit = n % 10
        if digit > 0 and num % digit == 0:
            count += 1
        n = n // 10
    return count

print(evenlyDivides(12))

