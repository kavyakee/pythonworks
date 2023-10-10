#check whether the first letter of the given word is vowel or consonant
#casefold() can be applied in iniatialization to convert capital letter to small letters
word=input("Enter the word")
if(word[0]=="a" or word[0]=="e" or word[0]=="i" or word[0]=="o" or word[0]=="u"):
    print("vowel")
else:
    print("consonant")

#leap year or not

year=int(input("Enter the year"))     
if(year%100==0 and year%400==0):    #century year
    print("leap year")
elif(year%100!=0 and year%4==0):    # non century year
    print("leap year")
else:
    print("not leap year")

 # case 1 ,century leap year( ending with 00) if a yearv is century year that must be divisible by 400(century year= year%100=0 and year%400=0).
 # case 2 , not a century year if the year is not a century year that must be divisble by 4.
 # both the above cases have leap year
 # in the above prgrm, we have 3 cases leap year with centuary year, leap year of not a century year and not a leap year.