'''
A grocery store management system maintains a list of products. A new product 
is introduced, and it needs to be added at a specific position in the inventory list.
Write a program to insert an element at a specified index in an Inventory.

Input:
● First line contains two integers N (1 ≤ N ≤ 1000) and X, the new element.
● Second line contains N space-separated integers representing existing products.
● Third line contains an integer P (0 ≤ P ≤ N), the position to insert X.

Output:
Print the new array after insertion.

Example:
Input:  
5 99  
10 20 30 40 50  
2  

Output:  
10 20 99 30 40 50
'''

input_arr = list(map(int, input().split()))[:2]
N = input_arr[0]
element = input_arr[1]
arr = list(map(int, input().split()))[:N]
index = int(input())

# time complexity = O(n) -> element shift  
# space complexity = o(1) -> no extra space needed
def insert_element(element, arr, index):
    arr.insert(index, element)
    return arr

print(*insert_element(element, arr, index))