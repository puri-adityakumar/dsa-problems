# https://www.geeksforgeeks.org/problems/print-gfg-n-times/1

class Solution:
    def printGfg(self, n):
        if n <= 0:
            return
        print("zeke", end=" ")
        self.printGfg(n - 1)


# Test cases
if __name__ == "__main__":
    sol = Solution()

    print("Test Case 1: n = 5")
    sol.printGfg(5)  # Expected output: "zeke zeke zeke zeke zeke"
    print("\n")  # Newline for clarity

    print("Test Case 2: n = 3")
    sol.printGfg(3)  # Expected output: "zeke zeke zeke"
    print("\n")

    print("Test Case 3: n = 1")
    sol.printGfg(1)  # Expected output: "zeke"
    print("\n")

    print("Test Case 4: n = 0")
    sol.printGfg(0)  # Expected output: (nothing, since n is 0)
    print("\n")

    print("Test Case 5: n = -2")
    sol.printGfg(-2)  # Expected output: (nothing, since n is negative)
    print("\n")


