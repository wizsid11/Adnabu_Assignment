##Solution To Assignment
1. The set of all unique strings of minimum length make up the initial root list.
2. We maintain a dictionary of all strings as key and a list containing a boolean(0 or 1),set of words in the string and the length of the string as values.
3. Then we check if the set of words in any of the root string is a subset of set of words in another string.
4. If no we add the string to the list of root strings.

