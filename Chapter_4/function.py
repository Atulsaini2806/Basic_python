# Function:- Block of statement that perform a specific task.
# function are used remove  the redundancy(repation) in any program.

# syntax:-
# def_funs_name(parameter1,parameter2,.....) # function defination
#   # some work
#   return Value
 
# func_name(arg1,arg2) # function call

def cal_sum(a, b):
    sum = a + b
    print(sum)
    return sum

cal_sum(2, 3) # 5
cal_sum(45, 3) # 48
cal_sum(29, 15) # 44
# Here we do need to write the code for sum again and again, we can only call the function and pass the value as argument.

# Note:- untill we call the function, the code will not execute.


def first_program():
    print("hello wprld!!")

first_program()

# if we do not pass any parameter and argument then also our program will run.

# WAP to find the avg of three numbers
def cal_avg(a,b,c):
    sum = a+b+c
    avg = sum/3
    print("Average:", avg)
    return avg
cal_avg(45,12,21)


# if we want to take the input from the user
def cal_avg(d, e, f):
    sum = d + e + f
    avg = sum / 3
    print("Average:", avg)
    return avg

d = int(input("Enter first number: "))
e = int(input("Enter second number: "))
f = int(input("Enter third number: "))

cal_avg(d, e, f)

