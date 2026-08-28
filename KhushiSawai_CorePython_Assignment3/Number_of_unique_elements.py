# Find the number of unique elements in a collection
numbers = input("Enter numbers:")
numbers = numbers.split()
unique_numbers = set(numbers)
print("Number of unique elements:",len(unique_numbers))
