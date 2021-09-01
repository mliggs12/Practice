"""Back to Basics: Strings

str()

Strings are just lists of characters and whitespace.
Learning more about lists will help learn more about strings

str.split(sep, maxsplit) -> list
Return a list of the words in the string, using sep as the delimiter string.

sep The delimiter according which to split the string. None (the default value) means split according to any whitespace, and discard empty strings from the result. maxsplit Maximum number of splits to do. -1 (the default value) means no limit.
"""

string = "!!!!!This is the string that I am going to use for this practice today.!!!!!"

# String methods
# split() method should default to splitting by space
split_string = string.split()
split_string_by_delimiter = string.split(!)

# Prints a list of strings
print(split_string)