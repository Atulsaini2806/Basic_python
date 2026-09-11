# list is a built-in data structure in Python that is used to store multiple items in a single variable. 
# Lists are ordered, mutable (changeable), and allow duplicate elements. 
# They are defined by enclosing elements in square brackets [].
# list can store elements of different data types, including integers, strings, floats, and even other lists. that's make it different from the array.


list = [70,85,65,"atul",45.6, "apnacollage", [1, 2, 3]]
print(type(list)) # <class 'list'>
print(len(list)) # 7
print(list[0]) # 70
print(list[3]) # atul


a = ["hello", 51 ,45.5]
print(a[0]) # hello
a[0] = "atul"   # due mutable property
print(a) # ['atul', 51, 45.5]


# slicing :- similar to string slicing, we can also slice lists in Python.
b = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(b[2:5]) # [3, 4, 5]
print(b[3:]) # [4, 5, 6, 7, 8, 9]
print(b[:5]) # [1, 2, 3, 4, 5]
print(b[-1:]) # [9]
print(b[-5:-2]) # [5, 6, 7]


# list specific methods
list1 = [1, 2, 3, 4, 5]
list1.append(6)  # adds an element to the end of the list
print(list1)  # [1, 2, 3, 4, 5, 6]

list1.insert(2, 10)  # inserts an element at a specific index
print(list1)  # [1, 2, 10, 3, 4, 5, 6]

list1.remove(3)  # removes the first occurrence of an element
print(list1)  # [1, 2, 10, 4, 5, 6]

list1.pop()  # removes and returns the last element of the list
print(list1)  # [1, 2, 10, 4, 5]

list1.pop(2)  # removes and returns the element at a specific index
print(list1)  # [1, 2, 4, 5]

list1.sort()  # sorts the elements of the list in ascending order
print(list1)  # [1, 2, 4, 5, 10]

list1.sort(reverse=True)  # sorts the elements of the list in descending order
print(list1)  # [10, 5, 4, 2, 1]