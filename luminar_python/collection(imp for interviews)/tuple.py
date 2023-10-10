# TUPLE
# ()            eg;tp=(10,20,20,30)
# Duplicates allowed.
# Indexing supported.
# Updation couldnt be supported.(immutable)
# Insertion order preserved.
# database are tuples by default since it doesnt needs to be modified.

# TUPLE METHODS
# count() - to know the no of occurance of an object.
# index() - to know the position of an object.

tp=(10,20,20,30)
print(tp.count(20))
print(tp.index(30))
print(sorted(tp))