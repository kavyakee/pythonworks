num=int(input("enter the number"))
sum=0
while(num!=0):
    digit=num%10
    cube=digit**3
    sum+=cube
    num=num//10
print(sum)




text="carrot"
word_count={}
for ch in text:
    if ch in word_count:
        word_count[ch]+=1
    else:
        word_count[ch]=1
print(word_count)

source_word="poop"
target_word="pop"
source_list=[]
kangaroo= ""
for ch in source_word:
    source_list.append(ch)
for ch in target_word:
    source_list.pop(source_list.index(ch))
    kangaroo+=ch
print(kangaroo==target_word)



lst=[10,12,13,14,15,17]
element=12
is_found=False
i=0
stop=len(lst)
while(i<stop):
    curr_val=lst[i]
    if(curr_val==element):
        is_found=True
        break
     i+=1
print(is_found)










lst=[2,5,3,8,10,4,6]
lst.sort()
is_found=False
low=0
upp=len[lst]-1
s_ele=4
while(low<=upp):
    mid=low+upp//2
    if  (s_ele=lst[mid]):
        is_found=True
        break
    elif s_ele<lst[mid]:
    upp=mid-1
    elif s_ele>lst[mid]:
    low=mid+1
print(is_found)
    




