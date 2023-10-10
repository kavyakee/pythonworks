# DICTIONARY
# {} denoted by single {} 
# no duplicate key allowed.
# no indexing
# insertion order not preserved.
# dictionaryname={"key":"value"}    and key can be called
mobile={"name":"samsung s22","brand":"Samsung","price":"10","colour":"grey"}
print(mobile["name"])
print(mobile["colour"])

# adding a new key value pair
# dictionaryname[new key]="value"
mobile["display"]="amoled"
print(mobile)

# to check a key is present in dictionary or not - to that we use 'in'
# offer
if "offer" in mobile:
    print("present")
else:
    print("not")

# to implement 50 rs (if offer=100, then offer=100+50. if there is no offer then offer=50)
if "offer" in mobile:
    mobile["offer"]=+50
else:
    mobile["offer"]=50
print(mobile)

# find the value of each key(count of each order)
orders=["vegmeals","fishmeals","meatmeals","cb","fb","bb","vegmeals","fishmeals","vb"]
order_count={}                 # to convert to dictionary
# eg; item=vegmeals
for item in orders:       # to check each key,if vegmeals is present=1                                     if again vegmeals comes 1+1=2
    if item in order_count:
        order_count[item]+=1   # if 
    else:
        order_count[item]=1    # if vegmeals is not then it will set vegmeals as key and value as 1.

print(order_count)

# to count the enquiry
enquires=["django","testing","django","bigdata","django","aws","aws","django"]
#center_head
center_head={}
for courses in enquires:
    if courses in center_head:
        center_head[courses]+=1
    else:
        center_head[courses]=1
print(center_head)

# character count
text="carrot"
word_count={}
for ch in text:
    if ch in word_count:
        word_count[ch]+=1
    else:
        word_count[ch]=1
print(word_count)


#text = "hello hai hello hai"   print the word count

text = "hello hai hello hai"
words=text.split(" ")                     # to separate the words from the given text
word_count={}
for word in words:
    if word in word_count:
        word_count[word]+=1
    else:
        word_count[word]=1
print(word_count)

# to print the recursive character(repeated more times)
text="ABCDBBCD"
word_count={}
for ch in text:
    if ch in word_count:
        print(ch,"is frst recursive character")
        break
    else:
        word_count[ch]=1


# DICTIONARY METHODS



# key() - to return the keys
student={"name":"hana","course":"djanjo","placed_at":True,"salary":50000}
for k in student.keys():                     
    print(k)

# values()  - to return values
for v in student.values():
    print(v)

# items() - to return both keys & values
for k,v in student.items():
    print(k,v)

# get() - to pass an existing value 
# print(student["name"])    instead of calling like this we can use 'get' method.
print(student.get("name"))
# using [], when an invalid case occurs, it returns error while 'get' method returns none. using 'get' value will be beneficial.

# pop() - to remove a key     syntax; pop(key)
student.pop("name")
print(student)

# to print the non recursive alphabets.

text="AABCDEEEE"
word_count={}
for ch in text:
    if ch in word_count:
        word_count[ch]+=1
    else:
        word_count[ch]=1
for k,v in word_count.items():           # to get the keys&values.
    if v==1:
        print(k)


# second recursive character

text="ABBCCCDE"
word_count={}
lst=[]                               # list is created to store the repeated values, that means,if A is present then it will return 1, if another A is there it will be stored in the oth index of list....
for ch in text:
    if ch in word_count:
        lst.append(ch)               # to add the repeated character to the list.
    else:
        word_count[ch]=1
print(lst[1])                        # lst[0] represents the frst recursive character, here we wants the second recursive character.

 # method 2

# text="ABBCCCDE"
# lst1=[]
# lst2=[]
# for ch in text:
#     if ch in lst1:
#         lst1.append(ch)
#     else:
#         lst2.append(ch)
# print(lst1[1])



#KANGAROO WORD                 hen can be created from the word chicken

sourse_word="chicken"
target_word="hen"
sourse_wordlst=[]                             
kangaroo_string=""                                   # mainly for targetword
for ch in sourse_word:
    sourse_wordlst.append(ch)                        # to add each characters of chicken to the list
for ch in target_word:                               # to take each word from the target
    if ch in sourse_wordlst:                         # if the ch from hen is exist in chicken
        sourse_wordlst.pop(sourse_wordlst.index(ch)) # the ch h e n will be removed from chicken.
        kangaroo_string+=ch                          # the removed words h e n will be added to kangaroo string
print(kangaroo_string==target_word)                  # if the h e n in kangaroo string & target words are eqaul, then it must be a kangaroo word.

# method2 using dictionary
source_word="decreases"
target_word="dress"
word_count={}
for ch in sourse_word:
    if ch in word_count:
        word_count[ch]+=1
    else:
        word_count[ch]=1
for ch in target_word:
    if ch in word_count and word_count.get(ch)>0:
        word_count[ch]-=1
    else:
        print("not kangaroo")
        break











