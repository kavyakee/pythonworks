lst=[1,2,3,4,5]
squares=[]
for n in lst:
    squares.append(n**2)
print(squares)
# instead of using this method

lst=[1,2,3,4,5]
squares=[]
squares=[ n**2 for n in lst]                
print(squares)

# in [] in left side there we will apply the code for return, in middle the loop and at the right side the condition.

#CUBES
lst=[1,2,3]
cubes=[]
cubes=[n**3 for n in lst]
print(cubes)

# ODD or EVEN
lst=[1,2,3,4,5,6,7,8,9,10]
even=[n for n in lst if n%2==0]
odd=[n for n in lst if n%2!=0]
print(even)
print(odd)

# greater than5
lst=[1,2,3,4,5,6,7,8,9,10]
grterfive=[n for n in lst if n>=5]
print(grterfive)

# print 1800-2024
yrs=[y for y in range(1800,2024)]
print(yrs)

# to print centuary yrs
yrs=[y for y in yrs if y%100==0]
print(yrs)

#non century yrs
yrs=[y for y in range(1800,2024)]
yrs=[y for y in yrs if y%100!=0]
print(yrs)

# print the following using listcomprehension

items=[
    {"id":1,  "name":"sugar",      "price":40,  "avl_qty":10},
    {"id":2,  "name":"milk",       "price":28,  "avl_qty":40},
    {"id":3,  "name":"teapowder",  "price":230, "avl_qty":100},
    {"id":4,  "name":"tomatto",    "price":120, "avl_qty":5},
    {"id":5,  "name":"potatto",    "price":45,  "avl_qty":70},
    {"id":6,  "name":"carrot",     "price":80,  "avl_qty":0},
    {"id":7,  "name":"oreo",       "price":45,  "avl_qty":0},
    {"id":8,  "name":"hideandseek","price":50,  "avl_qty":50},
     ]
# print all names
all_names=[i.get("name")for i in items]
print(all_names)

#print instock(available) items
instock_items=[i.get("name")for i in items if i.get("avl_qty")>0]
print(instock_items)

#print items under 50
under_fifty=[i.get("name")for i in items if i.get("price")<50]
print(under_fifty)

#print items in the range of 20-50(price)
rangetwenty_fifty=[i.get("name") for i in items if i.get("price") in range(20,51)]
print(rangetwenty_fifty)

# print the price of oreo
oreo_price=[i.get("price") for i in items if i.get("name")==("oreo")]
print(oreo_price)

# update the price of oreo to 90
oreo_data=[ i for i in items if i.get("name")=="oreo"][0]        #[0] here output will be in list to remove the [] from terminal we use [0].
oreo_data["price"]=90                                            # intstead of using [0] above we can also use oreao_data[0]["price"]=90
print(items)


# costly product & cheap product
costly_product=max(items,key=lambda d:d.get("price"))
cheap_product=min(items,key=lambda d:d.get("price"))
print(costly_product)
print(cheap_product)