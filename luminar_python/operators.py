#operators
#arithmetic   + => addition
            # - => subtraction
            # * => multiplication 
            # / => division
            # % => modulus
            # ** => exponential
            # //=> floor division
#logical
#assignment
#relational
#bitwise
#membership operators
#ternary operator
  
#ternary operator
# +ve or -ve

num=-10
#if(num>0):
#  print("+ve")
#else:
#   print("-ve")
result="+ve" if num>0 else "-ve"     #intead of the above code 19,29,21 and 22 it can be applied in a single line
print(result)

#odd or even
num=70
result="even" if num%2==0 else "even"
print (result)

#largest
num1=90
num2=100
result="num1 larger" if num1>num2 else "num2 larger"
print(result)

# num>5,num+1 and num<5 num-1 (mapping)

num=int(input("enter the number"))
#if(num>5):
#    print(num+1)
#else:
#    print(num-1)
result=(num+1) if num>5 else (num-1)
print(result)

#smart sub
n1=int(input("enter the number1"))
n2=int(input("enter the number2"))
#if n1>n2:
#    print(n1-n2)
#else: 
#    print(n2-n1)
result=n1-n2 if n1>n2 else n2-n1
print(result)

int=int(input("enter the number"))
result="+ve" if num>0 else "-ve" if num<0 else "zero"
print(result)
b
#(mapping)

num=int(input("enter the number"))
result=num+1 if num>5 else num-1 if num<5 else 5
print(result)