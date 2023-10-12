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
################################################# Update Values
    # 1) x value 10 to 15
x[1][0] = 15
print(x)

    # 2) Michael's last name to "Bryant"
students[0]['last_name'] = "Bryant"
print(students)

    # 3) Messi to Andres
sports_directory['soccer'][0] = "Andres"
print(sports_directory)

    # 4) z's value 20 to 30
z[0]['x'] = 30
print(z)



################################################# Iterate
print("################ Iterate")
    # Function iterate_dict(some_list) prints every key-value pair in each dict list
def iterate_dict(some_list):
    return "starting over"

print(f"students: {iterate_dict(students)}")
print(f"students: {iterate_dict(sports_directory)}")


