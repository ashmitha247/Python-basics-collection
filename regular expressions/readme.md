# What is a Regular Expression?
A regular expression (often abbreviated as regex or regexp) is a sequence of characters that forms a search pattern.
It is used for string searching and manipulation, allowing you to match, search, and replace text based on specific patterns.
Regular expressions are widely used in programming, data validation, text processing, and more.

# classification:
In regular expressions (regex), characters can be classified into two main categories:
a) literal characters
b) meta characters

## literal characters: 
Literal characters are the characters that match themselves exactly. For example, if you use the character a in a regex pattern, it will match the character a in the input string. Literal characters include:

Letters (e.g., a, b, c, A, B, C, etc.)
Digits (e.g., 0, 1, 2, ..., 9)
Special characters that are not used as meta characters (e.g., @, #, $, etc.)
For example, the regex pattern cat will match the string "cat" exactly.

## Meta characters:
They are used to define patterns and control the matching behavior.

In Python, the "re" module provides support for working with regular expressions.
Here are five commonly used meta characters in regex:

1) Dot("."):
            It matches every single character except a newline.
example:

import re

pattern = r"a.b"
text = "acb"
match = re.search(pattern, text)
print(match)  # Output: <re.Match object; span=(0, 3), match='acb'>

2) Caret("^"):
                matches the start of a string

example:

import re

pattern = r"^Hello"
text = "Hello there!"
match = re.search(pattern, text)
print(match)

3) Dollar sign("$"):
                    matcges the end of the string.

example: 

import re

pattern = r"$nice"
text = "that's nice"
match = re.search(pattern,text)
print(match)

4) Brackets("[]"):
                When you use brackets, you can specify a group of characters, and the regex will match any single character from that group.
example:

import re


pattern=r"[aeiou"]
text = "hello"
match = re.findall(pattern,text)
print(match)

5) ("\d"):

\d: This is a meta character in regex that matches any digit. It is equivalent to the character class [0-9], meaning it will match any single digit from 0 to 9.



# regex functions:
- re.match()
- re.search()
- re.fullmatch()
- re.sub()
