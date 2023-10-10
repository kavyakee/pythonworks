#functions- to perform a particular task.
# outside the class


# BUILT IN FUNCTIONS

# print()
# input()
# round()
# max()
# min()
# sum()
# sorted()


#python is interpreted language.
# to add 2 nos

def add(n1,n2):            # we need to define a function first, def-define,add is a userdefined function, n1&n2 are the parameters.
    res=n1+n2
    return res             # to return the result.
print(add(40,60))          # to print the values

# to print the cube
def cube(n):
    res=n**3
    return res
print(cube(3))

# to print the largest

def lar(n1,n2):
    if(n1>n2):
        return n1
    else:
        return n2     #return n1 if n1>n2 else n2     this can also be used. return f"{n1} is greatest" if n1>n2 else f"{n2} is greatest.
print(lar(30,40))

# to print the substraction

def sub(n1,n2):
    return n1-n2
print(sub(10,7))

# smart sub - to subtract the very smallest number from the largest

def smrtsub(n1,n2):
    return n1-n2 if n1>n2 else n2-n1
print(smrtsub(10,5))
print(smrtsub(5,10))

#odd or even

def odevn(n):
    return f"{n} is odd" if n%2!=0 else f"{n} is even"
print(odevn(19))

# hcf
def hcf(num1,num2):
    res=1
    out=num1 if num1<num2 else num2
    for i in range(out+1,1,-1):
        if num1%i==0 and num2%i==0:
            res=i
            break
    return res
def lcm(num1,num2):
    gcd=hcf(num1,num2)
    res=(num1*num2)/gcd                      #eq to find lcm
    return res
    
num1=int(input("enter the num1"))
num2=int(input("enter the num2"))
print(lcm(num1,num2))

#method2
def lcm(n1,n2):
    max=num1 if num1<num2 else num2
    flag=True                                 #to heck the condition
    while(flag):
        if max%n1==0 and max%n2==0:
            print(f"lcm of {n1},{n2} is {max}")
            break
        else:
            max+=1
lcm(18,24)


# selling price ?

def get_discount_price(actual_price,discount):
    selling_price=actual_price-(actual_price*discount)/100
    return selling_price
print(get_discount_price(994,10))


