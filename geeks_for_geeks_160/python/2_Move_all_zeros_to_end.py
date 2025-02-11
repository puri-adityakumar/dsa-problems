# Question : https://www.geeksforgeeks.org/problems/move-all-zeroes-to-end-of-array0751/1
class Solution:
    def pushZerosToEnd(self,arr):
        
        count = 0
        
        for i in range(len(arr)):
            if arr[i] != 0:
                arr[i], arr[count] = arr[count], arr[i]
                count += 1
        return arr
 
# Testing the code
solution = Solution()
arr = [0, 1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0, 9]
print(solution.pushZerosToEnd(arr))  # Output: [1, 9, 8, 4, 2, 7, 6, 9, 0, 0, 0, 0, 0]