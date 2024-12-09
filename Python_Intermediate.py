#!/usr/bin/env python
# coding: utf-8

# # Basic Dictionary Operations

# ## Exercise 1:
# 
# Create a dictionary with the names of three countries as keys and their capitals as values. Write a program to:
# 
#  • Retrieve the capital of one of the countries.
#  
#  • Add a new country and its capital to the dictionary.

# In[1]:


name = {'Chad':'Njamena', 'Senegal': 'Dakar','South Africa':'Cape Town'}
print(name['Chad'])
name['Rwanda'] = 'Kigali'
print(name)


# ## Exercise 2:
# 
# Modify the dictionary from Exercise 1 by updating the capital of one of the countries. Print the updated dictionary.

# In[2]:


name['Senegal'] = 'Mbour'
print(name)


# # 3 Accessing Values

# ## Exercise 3:
# Write a program where the user inputs a key, and the program retrieves the corresponding value from a predefned dictionary. Include error handling if the key does not exist.
# 
# Hint: Use the .get() method to provide a default value when the key is not
# found

# In[3]:


cle = str(input('input a key please: '))
new_value = name.get(cle, 'Not found')
print(new_value)
print(name.get('France', 'Not found'))


# # 4 Dictionary Methods

# ## Exercise 4:
# 
# Given the dictionary:
# scores = {"Alice": 90, "Bob": 85, "Charlie": 88}
# 
# • Check if “Alice” is in the dictionary.
# 
# • Retrieve and print all keys and values using the appropriate dictionary
# methods.

# In[4]:


scores = {"Alice": 90, "Bob": 85, "Charlie": 88}
print('Alice' in scores)
#print(scores.keys())
keys = list(scores.keys())
print("keys: ", keys)
values = list(scores.values())
print('values:', values)
#paires = scores.items()
#print(paires)
#for keys, values in scores.items():
 #   print(keys, values)
    #print(values)


# # 5 Nested Dictionaries

# ## Exercise 5:
# 
# Create a nested dictionary to represent a simple database of students. Each key should be a student’s name, and the value should be another dictionary containing their age, grade, and favorite subject. For example:
#     
# students = {
# "John": {"age": 15, "grade": "10th", "favorite_subject": "Math"},
# "Jane": {"age": 14, "grade": "9th", "favorite_subject": "Science"}
# }
# 
# Write a program to:
#     
# • Add a new student to the database.
# 
# • Retrieve and print a specifc student’s favorite subject.

# In[10]:


students = {
"John": {"age": 15, "grade": "10th", "favorite_subject": "Math"},
"Jane": {"age": 14, "grade": "9th", "favorite_subject": "Science"},
"Flora":{"age":21, "grade":"1st", "favorite_subject":"Machine learning"}
}
students["Donal"]={"age":28,"grade":"4th","favorite_subject":"Physics"}
print(students)
specific_fav_sub = students["Flora"]["favorite_subject"]
print(f"\nspecific_fav_sub: {specific_fav_sub}")
#for values in students.items():
 #   print(values)


# # 6 Advanced Challenges

# ## Exercise 6:
# 
# Given a dictionary of fruits and their prices:
# fruits = {"apple": 2, "banana": 1, "cherry": 3}
# 
# Write a program that asks the user to input a fruit and checks if it is available.
# If it is, print its price; otherwise, display a message saying it is not available.

# In[6]:


fruits = {"apple": 2, "banana": 1, "cherry": 3}
new_fruit = str(input('Name of a new fruit: '))
print(new_fruit in fruits)
if new_fruit in fruits:
    print( f"The price of {new_fruit} is {fruits[new_fruit]}")
else:
    print(f'{new_fruit} It is not available')


# ## Exercise 7:
#     
# Implement a dictionary-based voting system where:
#     
# • The keys are candidates’ names, and the values are their respective vote
# counts.
# 
# • Users can cast votes by entering a candidate’s name.
# 
# • The program updates the vote count and displays the current standings.

# In[7]:


candidate_vote = {}
for i in range(10):
    candidate_name = str(input('Entrer le nom du candidat: '))
    if candidate_name in candidate_vote:
        candidate_vote[candidate_name] += 1
    else:
        candidate_vote[candidate_name] = 1

print('\nResultats des votes: ')
print("\ncandidate_vote")
for candidate_name, votes in candidate_vote.items():
    print(f"{candidate_name}:{votes} votes")
if candidate_vote:
    winner = max(candidate_vote, key = candidate_vote.get)
    print(f"\nThe winner is {winner} with {candidate_vote[winner]} votes")
else:
    print("No vote registred")

