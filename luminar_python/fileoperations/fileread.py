# 3 modes => read(r),write(w),append(a)
# syntax= open("copy path(copy the txt file and paste)","mode")
# back slash \ should be 2 (\\) otherwise use forward slash /

f=open("C:\\Users\\Admin\\Desktop\\luminar_python\\fileoperations\\data.txt","r")
for line in f:
     print(line)

# Using list comprehension
words=[line.rstrip("\n") for line in f ]             #rstrip => to remove from right side.
print(words)