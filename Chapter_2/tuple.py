# Tuple is an immutable data structure in Python that can hold a collection of items. 
# It is similar to a list, but unlike lists, tuples cannot be modified after they are created. 
# Tuples are defined by enclosing the items in parentheses `()` and separating them with commas.
# Tuples allow duplicate elements.

tuple = (70, 85, 65, "atul", 45.6, "apnacollage", (1, 2, 3))
print(type(tuple)) # <class 'tuple'>
print(len(tuple)) # 7
print(tuple[0]) # 70
print(tuple[3]) # atul
print(tuple[-1]) # (1, 2, 3)
print(tuple[6]) # (1, 2, 3)


# Note:- if we want write only one element in tuple then we have to use comma after that element otherwise 
         # it will be consider as a string or int.
tuple1 = (70,) # tuple with one element
print(type(tuple1)) # <class 'tuple'>

tuple2 = (70) # not a tuple, it's an int
print(type(tuple2)) # <class 'int'>


# tuple slicing :- similar to string slicing, we can also slice tuples in Python.
tuple3 = (15, 22, 32, 14, 45)
print(tuple3[2:5]) # (32, 14, 45)
print(tuple3[3:]) # (14, 45)
print(tuple3[:5]) # (15, 22, 32, 14, 45)
print(tuple3[-1:]) # (45)
print(tuple3[-5:-2]) # (15, 22, 32)



# if we want to change the value of a tuple we can not do that directly because tuple is immutable. 
# but we can convert the tuple into a list, change the value and then convert it back to a tuple.
tuple4 = (1, 2, 3, 4, 5)
converted_list = list(tuple4) # convert tuple to list
converted_list[2] = 15 # change the value at index 2
print(converted_list) # [1, 2, 15, 4, 5]
