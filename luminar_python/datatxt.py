class Karthika:
    sister:str
    parents:str
    age:int
    boyfriend:str
    gender:str
    kpop:str
    def create(self,sister,parents,age,boyfriend,gender,kpop):
        self.sister=sister
        self.parents=parents
        self.age=age
        self.boyfriend=boyfriend
        self.gender=gender
        self.kpop=kpop
    def get(self):
        print(self.sister,self.parents,self.age,self.boyfriend,self.gender,self.kpop)
employee=Karthika()
employee.create("kavya","mini &saji",16,"joel","f","bts")
employee.get( )


