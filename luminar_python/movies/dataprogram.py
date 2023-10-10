from json import load
path="C:\\Users\\Admin\\Desktop\\luminar_python\\movies\\mdb.json"
with open(path,encoding="utf-8") as f:
    filims=load(f)
print(len(filims))
# all movies names in 2015

# comedy movies
funny_movies=[f.get("title") for f in filims if "Comedy" in f.get("genres")]
print(funny_movies)
# id in range of (20,21) and runtime>110
mfilter=[ f.get("title") for f in filims if f.get("id") in range (20,31) and f.get("runtime")<="110"]
# movies with one word, print their titles
title_flr=[f.get("title")for f in filims if len(f.get("title").split(" "))==1]
print(title_flr)

#genre=drama, highest runtime
fdrama=[f for f in filims if "Drama" in f.get("genres")]
longest=max(fdrama,key=lambda f:int(f.get("runtime")))
print(longest)

# print the which has the highest runtime movies
wc={}
for m in filims:
    year=m.get("year")
    if year in wc:
        wc[year]+=1
    else:
        wc[year]=1
# out=max(wc,key=lambda k:wc.get(k))
# print(out)

print(max((v,k) for k,v in wc.items()))            # when its (v,k) value will be considered frst then key