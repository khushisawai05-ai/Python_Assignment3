# Update a Dictionary Value
# Update an existing value in a dictionary

stu={"Name":"Shrija","Age":15,"Course":"Python","City":"Amravati"}
print(f"Original Age: {stu['Age']}")
stu.update({"Age":21})
print("Updated Age:", stu["Age"])
print("Updated Dictionary:",stu)