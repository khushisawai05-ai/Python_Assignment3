# Create a function that checks whether a given number is a prime number.
def prime(number):
    if number<2:
        return False
    for i in range(2,number):
        if number % i ==0:
            return False
    return True
number = int(input("Enter number:"))
if prime(number):
    print(number,"is a Prime Number.")
else:
    print(number,"is not a Prime Number.")