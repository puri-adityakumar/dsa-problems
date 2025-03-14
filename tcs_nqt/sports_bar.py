'''
Vishal has opened a new sports bar. On the very first day, he made the bar free for everyone. There are various pool 
tables which most of the people are interested in and the pool tables are numbered from 1 to K. 
Let's say there are N customers who visited the bar. Each has an entry and exit time. The customers are very specific 
with their pool table, if they get their requested table, then they are going to play, otherwise they will leave. The 
customer will arrive at a table at his entry time and has to leave the table at his exit time. A customer will use only a 
table of his preference. If the customer doesn’t get the specific table of their choice, they won’t take any other table, 
even if it is available. 
Vishal wants most of the customers to join his club, So that they visit again, and his business may flourish. 

Given a list of N customers and K tables, along with their Entry (En[]) and Exit (Ex[]) time and table number T[], find the 
maximum number of customers that can be accommodated in the club. 

Let us understand this with an example:
Let's say N = 3 and K = 3 Entry and Exit and Pool table is given in sequence for each customer. 
Customer 1: 10 100 1 
Means entry time is 10, Exit time is 100, and the table which he prefers is 1. 
Customer 2: 10 50 1 
Means entry time is 10, Exit time is 50, and the table which he prefers is 1. 
Customer 3: 10 100 2 
Means entry time is 10, Exit time is 100, and the table which he prefers is 2. 
As Vishal wants more customers to be accommodated, he will prefer those customers who stay less, so that if anyone else 
comes, they can be easily accommodated. 

So here Customer 2, will be given Table 1. For Table 2 there is no conflict, so Customer 3 easily takes Table 2. 
In this way, we can accommodate a maximum of 2 customers. Hence the answer is 2. 

Example 1: 
Input: 
3 -> Input Integer, N 
3 -> Input Integer, K 
1 3 1 -> Input Integer, En[], Ex[], T[] 
4 6 2 -> Input Integer, En[], Ex[], T[] 
7 10 3 -> Input Integer, En[], Ex[], T[] 

Output: 
3 -> Output 

Explanation: Clearly in the above scenario, there is no conflict among the customers for pool tables, each customer is 
looking for different tables. Hence all the customers can be accommodated here. So the answer is 3. 
'''
