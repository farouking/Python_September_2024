#I-Update Values in Dictionaries and Lists
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

#1.Change the value 10 in x to 15.
x [1][0]=15
print(x)
#2.Change the last_name of the first student from 'Jordan' to 'Bryant'.
students[0]["last_name"]="Bryant"
print(students)

#In the sports_directory, change 'Messi' to 'Andres'
sports_directory['soccer'][0]="Andres"
print(sports_directory)

#Change the value 20 in z to 30
z[0]['y']=30
print(z)

#II-Iterate Through a List of Dictionaries

def iterateDictionary (my_list) :
    for item in my_list:
        if isinstance(item, dict):#check type of object
            print("Dictionary found:")
            for key, value in item.items():#Return the dictionary's key-value pairs:
                print(f"Key: {key}, Value: {value}")
        else:
            print(f"Non-dictionary item: {item}")

L_1=[{ "brand": "Ford", "model": "Mustang", "year": 1964},{'first_name' : 'John', 'last_name' : 'Rosales'},21,[1,2,4],{"best_Sport":"swiming","height":1.82,"weight":80}]

print(iterateDictionary(L_1))

#III.Get Values From a List of Dictionaries

def iterateDictionary2(key_name, some_list):
    for item in some_list:
        if isinstance(item, dict):  # check type of object
            if key_name in item:    # check if the key exists in the dictionary
                print(f"Value: {item[key_name]}")
            else:
                print(f"Key '{key_name}' not found in the dictionary")
        else:
            print(f"Non-dictionary item: {item}")

print(iterateDictionary2("brand",L_1))
print(iterateDictionary2('first_name',students))

#IV.Iterate Through a Dictionary with List Values
def printInfo(some_dict):
    for key, values in some_dict.items():
        print(f"{len(values)} {key}")
        for value in values:
            print(value)
        print()  # Print a blank line for better readability

print(printInfo(sports_directory))