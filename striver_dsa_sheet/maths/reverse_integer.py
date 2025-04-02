# https://leetcode.com/problems/reverse-integer/

class Solution:
    def reverse(self, x: int) -> int:
        rev = 0
        sign = -1 if x < 0 else 1
        x = abs(x)

        while x != 0:
            rev = rev * 10 + x % 10
            x //= 10

        if rev < (-2 ** 31) or rev > (2 ** 31) - 1:
            return 0

        return sign * rev


# Testing the function
solution = Solution()

test_cases = [120, 123, -123, 0, 1534236469, -2147483648]
expected_outputs = [21, 321, -321, 0, 0, 0]

for i, test in enumerate(test_cases):
    result = solution.reverse(test)
    print(
        f"Test case {test}: Output = {result}, Expected = {expected_outputs[i]}, Pass = {result == expected_outputs[i]}")
