# Question Link : https://www.geeksforgeeks.org/problems/second-largest3735/1

class Solution:
    def getSecondLargest(self, arr):
        alpha = -1
        beta = -1
        
        for num in arr:
            if num > alpha:
                beta = alpha
                alpha = num
            elif num > beta and num != alpha:
                beta = num
        return beta

# Testing the code
solution = Solution()
arr = [12, 35, 1, 10, 34, 1]
print(solution.getSecondLargest(arr))  # Output: 34