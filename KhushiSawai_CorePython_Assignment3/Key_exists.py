# Check whether a particular key exists in a dictionary.
student = {'Name':'Khushi','Age':24,'Course':'Python','City':'Mumbai'}
print(student)
key_name =input("Enter Key:")
if key_name in student:
    print(f"Key exists in the dictionary: {key_name}")
else:
    print(f"Key is not exists in the dictionary: {key_name}")