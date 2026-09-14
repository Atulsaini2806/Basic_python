# Dictionary are used to store data in key-value pair. 
# It is a collection which is ordered, changeable(mutuable) and does not allow duplicates.

# example 1
dict = {
    "name": "Atul",
    "age": 22,
    "college": "MIET",
    "branch": "CSE",
    "marks": [70, 85, 65, 45.6],
    "subject": {"DAA", "DBMS", "OS", "OOPS","ML", "CN"}
}
print(dict)

# we can also store a list and tuple in any dictionary in the form of key-value pair.
# we can make or use any data type as key but mostly we used a string as a key in dicionary.

# accessing the value of any key
print(dict["name"]) # Atul 
print(dict["age"]) # 22
print(dict["marks"]) # [70, 85, 65, 45.6]

dict["surname"] = "Saini" # add a new key-value pair
print(dict)


# example 2
dict2 = {
    "name": "Ujjwal",
    "age": 23,
    "college": "CORE",
    "branch": "DS",
    "marks": [75, 80, 90, 95],
}
print(dict2)

# mututable features of dictionary :- we can change the value of any key in dictionary.
dict2["name"] = "Vansh"
print(dict2) # change the value of name key


# Dictionary methods :- there are many methods available in dictionary to perform different operations. Some of the most commonly used methods are:
print(dict2.keys()) # returns a list of all the keys in the dictionary as a tuple.
print(dict2.values()) # returns a list of all the values in the dictionary as a tuple.
print(dict2.items()) # returns a list of all the key-value pairs in the dictionary as a tuple.
print(dict2.get("name")) # returns the value of the specified key.
print(dict2.get("age"))
# Mainly get method are used for the nested dictionary


# Nested Dictionary :- We can also create a dictionary inside a dictionary. This is called nested dictionary.

student = {
    "name": "Rahul Kumar",
    "age": 22,
    "subjects": {
        "physics": 85,
        "chemistry": 90,
        "maths": 95
    }
}
print(student) 
print(student["subjects"]) # return all subjects marks.
print(student["subjects"]["physics"]) # return only physics marks 85
