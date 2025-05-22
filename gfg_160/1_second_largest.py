# https://www.geeksforgeeks.org/batch/gfg-160-problems/track/arrays-gfg-160/problem/second-largest3735
class Solution:
    def getSecondLargest(self, arr):
        first = -1
        second = -1
        
        for i in range(len(arr)):
            if arr[i] > first:
                second = first
                first = arr[i]
            elif arr[i] > second and first != arr[i]:
                second = arr[i]
        return second