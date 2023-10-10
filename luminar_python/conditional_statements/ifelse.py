age=int(input("enter the age"))
if(age>=18):
    print("eligible")
else:
    print("not elible")

#HOMEWORK
# check whether the numbers are greater,lesser or equal.
num1=int(input("enter the  first number"))
num2=int(input("enter the second number"))
if(num1>num2):
    print("the greatest number is",num1)
if(num1<num2):
    print("the smallest number is",num1)
if(num1==num2):
    print("the numbers are equal")
else:
    print("invalid")

# print 3 numbers in ascending or descending order
num1=int(input("num1"))
num2=int(input("num2"))
num3=int(input("num3"))
if(num1>num2 and num1>num3):
    if(num2>num3):
        print("num1,num2,num3")
    else:
        print("num1,num3,num2")
if(num2>num1 and num2>num3):
    if(num1>num3):
        print("num2,num1,num3")
    else:
        print("num2,num3,num1")
if(num3>num1 and num3>num2):
    if(num1>num2):
        print("num3,num1,num2")
    else:
        print("num3,num2,num1")