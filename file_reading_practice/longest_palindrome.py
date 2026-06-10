"""
## 5. Longest Palindrome in the File  *(Hard)*

=================================================
LONGEST PALINDROME
=================================================

Problem Statement:
Read the text file `sowpods.txt` and find the
LONGEST PALINDROME word in the file.

If multiple palindromes share the maximum
length, print ALL of them.

-------------------------------------------------
Input Example (sowpods.txt sample):
level
radar
noon
civic
deified
racecar
rotator
malayalam

Output Example:
Longest palindrome length: 9
malayalam

-------------------------------------------------
Explanation:
Lengths of the palindromes in the sample:
   level    -> 5
   radar    -> 5
   noon     -> 4
   civic    -> 5
   deified  -> 7
   racecar  -> 7
   rotator  -> 7
   malayalam -> 9
The longest is "malayalam" with 9 characters.
=================================================

"""

longest_length = 0
longest_palindromes = []

file = open("file_reading_practice/sowpods.txt", "r")

for word in file:
    word = word.strip().lower()

    if word == word[::-1]: # palindrome check

        if len(word) > longest_length:
            longest_length = len(word)
            longest_palindromes = [word]

        elif len(word) == longest_length: #if more than 1 palindrome has same length
            longest_palindromes.append(word)

file.close()

print("Longest palindrome length:", longest_length)

for word in longest_palindromes:
    print(word)