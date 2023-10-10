datas=[
    {"id":100,"name":"python","price":350},
    {"id":101,"name":"java","price":450},
    {"id":102,"name":"Django","price":1300},
    {"id":103,"name":"Html","price":1000},
    {"id":104,"name":"Bootstrap","price":300},
    

]
print(datas)

def retrieve_datas(id=None,*args,**kwargs):
    obj=[i for i in datas if i.get("id")==id]
    return obj
print(retrieve_datas(id=103))




def destroy_datas(id=None,*args,**kwargs):
    obj=[i for i in datas if i.get("id")==id][0]
    datas.remove(obj)
    return obj
print(destroy_datas(id=103))
print(datas)

def update_datas(id=None,*args,**kwargs):
    obj=[i for i in range if i.get("id")==id][0]
    obj.update(kwargs)
update_datas(id=101,name="Css")
print(update_datas(id==101))

