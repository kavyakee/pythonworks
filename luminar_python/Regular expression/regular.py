#  REGULAR EXPRESSION
# pattern matching
# eg; mail id
# re.py
# def finditer()      =>
# def group()
# def fullmatch()
# def search()
# def start()

from re import*
text="ababaaabab34A"
#     12345678910
pattern="ab"
pattern="[a-z]"                       # to take lowercase letters
pattern="[A-Z]"                       # to take uppercase letters
pattern="[0-9]"                       # to take numbers 
pattern="[a-zA-Z0-9]"                 # to take lowercase letters,upper& numbers .
pattern="[^a-zA-Z0-9]"                # ^ this is used to exclude (here lower,upper&digits)
pattern="\d"                          # to print numbers  only
pattern="\D"                          # to print except numbers  .
pattern="\w"                          # to print numbers & alphabets(lower&upper)
pattern="\W"                          # to print except numbers & alphabets(lower&upper) ie, special characters.
matcher=finditer(pattern,text) 
for m in matcher:
    print(m.start(),m.group())         # start() is to specify the position from the given string. group() is to specify the given pattern



# to print the vowels.
from re import *
text="goodmorning # sachin"
pattern="[eaiou\W\d]"

matcher=finditer(pattern,text)
for m in matcher:
    print(m.start(),m.group())
