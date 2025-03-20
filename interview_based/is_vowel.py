'''
    Counts the number of vowels and consonants in a given string.

    A vowel is one of: 'A, E, I, O, U' (both uppercase and lowercase).
    A consonant is any alphabetic character that is not a vowel.
    Non-alphabetic characters (spaces, digits, punctuation) are ignored.

    Parameters:
    s (str): The input string.

    Returns:
    tuple: A tuple containing (vowel_count, consonant_count).

    Example:
    --------
    > count_vowels_and_consonants("Hello, World!")
    (3, 7)

    Constraints:
    ------------
    - The input string may contain letters (A-Z, a-z), digits (0-9), spaces, and special characters.
    - The function is case-insensitive.
    - The function should only count English alphabetic characters.
'''

def count_vowel(str):
    vowel = "aeiouAEIOU"
    count_vowels = 0
    count_consonants = 0
    
    for char in str:
        if char.isalpha():
            if char in vowel:
                count_vowels += 1
            else:
                count_consonants += 1
    return  count_vowels, count_consonants

s = "Hello bitcc!"
print(count_vowel(s))   
