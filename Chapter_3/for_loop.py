# for loop are used for sequential traversal for traveresing list,string.tuples.

#example :-
list = [1,2,3,4,5,6]
for el in list:
    print(el)
else:
    print("END")

#example 2:-
str = "apnacollage"
for char in str:
    if(char == 'o'):
        print("O found")
        break
        print(char)

# Search for anumner x in this tuple using for loop
nums = (1,4,9,16,25,36,49,64,81,100)
x = 36
idx = 0
for el in nums:
    if(el == x):
        print("num found", idx)
        idx+1
        break
    else:
        print("num does not exit")  



