# Create a program to perform basic operations on a set.

numbers = {10,20,30,40,50}
print(f"Original Set:",numbers)

add_num = int(input("Enter numbers to add:"))
numbers.add(add_num)

remove_num = int(input("Enter number to remove:"))
numbers.remove(remove_num)

print(f"Final Set:",numbers)