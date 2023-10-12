x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]


################################################# Iterate
print("################################ Iterate_dict")

################################################# List to dictionary

# Function iterate_dict(given_list) prints every key-value pair in each dict list
def iterate_dict(given_list):
    for each_dict in given_list:
        print(f"first_name - {each_dict['first_name']}, last_name - {each_dict['last_name']}")

iterate_dict(students)


# EXTRA: Function iterate_list_or_dict(given_list) prints values nested within lists and dictionaries. 
def iterate_list_or_dict(given_list):
    if type(given_list) == type([]):
        for i in given_list:
            if type(i) == type([]):
                for inner_i in i:
                    print(f"{i} in given_list is a LIST")
            elif isinstance(i, dict):
                print(f"{i} in given_list is a DICT")
    elif isinstance(given_list, dict):
        print("Given_list is a DICT")



################################################# Dictionary to list
print("################################ print_info")

# Create a function printInfo(some_dict) that given a dictionary whose values are all lists, prints the name of each key along with the size of its list, and then prints the associated values within each key's list. For example:
def print_info(given_dict):
    for key in given_dict.keys():
        print(f"{key}: {len(given_dict[key])}")
        for each_value in given_dict[key]:
            print(each_value)
        print("\n")

print_info(sports_directory)



























#     if type(given_list) == list:
#         for item in given_list:
#             if type(item) == list:
#                 print("Item is a LIST and needs to print like english")
#             elif type(item) == dict:
#                 print("Item is a DICT and needs to print like english")


#     elif type(given_list) == dict:
#         for item in given_list:
#             print(f"Key is: {item}, Value is: {given_list[item]}")

# iterate_dict(students)
# iterate_dict(sports_directory)

# iterate_dict(x)
# iterate_dict(z)

# # Dict needs KEYS
# # Lists need INDICES

# #################>>>>>>>>>>>>>>>>>>> next step: look up "map" for python <3


































# Function iterate_dict(some_list) prints every key-value pair in each dict list
# def iterate_dict(some_list):
#     for each_item in some_list:
        # print(each_item.keys())


# print(f"students: {iterate_dict(students)}")
# print(f"students: {iterate_dict(sports_directory)}")
