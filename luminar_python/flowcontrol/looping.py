#1) Sequential
#2) Selection
#3) Iterative

 #Looping
#demo
start=1                       #initialization
while(start<=5):              # condition
    print("Hello world")      # statement to be executed or iterated
    start=start+1             # increment or decrement
#1 to 5 
start=1                      
while(start<=5):             
    print(start)      
    start=start+1  

# 5 10 1
start=5
while(start>=1):
    print(start)
    start=start-1     
     
# natural numbers upto 10
i=1
while(i<=10):
    print(i)
    i=i+1

# natural numbers from 10 to 1
i=10
while(i>=1):    # i=10>=1  9>=1  8>=1 ....1>=1  0>=1
    print(i)    # 10       9     8        1     (0>=1)is false so stops execution
    i=i-1       # i=10-1=9,i=8   i=7  ....i=1   i=0

# starting value and ending value should be user defined and print nos

i=int(input("enter the starting value"))
j=int(input("enter the ending value"))
start=i
while(start<=j):
    print(start)
    start=start+1          # start+=1 => start=start+1

i=int(input("enter the starting value"))
j=int(input("enter the ending value"))
while(j>=i):
    print(j)
    j-=1

#print all odd nos within the given range
# 1st method
start=1
range=int(input("enter the ending value"))
while(start<=range):
    print(start)
    start+=2

#2nd method

start=1
range=int(input("enter the ending value"))
while(start<=range):
    if(start%2!=0):
        print(start)
    start+=1

# even numbers
# method 1
start=2
range=int(input("enter the ending no"))
while(start<=range):
    print(start)
    start=start+2

#method 2
start=2
range=int(input("enter the ending no"))
while(start<=range):
    if(start%2==0):
        print(start)
    start=start+1

#homework print nos divisible by 3 and 5 by user input.
#method 1
i=int(input("enter the start no"))
j=int(input("enter the ending no"))
while(i<=j):
    if(i%3==0 and i%5==0):   #nos should be divisible by 3&5 at the sametime.method2 => 2 ifs can be used
        print(i)
    i=i+1

#method 2

i=int(input("enter the start no"))
j=int(input("enter the ending no"))
while(i<=j):
    if(i%3==0):
        if(i%5==0):
            print(i)
    i=i+1


# if a no divisible by 9 print hloo and 18-world

i=int(input("enter the start no"))
j=int(input("enter the ending no"))
while(i<=j):
    if(i%9==0):
        print("hloo")
        if(i%18==0):
            print("world")
    i+=1




