'''
    https://leetcode.com/problems/contains-duplicate
    https://prepinsta.com/top-150-notout-questions/check-if-array-contains-duplicates/
    
'''
from typing import List

def containsDuplicate(nums: List[int]) -> bool:
    hashset = set()
    
    for n in nums:
        if n in hashset:
            return True
        hashset.add(n)
    return False

arr = [1,2,3,4,5]
arr2 = [1,2,2,5]
print(containsDuplicate(arr))
print(containsDuplicate(arr2))
