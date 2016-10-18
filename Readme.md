##Solution To Assignment
1. The set of all unique strings of minimum length make up the initial root list.
2. We maintain a dictionary of all strings as key and a list containing a boolean(0 or 1),set of words in the string and the length of the string as values.
3. Then we check if the set of words in any of the root string is a subset of set of words in another string.
4. If it is not, we add the string to the list of root strings.

###Solution of a few examples
####Example 1:
#####Input - 
1. hello world python
2. scala world
3. java python scala hello world
4. world python hello
5. world hello
6. python clojure java world

####Output - 
1. world hello
2. scala world
3. python clojure java world 

####Example 2:
#####Input - 
1. hello world python
2. python world
3. python

####Output - 
1. python

####Example 3:
#####Input - 
1. python closure world scala
2. scala world

####Output - 
1. scala world
