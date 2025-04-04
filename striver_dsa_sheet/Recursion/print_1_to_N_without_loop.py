# https://www.geeksforgeeks.org/problems/print-1-to-n-without-using-loops-1587115620/1

class Solution:
    def printNos(self, n):
        if n == 0:
            return
        self.printNos(n - 1)  # Recursive call
        print(n, end=" ")  # Print after the recursive call


# Test cases
if __name__ == "__main__":
    sol = Solution()

    print("Test Case 1: n = 5")
    sol.printNos(5)  # Expected output: "1 2 3 4 5"
    print("\n")  # Newline for clarity

    print("Test Case 2: n = 3")
    sol.printNos(3)  # Expected output: "1 2 3"
    print("\n")

    print("Test Case 3: n = 1")
    sol.printNos(1)  # Expected output: "1"
    print("\n")

    print("Test Case 4: n = 0")
    sol.printNos(0)  # Expected output: (nothing, since n is 0)
    print("\n")

    print("Test Case 5: n = -2")
    sol.printNos(-2)  # Expected output: (nothing, since n is negative)
    print("\n")
