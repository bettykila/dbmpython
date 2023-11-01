#Question 1. 
#Creat a variabe x that holds string value Hello
x = "Hello"
print(x + " Betty")

#Question 2. 
print (x[0])
print (x[1])

#Question 3. 
x = "hello world"
s = x [0:3]
print (s)
s = x [:3]
print (s)

#Question 4.
myname = "Joe"
print("Welcome " + myname + " to CCDM course")

#List
# A list with 3 integers
numbers = [1, 2, 5]
print(numbers)

#Q1. Create a list called courses
courses = ["CCDM", "CCIT", "CCLSA", "CCNS"]
print(courses)

#Q2. Access the second last course.
print (courses[-2]) #CCLSA

#slicing
my_list = ['p','r','o','g','r','a','m','i','z']

# items from index 2 to index 4
print(my_list[2:5])

# items from index 5 to end
print(my_list[5:])

# items beginning to end
print(my_list[:])

# Using the append method to inser values into a list

courses.append("CCAIT")
print(courses)

#Python List Length
list = [ "New York", "Los Angles", "Boston", "Denver" ]
print(list) # prints all elements
print(list[0]) # print first element

#Exercise 1
languages = ['Python', 'Swift', 'C++']
print("List: ", languages)
print("Total Elements: ", len(languages)) # 3

list2 = [1,3,4,6,4,7,8,2,3]
print(sum(list2))
print(min(list2))
print(max(list2))
print(list2[0])
print(list2[-1])
