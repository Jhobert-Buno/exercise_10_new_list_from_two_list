# Exercise 10: Create a new list from two list using the following condition
# Create a new list from two list using the following condition

# Given two list of numbers, write a program to create a new list such that the new list should contain odd numbers from the first list and even numbers from the second list.

#given list
list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]

#result list
result_list = []

#for list 1
for i in list1:
    if i % 2 !=0:
        result_list.append(i)

#for list 2
for i in list2:
    if i % 2 ==0:
        result_list.append(i)

#result
print("Result list: ", result_list)
