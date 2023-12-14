'''
Question :
Given a string consisting of English alphabets, the task is to count the number of adjacent pairs of vowels.
For example :
Input: str = “abaebio”
Output: 2
(a, e) and (i, o) are the only valid pairs.
Source:A very Common Interview Question.

Time Complexity : The goal is to complete this question in O(n).
'''

#function to check whether a character is vowel or not
def is_vowel(character):
    return character.lower() in ['a', 'e', 'i', 'o', 'u']
  

#function to find the number of adjacent vowel pairs.
def adjacent_pairs(string):
    string=string.lower()
    n=len(string)
    return sum(
        1
        for i in range(0, n)
        if ((is_vowel(string[i]) and is_vowel(string[i + 1])))
    )

#driver code
string=input("enter string")
print (adjacent_pairs(string),"is the number of adjacent pairs of vowels")
  
