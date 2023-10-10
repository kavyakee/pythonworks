# LAMBDA FUNCTIONS
# def,function name, (),return these r not needed.
def add(n1,n2):
    return(n1+n2)
print(add(10,30))

# In Lambda
add_two= lambda n1,n2: n1+n2
print(add_two(10,30))

# square of a number
square=lambda n: n**2
print(square(4))

# cube of a number
cube= lambda n: n**3
print(cube(5))

# largest of a number
max=lambda n1,n2: n1 if n1>n2 else n2
print(max(10,20))

# smallest of 2 nos
min=lambda n1,n2: n1 if n1<n2 else n2
print(min(40,90))



# To print the longest word
text=" hi hello hai gudafternoon"
words=text.split(" ")
# l_word=max(words)                it will print the max word using ascii formulas a<b b<c c<d........
l_word=max(words,key=lambda w:len(w))
print(l_word)

# to sort the keywords
text=" hi hello hai gudafternoon"
words=text.split(" ")
srt=sorted(words,reverse=True,key=lambda w:len(w))
print(srt)
