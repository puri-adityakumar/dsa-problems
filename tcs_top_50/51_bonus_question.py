# was asked in TCS NQT 15-03-25

'''
Stock Price Range Analysis

Problem Statement:
Financial analytics firm RangeSum Capital specializes in analyzing stock performance across different timeframes. They need a program to quickly calculate the sum of stock values within specific date ranges to identify market trends.

Given multiple time periods represented as ranges, calculate the sum of all stock values within each range.

Input Format:
The input consists of one or more range specifications in the format (start,end), where start and end are integers representing days in a financial period.

For example, the input (1,5)(2,8)(10,15) represents three separate ranges to analyze:
- Days 1 through 5
- Days 2 through 8
- Days 10 through 15

Output Format:
For each range, output the sum of all values within that range (inclusive) on a separate line, using the format:
Sum of range [start] to [end]: [sum]

Constraints:
- Range bounds will be positive integers
- Multiple ranges may be provided in a single input
- There are no spaces within the input string
- Each range is enclosed in parentheses

Examples:
Example 1
Input: (1,5)
Output: Sum of range 1 to 5: 15

Example 2
Input: (1,5)(2,5)
Output:
Sum of range 1 to 5: 15
Sum of range 2 to 5: 14

Example 3
Input: (1,10)(5,15)(20,25)
Output:
Sum of range 1 to 10: 55
Sum of range 5 to 15: 110
Sum of range 20 to 25: 135

Explanation:
In Example 1, the sum of integers from 1 to 5 is 1 + 2 + 3 + 4 + 5 = 15.
In Example 2:
- First range (1,5): 1 + 2 + 3 + 4 + 5 = 15
- Second range (2,5): 2 + 3 + 4 + 5 = 14

Challenge:
Implement a solution that efficiently handles multiple range inputs and calculates their sums correctly.
'''

def calculate_range_sum(start, end):
    """Calculate the sum of integers from start to end (inclusive)."""
    return sum(range(start, end + 1))

def parse_ranges(input_string):
    """Extract all ranges from the input string."""
    ranges = []
    i = 0
    
    while i < len(input_string):
        if input_string[i] == '(':
            # Find the closing parenthesis
            j = input_string.find(')', i)
            if j != -1:
                # Extract the range string and split into start and end
                range_str = input_string[i+1:j]
                if ',' in range_str:
                    start, end = map(int, range_str.split(','))
                    ranges.append((start, end))
                i = j + 1
            else:
                i += 1
        else:
            i += 1
    
    return ranges

def main():
    # Get input from user
    input_string = input("Enter one or more ranges (e.g., (1,5)(2,7)): ")
    
    # Parse ranges
    ranges = parse_ranges(input_string)
    
    # Calculate and print results
    for start, end in ranges:
        range_sum = calculate_range_sum(start, end)
        print(f"Sum of range {start} to {end}: {range_sum}")

if __name__ == "__main__":
    main()