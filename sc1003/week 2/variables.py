# Variables
print("===== Variables =====")
a = 33
a = "test" # Redeclaring a variable with a different type.
# Invalid variable names
# $a = 33
# 2a = 33
# for = 33 # This is a keyword.
print(a)

HELLO_WORLD = "Hello World"
print(HELLO_WORLD)

# Duck Typing
# If some method/property exists, then it doesn't matter what the type is.
# It can still be used.
print("===== Duck Typing =====")
some_dict_1 = {
    "name": "hello 1",
}

some_dict_2 = {
    "name": "hello 2",
    "age": 33,
}

def print_name(some_dict):
    print(some_dict["name"]) # This will work for both dicts since they have a "name" key.
    
print_name(some_dict_1)
print_name(some_dict_2)

# Variable Types
print("===== Variable Types =====")
a_float = 33.0
a_int = 100
a_string = "Hello World"
a_boolean = True
a_list = [1, 2, 3]  
a_dict = {"name": "hello"}

print(f"Float: {type(a_float)}")
print(f"Int: {type(a_int)}")
print(f"String: {type(a_string)}")
print(f"Boolean: {type(a_boolean)}")
print(f"List: {type(a_list)}")
print(f"Dict: {type(a_dict)}")
