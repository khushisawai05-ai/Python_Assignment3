# Create a function that accepts three numbers and returns the largest number.
def numbers(a,b,c):
    if a>b and a>c:
        return str(a) + "is largest"
    elif b>a and b>c:
        return str(b) + " is largest"
    else:
        return str(c) +" is largest"
a,b,c=map(int,input("Enter numbers:").split())
# Call the function
display = numbers(a,b,c)
print(display)
