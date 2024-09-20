#1-Countdown 

def countdown(n):
    result = []
    for i in range(n, -1, -1):
        result.append(i)
    return result
# Test the function
print(countdown(10))

#2-Print and Return 

def print_and_return(my_list):
    # Print the first value
    print(my_list[0])
    # Return the second value
    return my_list[1]
# Test the function
result = print_and_return([1, 2])
print("Returned value:", result)

#3-First Plus Length:Create a function that accepts a list and returns the sum of the first value in the list plus the list's length.

def First_Plus_Length(mylist):
        sumlsit=mylist[0]+len(mylist)
        print ("the sum of the first value in list and the list lenght is",sumlsit)

# Test the function       
print(First_Plus_Length([5,5,5,99,7]))

#4-Values Greater than Second 

def values_greater_than_second(list1):
    if len(list1) > 2:
        count = 0
        list2 = []
        for i in range(len(list1)):
            if list1[i] > list1[1]:
                list2.append(list1[i])
                count += 1
        print(f"The second value in the original list is {list1[1]} and the list contains {count} values greater than it.")
        print("The new list is", list2)
    else:
        print("False")

# Test the function       
values_greater_than_second([1, 0, 5, 2, 2, 33, 4])  # Example list

#5-This Length, That Value of my list
def seize_value_list(seizelist, valuelist):
    ls = []
    for i in range(seizelist):
        ls.append(valuelist)
    print("The list generated is:", ls)
# Test the function       
seize_value_list(7,7)