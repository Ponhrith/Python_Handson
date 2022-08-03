"""
John Smith:
Name = John Smith
Age = 28
Gender = Male

"""

person = {
    "name":"John Smith",
    "age": 28,
    "gender": "Male",
    "is_married": True
}
print(person["name"])
print(person.get("birth_date", "December 25th, 1998"))

# print["name"] = "Mark Warner"
# print(person["name"])


person["birth_date"] = "December 25th, 1998"
print(person["birth_date"])