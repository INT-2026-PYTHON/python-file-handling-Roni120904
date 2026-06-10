"""
## 2. Alphabets That Never Appear Back-to-Back  *(Medium)*

=================================================
ALPHABETS NEVER IN SEQUENCE
=================================================

Problem Statement:
Read the text file `sowpods.txt` and PRINT
every alphabet letter that:
   - APPEARS at least once in the words of
     the file, AND
   - NEVER appears TWICE IN A ROW (back-to-back)
     in ANY word of the file.

Letters that never appear in the file at all
should NOT be in the answer. Letters that
appear back-to-back at least once (like the
'u' in "vacuum") should also be excluded.

-------------------------------------------------
Input Example (sowpods.txt sample):
aardvark
hello
buzz
moon
puppy

Output Example:
Letters that never appear back-to-back:
['b', 'd', 'e', 'h', 'k', 'm', 'n', 'r', 'u', 'v', 'y']

-------------------------------------------------
Explanation:
Letters seen anywhere in the sample:
   aardvark -> a, r, d, v, k
   hello    -> h, e, l, o
   buzz     -> b, u, z
   moon     -> m, o, n
   puppy    -> p, u, y
   seen    = {a, b, d, e, h, k, l, m, n, o,
              p, r, u, v, y, z}

Letters that ever appear back-to-back:
   aa (aardvark), ll (hello), zz (buzz),
   oo (moon),     pp (puppy)
   doubled = {a, l, z, o, p}

Answer = seen - doubled
       = {b, d, e, h, k, m, n, r, u, v, y}
Sorted -> ['b', 'd', 'e', 'h', 'k', 'm', 'n',
           'r', 'u', 'v', 'y']
=================================================

"""
def letters_never_back_to_back():
    seen = set() #set rejects duplicates
    doubled = set()

    file = open("file_reading_practice/sowpods.txt", "r") #r means read mode, it can read the contents

    for word in file:
        word = word.strip().lower() #strip removes all spaces,tabs,line change

        for letter in word:
            if letter.isalpha(): #for this problem,this line is optional
                seen.add(letter)

        for i in range(len(word) - 1):
            if word[i] == word[i + 1] and word[i].isalpha():
                doubled.add(word[i])

    file.close()

    print(f"Letters that never appear back-to-back:\n{sorted(seen - doubled)}")

letters_never_back_to_back()