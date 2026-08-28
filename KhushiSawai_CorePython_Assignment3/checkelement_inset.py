# Create a program that checks whether a particular element exists in a set.
set = {10,20,30,40,50}
number = int(input("Enter number to search:"))
print(f"Set: {set}")
if number in set:
    print(f"{number} is present in the set")
else:
    print(f"{number} is not present in the set")
