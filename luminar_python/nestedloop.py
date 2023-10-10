# nested loop is loop inside a loop
#     #       # 
#     #       #
#     #       #                  print this
                              # column works with respect to rwo should be considered.
for row in range(1,4):        # first of all provide the loop of row
    for col in range(1,4):    # then only the column. 
        print("#",end="\t")   # here end is provided to print the "#" in column wise respect to its corresponding column \t is for tab space.
    print()                   # print() is to print # to next line print("#",end="\n") can also provided.


#   1   1   1
#   2   2   2
#   3   3   3        print this

for row in range(1,4):
    for col in range(1,4):
        print(row,end="\t")    # here column gets incremented,value in row remains same,so row can be used.
    print() 


#   
#   #
#   #   #      print this

for row in range(1,4):
    for col in range(row):   # here column correspond to row is equal to row no, r1 contains 1 column,r2 contains 2 column, r3 contains 3 column.and also to gets traingular shape(or this shape) we can use this method
        print("#",end="\t")
    print()

#   1
#   1   2
#   1   2   3

for row in range(1,4):
    for col in range(row):
        print(col+1,end="\t")
    print()

#1
#1   #
#1   #  3
#1   #  3   #
#1   #  3   #   5
#1   #  3   #   5   #      print this     here in the place of even no it is #

for row in range(1,6):
    for col in range(row):
        result=col+1
        if result%2==0:
            print("#",end="\t")
        else:
            print(result,end="\t")
    print()


#   #   #   #
#   #   #
#   #
#                          print this

for row in range(4,0,-1):        # here in backward,
    for column in range(row):
        print("#",end="\t")
    print()

#           *
#         *   *
#       *   *   *
#     *   *   *   *
#   *   *   *   *   *
# *   *   *   *   *   *       print this

# 1  2  3  4  5  *                      r6
# 1  2  3  4   *   *                    r5
# 1  2  3   *    *     *                 r4
# 1  2   *     *     *    *             r3
# 1   *    *     *    *     *           r2
# *   *   *   *     *     *     *       r1

for row in range(1,7):
    for space in range(7-row,1,-1):   #we have 7 rows, frst row have 5 spaces(r6-1=5), rnd row-2=4,the rows gets decremented so -1.
        print(end=" ")                # to print the spaces
    for star in range(row):           # to print the *, frst row have 1 star, 2nd row have 2 stars.....
        print("*",end=" ")
    print()

limit=6
for row in range (1,limit+1):
    for col in range(1,limit*2):
        if(col%2!=0 and row==limit) or row+col==limit+1 or col-row==limit+1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
        print()


