class Hotel:
    items=[
    {"id":10,"name":"cb","price":160},
    {"id":101,"name":"vb","price":140},
    {"id":102,"name":"ghhe roast","price":120},
    {"id":103,"name":"afm","price":130},
    {"id":104,"name":"cf","price":90},
    {"id":105,"name":"porotta","price":10},

    ]
    def create(self,*args,**kwargs):
        self.items.append(kwargs)
        return f"{kwargs} created"
    # to retrieve
    def retrieve(self,id=None,*args,**kwargs):
        obj=[i for i in self.items if i.get("id")==id][0]
        return obj
    # to remove
    def destroy(self,id=None,*args,**kwargs):
        obj=[ i for i in self.items if i.get("id")==id][0]
        self.items.remove(obj)
        return f"{obj} has been removed"
    # to update
    def update(self,id=None,*args,**kwargs):
        obj=self.retrieve(id=id)
        obj.update(kwargs)
        return f"{obj} has been updated"
    
    
    
obj=Hotel()
# obj.create(id=109,name="noodles",price=150)
# print(obj.retrieve(id=10))
# print(obj.destroy(id=102))
print(obj.update(id=102,name="GHEE ROAST"))
        
    