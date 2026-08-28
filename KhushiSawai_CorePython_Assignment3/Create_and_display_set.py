# Create a Python program that accepts multiple values from the user and stores them in a set.

numbers=input("Enter 5 numbers:").split()
num_set = set(map(int,numbers))
print("Set:",num_set)