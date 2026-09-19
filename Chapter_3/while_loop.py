# loops are used to execute a block of code repeatedly.
# In python we have two type of loop- 
# 1. while loop:- first check the condition and then execute the block of code.
# 2. for loop:- first execute the block of code and then check the condition.

count = 1
while count <= 5:
    print("hello world !") # print hello world 5 times
    count += 1 # increment the value of count by 1 after each iteration

# The variable that we used before any while condition is called iterator variable.
# And when the code run inside a loop first time is called first iteration.
# In this case, the iterator variable is count. The value of the iterator variable is incremented by 1 after each iteration.
# The loop will continue to execute until the condition becomes false.

# prctice question:-
# example 1:- print the numbers from 1 to 20
i = 1
while i <= 20:
    print(i)
    i += 1

# example 2:- print the muktiplication table of number n
i = 1
n = int(input("Enter the number :"))
while i <= 10:
    print(n*i)
    i+=1


# example 3:- search the number x in the given tuple using the while loop
nums = (1,4,9,16,25,36,49,64,81,100)
x = 49
i = 0
while i < len(nums):
    if (nums[i] == x):
        print("found at idx",i)
        break
    else:
         print ("finding")
         i+=1


# break and continue
# break:- used to terminate the loop when encountered.
# example:-
i = 1
while i <= 5:
    print(i) 
    if (i==3):
       break
    i += 1 


# continue:-
nums = (1,4,9,16,25,36,49,64,81,100)
x = 36
for el in nums:
    if(el == x):
        print("num found")
        continue
    else:
        print("num does not exit")
    