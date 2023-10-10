# multiplication table of 2
 
num=1
while(num<=10):                  #1<=10                                            2<=10     .....10<=10
    print(f"{num} * 2 ={num*2}") # num=1; 1*2 =1*2(real multiplication operation)  2*2=2*2=4  ....10*2=10*2=20
    num+=1                       # num=2    num=3      ....num=10

# factorial
#4!= 4*3*2*1
num=4
start=1
f=1
while(start>=num):
    f=f*start
    start=start+1
    print(f)
