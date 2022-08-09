tuplee=(1,2,3,4)
print(tuplee)
print(len(tuplee)) #print length
print(tuplee[1:3]) #slicing
print(tuplee.count(3)) #count how many 3 is present in the tuplee
print(tuplee.index(4)) #print the index of the value

fruits=("apple","banana","mango","guava","jackfruit")
a,b,*c=fruits #tuple unpacking
print(a)
print(b)
print(c)
