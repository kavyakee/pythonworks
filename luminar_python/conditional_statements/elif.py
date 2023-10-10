#elif
n1=20
n2=20
if(n1==n2):
    print("two numbers are equal")   #in the case of ;elif', if the'if' condition is true then its print statement will executes, if it is false then only it passes to the 'elif',even if the 'if','elif' is false  then only it passes to the 'else'.
elif(n1>n2):
    print("n1 is greatest")
else:
    print("n2 is greatest")

# Grading System
# > 90-A+
# > 80-A
# > 70-B+
# > 60-B
# > 50-C+
# > 40-C
# > 30-D+
# < 30-Failed
mark=int(input("Enter the mark"))
if(mark>=90):
    print("A+")
elif(mark>=80):
    print("A")
elif(mark>=70):
    print("B+")
elif(mark>=60):
    print("B")
elif(mark>=50):
    print("C+")
elif(mark>=40):
    print("C")
elif(mark>=30):
    print("D+")
else:
    print("failed")


mark=int(input("Enter the mark"))
if(mark>=90):
    print("A+")
if(mark<90 and mark>=80):
    print("A")
if(mark<80 and mark>=70):
    print("B+")
if(mark<70 and mark>=60):
    print("B")
if(mark<60 and mark>=50):
    print("C+")
if(mark<50 and mark>=40):
    print("C")
if(mark<40 and mark>=30):
    print("D+")
if(mark<30):
    print("failed")

#HOMEWORK enter a grade and print which category of mark it is?

grade=input("Enter the grade")
if(grade=="A+"):
    print("90-100")
elif(grade=="A"):
    print("80-90")
elif(grade=="B+"):
    print("70-80")
elif(grade=="B"):
    print("60-70")
elif(grade=="C+"):
    print("50-60")
elif(grade=="C"):
    print("40-50")
elif(grade=="D+"):
    print("30-40")
else:
    ("Failed")


# Fever
celc=float(input("enter your body temp"))
fahrenht=celc*(9/5)+32
print(fahrenht)
if(fahrenht>99):
    print("The person is sick")
else:
    print("Normal temp")

#bmi
weight_inkg=float(input("enter the weght"))
height_incm=float(input("enter the height in cm"))
height_inmeter=height_incm/100
bmi=weight_inkg//height_inmeter**2       #bmi=weight in kg/ height in m^2
print(bmi)
if(bmi<20):
    print("under weight")
elif(bmi<25):
    print("normal weight")
elif(bmi<30):
    print("pre obesity")
elif(bmi<35):
    print("obesity")
else:
    print("invalid")

# largest of 3 nos
num1=int(input("num1"))
num2=int(input("num2"))
num3=int(input("num3"))
if(num1>num2 and num1>num3):
    print("num1 largest")
elif(num2>num1 and num2>num3):
    print("num2 largest")
elif(num3>num2 and num3>num1):
    print("num3 is largest")
elif(num1==num2 and num1==num3):
    print("all are equal")

# 2nd largest

num1=int(input("num1"))
num2=int(input("num2"))
num3=int(input("num3"))
if(num3>num2 and num2>num1):
    print("num2 is second largest")
elif(num1>num3 and num2<num3):
    print("num3 is second largest")
elif(num2>num1 and num3<num1):
    print("num1 is second largest")