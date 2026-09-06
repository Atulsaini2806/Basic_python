#  String in Python is a sequence of characters enclosed within single quotes (' ') or double quotes (" ").
#   Strings are immutable, meaning once they are created, they cannot be changed.

str1 = "My name is Atul Saini"
str2 = "apnacollage"

print(str1)
print(type(str1)) # <class 'str'>
print(len(str1)) # 21
# print(str1[0]) # M
# str1[4] = "@"
# print(str1[4]) # TypeError: 'str' object does not support item assignment because strings are immutable in Python.

#slicing
print(str2[3:8]) # acoll
print(str2[3:]) # acollage
print(str2[:8]) # apnacoll


#Negative indexing(always used in slicing)
print(str2[-1:]) # e
print(str2[-8:-3]) # acoll


# check the number is even or odd using string
num_str = int(input("Enter a number: "))
rem = num_str % 2
if rem == 0:
    print("The number is even.")
else:
    print("The number is odd.")