from re import *
text="aabbaaac"                                          #                                    "aabbaaac" 
pattern="a+"                                             # here a+ means one a or more         01234567             
pattern="a*"
pattern="a{1,2}"                                         # minimum of 1 and maximim of 2    in 0th location 2 a present and in 4th 2(max=2)   6th 1

matcher=finditer(pattern,text)                           # "aabbaaac"
for m in matcher:                                        #  0   4         in 0(aa)       4(aaa)
    print(m.start(),m.group())


#to check a phone no

phone=input("enter phone number")
rule="\d{10}"
matcher=fullmatch(rule,phone)
if matcher==None:                                  # ie,if the number exceeds 10, then the no should be invalid
    print("invalid")
else:
    print("valid")


#to check a variable

variable=input("enter a variable name")
rulee="[a-zA-Z][0-9a-zA-Z]*"
matcher=fullmatch(rulee,variable)
print("invalid" if matcher==None else "valid")

# atleast uppercase
# atleast 1 special characters
# atleast 8 characters.
password="Password@123"
rule="(?=.*[A-Z])(?=.*[\W])(?=.*[\d]).{8,}"
matcher=fullmatch(rule,password)
print("valid " if matcher!= None else "invalid")
    