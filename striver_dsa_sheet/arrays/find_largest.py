from typing import List

class Solution:
    def largest(self, arr: List[int]) -> int:
        max_val = arr[0]
        for i in arr:
            if i > max_val:
                max_val = i
        return max_val

# Instantiate the solution class
sol = Solution()

# Test cases
print("Test Case 1:", "Pass" if sol.largest([3, 5, 7, 2, 8]) == 8 else "Fail")
print("Test Case 2:", "Pass" if sol.largest([-10, -5, -1, -100]) == -1 else "Fail")
print("Test Case 3:", "Pass" if sol.largest([42]) == 42 else "Fail")
