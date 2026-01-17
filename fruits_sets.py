my_fruits = {'mandarina', 'platano', 'mango', 'ciruela', 'sandia'}
my_bff_fruits = {'mandarina', 'mango', 'sandia', 'guayaba', 'fresa'}

union_fruits = my_fruits.union(my_bff_fruits)
intersection_fruits = my_fruits.intersection(my_bff_fruits)
difference_fruits = my_fruits.difference(my_bff_fruits)
difference_fruits2 = my_bff_fruits.difference(my_fruits)

print(union_fruits)
print(intersection_fruits)
print(difference_fruits)
print(difference_fruits2)
