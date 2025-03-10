'''
    Leetcode: https://leetcode.com/problems/valid-anagram/ 
    
'''


def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    return sorted(s) == sorted(t)

s = "anagram"
t = "angrama"

a = "oyo"
b = "yoyo"

print(isAnagram(s,t))
print(isAnagram(a,b))
        