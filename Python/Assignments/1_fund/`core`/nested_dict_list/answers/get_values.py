students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]

# Create a function iterateDictionary2(key_name, some_list) that, given a list of dictionaries and a key name, the function prints the value stored in that key for each dictionary.

def iterateDictionary2(key_name, given_list):
    for each_dict in given_list:
        print(each_dict[key_name])

iterateDictionary2('first_name', students)