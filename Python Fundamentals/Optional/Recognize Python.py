#--variable declaration--#
#--Numbres--#
num1 = 42
num2 = 2.3
#--Boolean--#
boolean = True
#--Strings--#
string = 'Hello World'
#--List--#
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']
#--Dictionary--#
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}
#--Tuple--#
fruit = ('blueberry', 'strawberry', 'banana')
#--Asking about type of fruit=tuple(immutable--#
print(type(fruit))
#--Asking about type of fruit=tuple(immutable--#
print(pizza_toppings[1])#Sausage#
pizza_toppings.append('Mushrooms')#Adding new topping #
print(person['name'])#access value#
person['name'] = 'George'#modify value# modifying Name Jhon by George#
person['eye_color'] = 'blue'#modify value#modifying eye color#
print(fruit[2])#access value##Banana#
#--Conditionnal--#
if num1 > 45:
    print("It's greater")
else:
    print("It's lower")

if len(string) < 5:
    print("It's a short word!")
elif len(string) > 15:
    print("It's a long word!")
else:
    print("Just right!")

 #for loop#
for x in range(5):
    print(x)
for x in range(2,5):
    print(x)
for x in range(2,10,3):
    print(x)
x = 0
#- while loop#
while(x < 5):
    print(x)
    x += 1

pizza_toppings.pop()
#The pop() method removes the element at the specified position.
pizza_toppings.pop(1)

print(person)
person.pop('eye_color')
print(person)

for topping in pizza_toppings:
    if topping == 'Pepperoni':
        continue
    print('After 1st if statement')
    if topping == 'Olives':
        break
#- function#
def print_hello_ten_times():
    for num in range(10):
        print('Hello')

print_hello_ten_times()

def print_hello_x_times(x):
    for num in range(x):
        print('Hello')

print_hello_x_times(4)

def print_hello_x_or_ten_times(x = 10):
    for num in range(x):
        print('Hello')

print_hello_x_or_ten_times()
print_hello_x_or_ten_times(4)


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)