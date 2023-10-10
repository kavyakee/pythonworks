from re import *
text="ABCDABCDAB"
rule="[A-B]*"
pattern="AB"
count=0
matcher=finditer(rule,text)
for m in matcher:                                       
    print(m.start(),m.group())
for ch in text:
    if ch in pattern:
        count+=1
    else:
        count=1
print(count)


