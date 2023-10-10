#ABSTRACTION
#Hiding the details and provides the abtracted data.
# it should be inherited from abstract class (ABC).

from abc import ABC,abstractmethod                            # ABC(Abtract Base Class) should abtracted
class Bike(ABC):
    @abstractmethod                                           # @abstractmethod is a decorator, and is is a must. thats why pass is used
    def started(self):
        pass
        @abstractmethod
    def breaks(self):
        pass
    @abstractmethod
    def accelerate(self):
        pass

class Hunter(Bike):
    def started(self):
        print("hunter starts")
    def breaks(self):
        print("hunter breaks")
    def accelerate(self):
        print("hunter accelerates")

obj=Hunter()
obj.started()
obj.accelerate()








#banking
from abc import ABC,abstractmethod                            # ABC(Abtract Base Class) should abtracted
class Bank(ABC):
    @abstractmethod                                           # @abstractmethod is a decorator, and is is a must. thats why pass is used
    def fund_transfer(self):
        pass
    @abstractmethod
    def bal_enq(self):
        pass
    @abstractmethod
    def transaction_history(self):
        pass

class Gpay(Bank):
    def fund_transfer(self):
        print("gpay fund transfer")
    def bal_enq(self):
        print("gpay balance enquiry")
    def transaction_history(self):
        print("gpay transaction history")
    def gift_card(self):
        print("giftcard")

obj=Gpay()
obj.fund_transfer()
obj.gift_card()



#ENCAPSULATION => binding of data into a capsule.
#super keyword is used to call parent class from child class.

class Parent:
    props=["passion pro "," swift"]
    def get_props(self):
        return self.props
class Child(Parent):
    def get_props(self):
        self.p=super().get_props()
        self.p.append("hunter")
        return self.p
obj=Child()
print(obj.get_props())





