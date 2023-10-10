#conditional statements
# comparison and logical 0r relational operators are used.tab space are used for print(statements) instead of {}
# if,else,elif
# if syntax
# initialization
# if(condition)
#   print(statements...)       must give a statement and there should be proper indentation( : must, tab space)
# check a number is positive
num=5
if(num>0): 
    print("given number is positive")      # print statements following same tab space includes in the mainbody of 'if'
    print()  # output will be a blank line... still run bcz it included in the mainbody of 'if' since it follows the same tab space
print("hi")  # output will be as hi since python follows line by libe execution even if it is not included in the main body of 'if'
if(num<0):
    print("given number is negetive")

    # if the condition is unsatisfied then the statements in the mainbody of 'if' doesnt executes
# Homework

a=60
b=35
if (a>b):
    print("largest number =",a)
if(a<b):
    print("largest number =",b)

# user input   
#simple input
num1=input("enter first number:")      #user can provide the input values to the terminal
num2=input("enter second number:")
print(type(num1))                      #to get type of the values
print(type(num2))
# if we use print(num1*10), it will be considered as string and num1 will be displayed as ten num1s(eg;num1=22,num1*10=2222222222)and also num1+2,num1/10 addition and division also not possible with strings.
# to avoid the above prblm, we use int(input),when we specify the datatype of values, it could be considered as integers and normal arithmetic operations are possible.

#int(input)

num1=int(input("enter first number:"))   #above case the datatype will be as string since no datatype mentioned prior to number,so provide 'int'
num2=int(input("enter second number:"))
print(type(num1))
print(type(num2))


#float(input)
num1=float(input("enter the first number:"))
num2=float(input("enter the second number:"))
print(type(num1))
print(type(num2))
print(num1*10)

 #voting eligibility   
 
age=int(input("enter your age:"))
if(age>=18):
    print("eligible for voting")
if(age<18):
    print("not eligible for voting")


# 2 'if's can be used, but the ccrct condition only gets printed

# read colours from user,if "red" print "STOP", "green"  print"GO", "yellow" print"WAIT"

colour=input("enter the colour:")
if(colour=="red"):
    print("STOP")
if(colour=="green"):
    print("GO")
if(colour=="yellow"):
    print("WAIT")
