items=[
    {"id":10,"name":"cb","price":160},
    {"id":101,"name":"vb","price":140},
    {"id":102,"name":"ghhe roast","price":120},
    {"id":103,"name":"afm","price":130},
    {"id":104,"name":"cf","price":90},
    {"id":105,"name":"porotta","price":10},

]
def add_items(*args,**kwargs):
    items.append(kwargs)
add_items(id=106,name="bb",price=180)
print(items)
def retrieve_items(id=None,*args,**kwargs):
    obj=[i for i in items if i.get("id")==id]
    return obj
print(retrieve_items(id=103))

def destroy_item(id=None,*args,**kwargs):
    obj=[i for i in items if i.get("id")==id][0]
    items.remove(obj)
def update_item(id=None,*args,**kwargs):
    obj=[i for i in range if i.get("id")==id][0]
    obj.update(kwargs)
update_item(id=102,name="GHEE ROAST")
print(retrieve_items(id==102))
