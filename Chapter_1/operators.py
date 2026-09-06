# Arthmatic operators(+,-,*,/,**,//)
a = 16
b = 5
print(a + b) # 21
print(a - b) # 11
print(a * b) # 80
print(a / b) # 3.2
print(a % b) # reminder 1
print(a ** b) # 1048576


# Relational Operators or comparsion operators(==, !=, >, >=, <, <=)
c = 50
d = 20
print(c == d) # False
print(c != d) # True
print(c > d ) # True
print(c >= d) # True
print(c < d) # False
print(c <= d) # False


# Assignment Opertors(=, +=, -=, *=, /=, %=, **=)
num = 10
num += 10 # num = num + 10
print(num) # 20



# Logical Operators(and, or, not) prsedance: not > and > or

e = 50
d = 20
print(e > 30 and d < 30) # True, both condition should be true
print(e > 30 or d < 50) # True, at least one condition should be true
print(not(True)) # False, negation of the condition
print(not(False)) # True, negation of the condition
