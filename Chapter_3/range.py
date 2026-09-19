# Range function return a sequence of numbers that is start from 0 by default and increment by 1(by default)
# and stop before a specified number.
# range(start?,stop?,step?), here stoping condition is compulsary other two are optionally.
# starting index is always included but stoping index is not included.
# example 1:- first type :- range(stop)
seq = range(5)
for i in range(5):
    print(i) # 0,1,2,3,4

# or 
for i in range(5):
    print(i) # same output

# second type:- range(start,stop) where start inx is included but stop is not.
for i in range(2,10):
    print(i) # 2,3,4,5,6,7,8,9


# third type :- range(start,stop,step):
for i in range(15,28,2):
    print(i) # 17,19,21,23,25,27
