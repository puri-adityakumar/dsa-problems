# https://leetcode.com/problems/palindrome-number/

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        rev = 0
        y = x

        while y:
            rev = rev * 10 + y % 10
            y //= 10

        return rev == x


# Test cases
def test_isPalindrome():
    solution = Solution()

    # Test Case 1: Positive Palindrome
    assert solution.isPalindrome(121) == True, "Test Case 1 Failed"

    # Test Case 2: Negative Number (not a palindrome)
    assert solution.isPalindrome(-121) == False, "Test Case 2 Failed"

    # Test Case 3: Single Digit (always a palindrome)
    assert solution.isPalindrome(7) == True, "Test Case 3 Failed"

    # Test Case 4: Large Number Palindrome
    assert solution.isPalindrome(12321) == True, "Test Case 4 Failed"

    # Test Case 5: Large Number Non-Palindrome
    assert solution.isPalindrome(123456) == False, "Test Case 5 Failed"

    print("All test cases passed!")


# Run the test cases
test_isPalindrome()
