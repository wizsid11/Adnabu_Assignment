##Solution To Assignment
1. The set of all strings of minimum length make up the root.
2. Break the root strings into words and store them in a list(Parent list).
3. Check if the difference between the set of words in strings of length greater than the minimum length and Parent list is greater than 1.
4. If the difference is greater than 1 then break it into words and store it in parent list.
5. We Maintain a dictionary(ans_dict) where we store all the strings as key and their components(words),length of the string and boolean(0 or 1) in the form of a list as values.
6. Whenever we break a string satisfying point 4 into words and store it in the parent list we also change its boolean value from 0 to 1 in the ans dictinary.
7. If the difference is equal to 1 we just break a string into its components and store it in the parent list and don't change its boolean to 1.
8. At last we print all the keys in ans_dict whose boolean is 1.