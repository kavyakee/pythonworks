f=open("C:\\Users\\Admin\\Desktop\\luminar_python\\fileoperations\\numbers.txt")
# to print all the vehicle numbers.
all_nums=[line.rstrip("\n")for line in f]
print(all_nums)

#to print the kerala vehicle numbers
kerala_nums=[num for num in f if num.startswith("kl")]
print(kerala_nums)