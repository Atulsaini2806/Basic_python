# Set is a collection of unordered items.(no chnage or no indexing) and represent in {}.
# Each element in the set muet be unique and immutable.
# set = mutuable
# set -> element -> immutable

set1 = {1,2,3,4,5,6 }
set2 = {1,2,2,3,3,"hello", "hello","bye"}
print(set1) # {1, 2, 3, 4, 5, 6}
print(type(set1)) # <class 'set'>
print(set2) # {1, 2, 3, 'bye', 'hello'} return set without duplicate element.


collection = {} #empty dictionary
print(type (collection)) #<class 'dict'> 

collection1 = set() # empty set
print(type(collection1)) # <class 'set'>



# set mwthods:-
# example 1
set3 = {1,2,3,4,5}
set3.add(6) # add an element to the set
print(set3)

set3.remove(3) # remove an element from the set
print(set3)

set3.pop() # remove any random element from the set.
print(set3)


# example 2
set4 = {1,2,3}
set4.add("hello")
set4.add("atul")
set4.add((4,5,6)) # add a tuple to a list
#set4.add([4,5,6]) # add a list to the set ,it will give an error.
print(set4) # {1, 2, 3, 'hello'}

#Note:-
# we can add any immutable element(like- string, tuple) in a set.
# But we can not add any mutuable element(like- list, dict) in a set.


# Union and Intersection of sets:-
set5 = {1,2,3,4,5}
set6 = {4,5,6,7,8}

# Union
union_set = set5.union(set6)
print(union_set) # {1, 2, 3, 4, 5, 6, 7, 8}

# Intersection
intersection_set = set5.intersection(set6)
print(intersection_set) # {4, 5}


# practice question
# figure out a way to store 9 and 9.0 as separate elements in a set.
set7 = {9, 9.0}
print(set7) # {9}

# fisrt method: we can store 9 and 9.0 as separate elements in a set by converting 9.0 into string.
values = {9,"9.0"}
print(values) # {9, '9.0'}

# second method: we can store 9 and 9.0 as separate elements in a set by converting 9 into float.

value = {
    ("int", 9),
    ("float", 9.0)
}
print(value) # {('int', 9), ('float', 9.0)}