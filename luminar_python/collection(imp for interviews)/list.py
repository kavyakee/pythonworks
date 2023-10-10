#LIST
#list  - defined in []
# insertion order preserved
# duplication allowed
# mutable(can be updated)

#list prgrms
# print frst 3 malayalam movies
films=["vikathakumaran","marthandavarma","balan","nirmala"]
print(films[0])         # to print the 1st film
for f in films:
    print(f)


# to print the expenses
expenses=[12000,13000,14000,1100,22000,34000,89000]
print(expenses[2])
for e in expenses:
    print(e)
print(expenses[5])
print(expenses[6])
# to print maximum expenses

max_exp=0
for e in expenses:
    if e>max_exp:
        max_exp=e
print(max_exp)

#to print minimum expense

min_exp=expenses[0]             
for e in expenses:
    if e<min_exp:
        min_exp=e
print(min_exp)


#OTHER FUNCTIONS

#sum()- to sum numbers
#min()- to have the min of nos
#max()- to have the max of numbers
#sorted()- to sort thr numbers
sort=sorted(expenses)
ascending_sort=sorted(expenses,reverse=False)      # to print the list in ascending order
print(ascending_sort)
descending_sort=sorted(expenses,reverse=True)      # to print the list in descending order
print(descending_sort)

# to print expenses>16000

for e in expenses:
    if e>16000:
     print(e)


     #LIST METHODS
#append()- to add a new object to a list.
users=["mohanlal","mammotty","nivin","dq"," ","unni","unni"]
#add new object to list
users.append("sreenivasan")
print(users)
#pop()- to remove an object from list
users.pop(3)
print(users)
#index(" ") - to know the position of an object in a list.
print(users.index("unni"))
#count() - to know the no of occurance of an object in a list.
print(users.count("unni"))
#sort() - to sort the list.
users.sort()
print(users)
# to sort in descending order
users.sort(reverse=True)
print(users)
#clear() - to clear all the objects in the list
users.clear()
print(users)

users=["mohanlal","mammotty","nivin","dq"," ","unni","unni"]
#in ()- to check whether an object present in the list or not
if ("asif ali" in users):
    print("present")
else:
    print("not")
#not in() - not in
if ("asif ali" not in users):
    print("valid")
else:
    print("invalid")

# prblm 
bts=["v",
     "jimin",
     "jin",
     "rm",
     "jhope",
     "yoongi"]
jungkook_hyungs=["rm","jhope","yoongi"]
#list suggestions for jungkook
for p in bts:
    if p not in jungkook_hyungs:
        print(p)

#to print duplicate nos
arr=[5,2,5,3,2]
arr.sort()                     # 2 2 3 5 5
duplicate_list=[]              # to print list of array     
for i in range(0,len(arr)-1):  # c n          2==2 print(2)   2==3 skips   3==5 skips  5==5 print(5)
    current=arr[i]             # points at the frst index if array
    next=arr[i+1]              # points to the next element of current elements.
    if current==next:
        if current not in duplicate_list: # the same no 
            duplicate_list.append(current)
print(duplicate_list)

# to find the missing value
arro=[1,2,3,5,6]
arro.sort()
for i in range(0,len(arro)-1):   #array-1 bcz if c points to last no then n will will be outside.
    curr=arro[i]
    nex=arro[i+1]
    if nex-curr !=1:               # here the difference is 1 so the no whose difference not 1 is the missing no
        print(curr+1,"is missing")
        break

#method2

arri=[1,2,3,5,6]
arri.sort()
if arri[0]!=1:
    print("1 is missing")
else:
    for i in range(0,len(arri)-1):
        curre=arri[i]
        next=arr[i+1]
        if next-curre!=1:
            print(curre+1,"is missing")
            break

# print a pair with whose some is 8
lst=[2,3,4,5]
sum=8
low=0
upp=len(lst)-1                   #last position of the list.
while(low<upp):                  # 2   3   4   5 
    curr_sum=lst[low]+lst[upp]   # low         upp
    if(curr_sum==sum):
        print(lst[low],lst[upp])
        break
    elif(curr_sum<sum):          # 7<8
        low+=1                   # low=3        then 3+5=8
    else:
        upp-=1                   # if 7>sum we wanted, then upper will decrement upp=4

#lst1 10  12  14   16
#lst2 12  13  14   20     print the common element from both the lists

lst1 =[10,12,14,16]
lst2 =[12,13,14,20]
for n in lst1:
    if n in lst2:
        print("common element =",n)

#method 2  
lst1 =[10,12,14,16]                        #  10     12     14    16                12     13     14    20
lst2 =[12,13,14,20]                        #  p1                                    p2
lst1.sort()                                # p1<p2     so p1 will increement  12& 12 compared, now p2 icreemeted, 13& 12 compared now  14&13,   14&14(printed)   now 20&16 and loops end
lst2.sort()
p1,p2=0,0                                   # p1 &p2 points at the frst position
while(p1<len(lst1) and p2<len(lst2)):       # p1&p2 stands for position of list.  here p1=p2=0 so p1&p2 will be less than lsts  
    if lst1[p1]==lst2[p2]:                  #  if the frst element of both are same then it will be printed
        print("common element =",lst2[p2])  # either p1 or p2 will be printed
        p2+=1                               # here p2 is printed so p2 will be incremented.
    elif lst1[p1]<lst2[p2]:                 # p2>p1, so p2 will be considered(the next element in lst2 will be greater)
        p1+=1                               # if p1<p2 p1 will be smaller, so the p1 element will not be there in p2 anymore since it is sorted.
    else:
        p2+=1                               # otherwise p2 will be increemented.



#Userinput

limit=int(input("enter the length of list"))
lst=[]
for i in range(limit):
    element=int(input("enter element"))
    lst.append(element)
print(lst)




