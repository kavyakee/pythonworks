# SET
# set() 
#denoted by {n1,n2...} eg;st={10,20,30}          {} - dictionary
# indexing not supportable  eg;st[1] st[5] st[0]   etc are not possible
# no insertion order.
# duplication not allowed.
# mutable.

#SET METHODS
st={10,20,30,8,9}
#       0  1 2 3
#add()    to add an element to the set.
st.add(70)                       # 20,70,8,9,10,30
print(st)                        # here 0th element=20   1st element is 30 replaced by 70 then followed by the 3rd element 4,5... lastly the replaced element.
st1={10,20,30,40}
st2=(21,45,67,10)
#union - 2 sets combined
union_set=st1.union(st2)
print(union_set)
#intersection - to find the common element from both the sets.
intersect_set=st1.intersection(st2)
print(intersect_set)
# set difference - set1-set2 or set2-set1
set_difference=st1.difference(st2)
print(set_difference)
# remove- to remove a particular element from set return error if its false
# discard- to discard (but doesnt return errors)
st1.remove(20)
print(st1)
st1.discard(40)
print(st1)
#pop - to remove randomly
st1.pop
print(st1)
# symmetric difference
# set1Uset2 - set1 n set2            union of set1&set2 - intersection of set1&set2
sym_diff=st1.symmetric_difference(st2)
print(sym_diff)
