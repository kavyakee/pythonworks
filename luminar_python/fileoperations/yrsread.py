frr=open("C:\\Users\\Admin\Desktop\\luminar_python\\fileoperations\\yrs.txt","r")
frr_write=open("C:\\Users\Admin\\Desktop\\luminar_python\\fileoperations\\leapwrite.txt","w")
for year in frr:
    year=int(year)                          # it will be string to convert it to integer.
    if (year%100==0) and (year%400==0):
        frr_write.write(str(year)+"\n")
    elif(year%100!=0) and (year%4==0):
        frr_write.write(str(year)+"\n")
        