#swap- to interchange
num1=10
num2=20
#to swap  method 1
num3=num2
num2=num1
num1=num3
print(num1)
print(num2)           #an additional variable   ia applied to swap
                      # a,b,temp
                      # temp=b
                      # b=a
                      # a=temp


#method 2     
num1,num2=num2,num1     #this method only possible in python


#method 3
num1=num1+num2     #10+20=30   num1=30
num2=num1-num2     #30-20=10   num2=10    1st swap
num1=num1-num2     #30-10=20   num1=20    2nd swap


a,b,c=11,12,13      #multiple assignment
print(a)
print(b)
print(c)
