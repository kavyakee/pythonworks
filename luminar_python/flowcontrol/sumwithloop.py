# print sum of numbers  1 upto 10
i=1
sum=0
while(i<=10): # 1<=10       2<=1      3<=10      ......10<=10
    sum=sum+i # sum=0;0+1=1 sum=1+2=3 sum=3+3=6  .....sum=55
    i+=1      # i=2         i=3       i=4         .....i=10
print("sum of numbers upto 10 =",sum) 

# sum of odd numbers, range given by user
i=int(input("enter the starting no"))
j=int(input("enter the ending no"))
while(i<=j):
    if(i%2!=0):
        sum=0
        sum=sum+i
        i+=1
print("sum of odd numbers =", sum)

# sum of even numbers, range given by user

i=int(input("enter the starting no"))
j=int(input("enter the ending no"))
sum=0
while(i<=j):
    if(i%2==0):
        sum=sum+i
        i+=1
print("sum of even numbers =", sum)
