# https://www.geeksforgeeks.org/problems/sum-of-first-n-terms5843/1


class Solution:
    def sumOfSeries(self, n):
        if n == 1:
            return 1
        else:
            return (n ** 3 + self.sumOfSeries(n - 1))


# Test cases
if __name__ == "__main__":
    sol = Solution()

    print("Test Case 1: n = 3")
    print(sol.sumOfSeries(3))  # Expected output: 1^3 + 2^3 + 3^3 = 1 + 8 + 27 = 36
    print("\n")

    print("Test Case 2: n = 5")
    print(sol.sumOfSeries(5))  # Expected output: 1^3 + 2^3 + 3^3 + 4^3 + 5^3 = 225
    print("\n")

    print("Test Case 3: n = 1")
    print(sol.sumOfSeries(1))  # Expected output: 1^3 = 1
    print("\n")
