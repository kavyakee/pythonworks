lst=[
    [25,27,30],
    [33,35,39]
    [40,41,42]
    [70,72,73]
]
lst.sort()
low=0
upp=len(lst)
search_element=35
is_found=False
while(low<=upp):
    mid=lst[low]-lst[upp]
    if (search_element==lst[mid]):
        is_found=True
    elif( lst[mid]<search_element):
        upp=mid-1
    elif( lst[mid]>search_element):
        low=mid+1
    print(is_found)