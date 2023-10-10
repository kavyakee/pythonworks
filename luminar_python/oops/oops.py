# OOPS object oriented prgrms
# attributes in lowercase.(characteristics eg; bottle attributes are its material, quantity,company ....)
# methods

class Employee:
    id:int
    name:str
    gender:str
    salary:int
    def create(self,id,name,gender,salary):                   # self is a keyword(used to point the current object.)
        self.id=id
        self.name=name
        self.gender=gender
        self.salary=salary
    def get(self):
        print(self.id,self.name,self.gender,self.salary)

emp1=Employee()
emp1.create(123,"kavya","female","50000")
emp1.get()

emp2=Employee()
emp2.create(109,"hana","male","5")
emp2.get()



class Bank:
    accountno=int
    person_name=str
    ifsc_code=str
    branch=str
    account_type=str
    balance=int
    bank_name=str
    def create(self,ac_no,ifsc,branch,balance):
        self.accountno=ac_no
        self.ifsc_code=ifsc
        self.branch=branch
        self.balance=balance
    def deposit(self,amount):                                                               # here after the keyword self, amount is given as attribute since we have to provide the amount in the method calling section bcz we are adding the amount here by user input.
        self.balance+=amount
        print(f"your {self.accountno} has been credited withamount {amount} balance {self.balance} ")
    def withdraw(self,amount):                                                              # # here after the keyword self, amount is given as attribute since we have to provide the amount in the method calling section bcz we are debuting the amount here by user input.
        if amount >self.balance:
            print("insufficient balance")
        else:
            self.balance-=amount
            print(f"your {self.accountno} has been debited by {amount} balance {self.balance}")
    def getbalance(self):
        print(f"your current balance is {self.balance}")
customer=Bank()
customer.create(1234567890,"FBRL6789","Kakanad",3456789000000)  
customer.deposit(7890)
customer.withdraw(789000)
customer.getbalance()     


              
