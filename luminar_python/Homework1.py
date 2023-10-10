# 1 swap 3 numbers
num1=10
num2=20
num3=30
num4=num3
num3=num2
num2=num1
num1=num4
print(num1)
print(num2)
print(num3)

# 2 swapping of 2 strings
str1="i am"
str2="kavya"
str3=str2
str2=str1
str1=str3
print(str1) 
print(str2)

 # 3 swapping of 3 string
str1="i am"
str2="kavya"
str3="from Thiruvalla"
str4=str3
str3=str2
str2=str1
str1=str4
print(str1)
print(str2)
print(str3)

# 4 find out the selling price of a product if offer in percentage and items current price is given.
  # eg; current price = 20
  #     offer in percentage(discount in percentage)= 2%
  #     selling price =?
cp=20
op=50
dis=cp*op/100
sp=cp-dis
print("current_price is",cp)
print("discount is", dis)
print("selling_price is",sp)

# 5 Convert degree celsius to fahrenheit 
# celsius => fahrenheit
cel=100
fah=(cel*1.8)+32
print("celsius is",cel)
print("fahrenheit is",fah)

# 6 %dis ??
actual_price=140
selling_price=135   #sp=ap-dis
dis=actual_price-selling_price
print(dis)
offer_inperc=(dis/actual_price)*100    #%dis=(dis/ap)*100
print(offer_inperc)

# 7 BMI body mass index
#bmi=(weight in kg)/height in meter square
weight_kg=72
height_cm=165
#cm=>meter   meter=cm/100
height_m=height_cm/100
bmi=(weight_kg)/height_m**2     #meter square is meter raise to 2 so it will be **2(exponential) m^3=>m**3
print(bmi)

# CONVERSIONS
# 8
vol_litre=5
vol_millitre=vol_litre*1000
print(vol_millitre)
# 9
pressu_pas=1
press_bar=pressu_pas/100000
print(press_bar)

#10
speed_meter_persec=4
speede_kmperhr=speed_meter_persec*3.6
print(speed_meter_persec)

# 11
mass_kg=6
massgrm=mass_kg*1000
print(massgrm)
