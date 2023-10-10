lst=[1,2,3,5,6] 

   
    
for i in range(0,len(lst)-1):   
    curr=lst[i]
    nex=lst[i+1]
    if nex-curr !=1:               
        print(curr+1,"is missing")
        break