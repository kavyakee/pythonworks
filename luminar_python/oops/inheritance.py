#INHERITANCE
class Parent:
    phone="samsung"
    bike="passionpro"
    def mobile(self):
        print(self.phone)
    def vehicle(self):
        print(self.bike)

class Child(Parent):                              #this method can be used
    pass
obj=Child()
obj.mobile()


# MULTIPLE INHERITANCE

class P1:
    def m1(self):
        print("inside class p1 m1 method")

class P2:
    def m2(self):
        print("inside class p2 m2 method")

class Child(P2,P1):                                    # here p2 p1 classes are inherited by the class child.so thats why the method m2() & m1() are prosecced with respect to the object created by class child.
    def m3(self):
        print("inside class child m3 method")
obj=Child()
obj.m3()
obj.m2()
obj.m1()



# METHOD OVER RIDING       method in child class can over ride the methods in parent class.
# if method overriding should happen, 2 classes must be there and the child classe should be inherited too. 
class iu:
    def dates(self):
        print("wants to date lee jong")
    def marry(self):
        print(" wamts to marry to lee jong")
class Lee_jong:
    def dates(self):
        print("wants to date a celebrity")
    def marry(self):
        print("wants to marry a celebrity")
class hana(iu):
    def dates(self):
        print("dates lee oppa")
    def marry(self):
        print("marries lee oppa")
obj=hana()
obj.dates()




# Variable length argument methods

def product(*args):                                  # '*' will take arguments as tuple.so many values can be taken.
    res=1                                            # res=0 cant be used since n*0=0 so the result will be equal to 0 
    for n in args:
        res*=n                                       # then 1*n
    print(res)
product(1,2,3,4)
product(10,20)






# goodmorning user kavya

def greetings(**kwargs):                             # when we use ** parameters will be taken as dictionary. 
    print(f"{kwargs.get('msg')}app user {kwargs.get('user_name')}")                    # outside is " " so thats why we used ' ' inside.
greetings(msg="good morning",user_name='hana')


#hloo user hana your food is ready to deliver.
def dispatch(**kwrgs):
    print(f"hello {kwrgs.get('name')} your food {kwrgs.get('food')} is ready to deliver")
dispatch(food="ramen",name="hana")




#METHOD OVERLOADING
# same method name, but different parameters

class calculator:
    def add(self,n1,n2):
        print(n1+n2)
    def add(self, n1,n2,n3):
        print(n1+n2+n3)
obj=calculator()
obj.add(10,20)
# but in python we use '*'
















