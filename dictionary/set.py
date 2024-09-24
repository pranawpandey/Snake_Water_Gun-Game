set1= set([1,2,3,4,5])
set2= set([2,3,5,6])
print(set2-set1) #difference
print(set2 | set1) #union
print (set1.union(set2))
print(set2.intersection(set1))
print(set2.difference(set1))
print(set1 & set2) #intersection
print (set1)
                                         
set2.add(8)
print(set2)

set1=set([1,2,3,'p','o','i'])
set2=set([5,6,3,'l','n','b'])
print(set2.difference(set1))
print(set2.intersection(set1))
print(set2.union(set1))
set2.add('apple')
print(set2)

print(set2.add(" apple "))
