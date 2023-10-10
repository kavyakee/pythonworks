#string is a sequance of characters.
name='ka1vyak'
print(name.casefold())       # to convert to lowercase(full)
print(name.capitalize())     # to covert to capital letters only frst one.

print(name.count('a'))       # to print the count of a particular character.
print(name.index('v'))       # to print the position(frst occurance) of a particular character.
print(name.strip('ya'))      # to remove a particular character either from left side or right side not from middle.
print(name.rstrip('k'))      # to remove a particular character from right side.
print(name.lstrip('k'))      # to remove a particular character from left side.
print(name.isalpha())        # to check whether the given string contains alphabets or not. if it is, the it print true or false.
print(name.isdigit())        # to check the digits
print(name.isalnum())        # digit & alphabets
name="python is a programming language"
words=name.split(" ")        # to split the words in string
for w in words:
    print (w)
name="python is a programming language"
words=name.split(" ")     
for words in words:
    if(words[0]=="a" or words[0]=="e" or words[0]=="i" or words[0]=="o" or words[0]=="u"):
        print(words)

#method 2
# text="Python is a programming language"
# words=name.split(" ")
# vowels=("a","e","i","o","u")
# for words in words:
#     if words.casefold().startswith(vowels):    #startwith- to check a particular character in word first word
# print(words)


text="malayalam"
if(text==text[::-1]):
    print("palindrome")
else:
    print("not palindrome")

putt='curry'
curry='kadala'
print(curry)

