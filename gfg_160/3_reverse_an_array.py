# https://www.geeksforgeeks.org/batch/gfg-160-problems/track/arrays-gfg-160/problem/reverse-an-array

# without library function
class Solution:
    def reverseArray(self, arr):
        
        l, r = 0, len(arr) - 1
        
        while l < r:
            arr[l], arr[r] = arr[r], arr[l]
            l += 1
            r -= 1
        return arr
        
# with using lib function    
class Solution:
    def reverseArray(self, arr):
        arr.reverse()
        return arr
        