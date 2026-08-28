# Create a program that demonstrates the basic operations of Python sets.
set_A = {1,2,3,4}
set_B = {3,4,5,6}

# Union
print(f"Union: {set_A.union(set_B)}")

#Intersection
print(f"Intersection: {set_A.intersection(set_B)}")

# Difference
print(f"A-B: {set_A.difference(set_B)}")

# Symmetric Difference
print(f"Symmetric Difference: {set_A.symmetric_difference(set_B)}")