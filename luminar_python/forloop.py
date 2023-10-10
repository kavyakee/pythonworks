# inside the class is method and outside the class is function
#\n is next or new line
#range(start,stop step) start=starting value   stop= ending value(1-10 then upto 9)  step=jump (2 1,3,5....)

# print 1 to 10
for i in range(1,10,1):
    print(i)

# print 10 to 1
for i in range(10,1,-1):
    print(i)

#user input
low_limit=int(input("enter the lower limit"))
upp_limit=int(input("enter the upper limit"))
for i in range(low_limit,upp_limit):
    print(i)

#print all even numbers between lower limit and upper limit
low_limit=int(input("enter the lower limit"))
upp_limit=int(input("enter the upper limit"))
for i in range(low_limit,upp_limit):
    if(i%2==0):
        print(i)

# HOMEWORK divisible by 3 fizz, 5 buzz, 15 fizz buzz else print no

low_limit=int(input("enter the lower limit"))
upp_limit=int(input("enter the upper limit"))
for i in range(low_limit,upp_limit):
    if(i%3==0):
        print(i,"fizz")
    if(i%5==0):
        print(i,"buzz")
    if(i%15==0):
        print(i,"fizzbuzz")
    else:
        print(i)

    
    #factorial
num=4
fact=1
for i in range(1,num+1):
    fact=fact*i
print(fact)

    #hcf of 2 nos    Highest Common Factor(greatest common divisor)

num1=18
num2=24
for i in range(1,num2+1):                # num2+1 or specified no can be used.
    if (num1 %i==0 and num2%i==0):       #num1 $ num2 gets divided by the i value from the loop.
        hcf=i
print(hcf)

# break    breaks the loop
# continue skips that particular condition

# break
for i in range(1,51):
    if i==25:
        break
    print(i)

#continue
for i in range(1,51):
    if i==25:
        continue
    print(i)

#prime numbers (their factors only should be 1 $ the no itself. eg; 3,5,7,11,13....)

num=int(input("enter the number to check prime or not"))
is_prime=True                #we should assign it to true
for i in range(2,num):       # here start=2 bcz in prime numbers,their factors only should be 1 $ the no itself. so we should check if its divisible by nos except 1.eg 12(1,12 are the factors according to the thoery of prime no, so we should check if its divisble by other no or not)
    if num%i==0:             # to check whether the no is divisible by others or by 1 or the no itself
        is_prime=False       # if it is divisible by other nos then it is not a prime no
        break                # here user input is provided so we need to use break statement to stop the loop.
print(is_prime)              # if the condition satisfied print true.

# vowels in loop

# print alphabets step by step
text="cofee"
for ch in text:                 # ch means character like i in numbers
    print(ch)

# to print vowels
text="cofee"
for ch in text:
    if  ch in ["a","e", "i", "o", "u"]:        #ch == "a" or ch =="e" or ch =="i" or ch =="o" or ch =="u":
        print(ch)

#to print the vowel count & consonant count
text="paralysis"
v_count=0                                # to calculate the upcoming increase in the number of vowels in the given text
c_count=0                                # to calculate the upcoming increase in the number of vowels in the given text
for ch in text:
    if ch in ["a","e", "i", "o", "u"]:  # if there is a vowel in the text it will print 1
        v_count+=1                      # vcount increments & check if there is any other vowel in the text and adds(1+1=2)and vcount increments by 1 & checks if there is another vowel in the text and adds....... 
    else:                               # or else the same thing happns to the consonant count in the given text
        c_count+=1
print("vowel count",v_count)
print("consonant count",c_count)









    