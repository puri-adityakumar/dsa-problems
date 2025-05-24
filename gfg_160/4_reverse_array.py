# https://www.geeksforgeeks.org/batch/gfg-160-problems/track/arrays-gfg-160/problem/rotate-array-by-n-elements-1587115621

class Solution:
    def rotateArr(self, arr, d):
        n = len(arr)
        d = d % n
        
        arr[:] = arr[d:] + arr[:d]

        return arr  