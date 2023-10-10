#file name should be given at last, the file which we needed.
fw=open("C:\\Users\Admin\\Desktop\\luminar_python\\fileoperations\\write.txt","w")
fw.write("DIE")

# to print 1800-2025
fw=open("C:\\Users\Admin\\Desktop\\luminar_python\\fileoperations\\yrs.txt","w")
for y in range(1800,2025):
    fw.write(str(y)+"\n")

