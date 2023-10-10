#fibanacci series
# 0  1  1(0+1)  2(1+!)  3(2+1)    5(2+3)   ........ previous no+ current no

prev=0
current=1
print(prev)
print(current)
start=1             # start1 means the position
while(start<=9):
    fib=prev+current   
    print(fib)
    prev=current
    current=fib
    start+=1


#Armstrong number
#eg 153= 1^3 + 5^3 + 3^3 = 153   (in python 1**3+5**3+3**3)
# here 135 is a 3 digit no thats why we used the **3, exponent of the digit used should be considered,sum of exponent of digits = number
num=int(input("enter the no"))
original=num
sum=0       #then only sum application possible
while(num!=0):        #here we are gonna extract each digit,thats why we check num not equal to 0       15!=0       1!=0     0!=0 false      
    digit=num%10      # 153%10=3                                                                        15%10=5     1%10=1
    cube=digit**3     # cube= 3**3=27                                                                   5**3=125    1**3=1
    sum+=cube         # sum=sum+cube  0+27                                                              0+125=125   0+1=1          
    num=num//10       # num=153//10=15                                                                  15//10=1    1//10=0
print(sum)            # sum=27+125+1=153
if(sum==original):    # if we check sum==num, num=0(from the while loop) so we should initialize num=original to check whether the no is armstrong or not
    print("num is armstrong")
else:
    ("not")



