'''
A librarian is digitizing old books and needs to store page numbers in reverse order 
for a historical reference system. Help the librarian reverse the order of a given list of page numbers.

Input:
First line contains an integer N (1 ≤ N ≤ 1000), the number of pages.
Second line contains N space-separated integers representing the page numbers.

Output:
Print the reversed array.

Example:
Input:  
5  
10 20 30 40 50  

Output:  
50 40 30 20 10


'''

N = int(input())
arr = list(map(int, input().split()))[:N]

arr.sort()
arr.reverse()

print(*arr)
