# LINEAR SEARCH       list should be sorted.


lst=[12,14,16,17,90]
element=17
i=0
stop=len(lst)
is_found=False
while(i<stop):
    cur_value=lst[i]
    if cur_value==element:
        is_found=True
        break
    i+=1
print(is_found)

# BINARY SEARCH                  list should be sorted.

# worst case  - to search an element not in the list.
# edge case   - to search the element at low & upp
lst=[3,2,14,8,9,10,7]
lst.sort()                        #  low___________ midd ____________upp
low=0                             #     -                      +
upp=len(lst)-1                    #    s.e< midd               s.e > midd
search_element=3                  #      upp                      low      (to be placed)
is_found=False                   
while(low<=upp):
    mid=(low+upp)//2
    if search_element==lst[mid]:       #   2  3  7  8  9  10  14           
        is_found=True                  #   0  1  2  3  4  5   6                 
                                       #  low       mid        upp
        break
    elif search_element<lst[mid]:      #  3<8  place upp to mid-1(2nd location)        
        upp=mid-1
    elif search_element>lst[mid]:      # if srch element>8 place low to mid+1 
        low=mid+1                      # while loop executes till we find the srch element,in each iteration middle element will be compared with right or left sublist.

print(is_found)



