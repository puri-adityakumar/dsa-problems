# method: 1


'''

def find_freq(arr):
    
    for i in arr:
        freq[i] = freq.get(i,0) + 1
    return freq
    
freq ={}  
arr = [1,5,1,2,3,3,5,3]
find_freq(arr) 
for key, value in freq.items():
        print(f"{key} {value}")
        
'''

# method : 2

from collections import Counter

arr = [1,5,1,2,3,3,5,3]

frequency = Counter(arr)
for key, value in frequency.items():
        print(f"{key} {value}")
