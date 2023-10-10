#comparison operators or relational operator which provide true or false(boolean value) as output  => to compare
#n1=6   n2=10
# <      n1<n2  T
# >      n1>n2  F
# <=     n1<=n2 T
# >=     n1>=n2 F
# ==     n1==n2 F
# !=     n1!=n2 T
n1=50
n2=60
print(n1<n2)

# logical operators    to satisfy certain conditions 
# AND  OR  NOT
# X      Y        AND      OR         NOT(X)    NOT(Y)
# True  False     F        T           F          T
# True  True      T        T           F          F
# False True      F        T           T          F
# False False     F        F           T          T


# bitwise operators
# & bitwise and
# | bitwise or
# ^ bitwise xor
# ~ bitwise not
# 1.....9 decimal values to binary values
# 1 & 2 => 0001 &
#          0010     => 0000 = 0

#1 | 2  => 0001 |
#          0010     => 0011 = 3
print(1&2)
print(1|2)

# in python, ~(not) in a special way such that, ~ of a positive number( add 1 and give -sign)
# ~ of a negetive number(subtract 1 and give + sign)
print("bitwise not : ",~1)
print("bitwise not : ",~2)
print("bitwise not : ",~5)
print("bitwise not : ",~-3)
print("bitwise not : ",~-1)
print("bitwise not : ",~-7)
print("bitwise not : ",~0)
