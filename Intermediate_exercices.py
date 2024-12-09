
name = {'Chad':'Njamena', 'Senegal': 'Dakar','South Africa':'Cape Town'}
print(name['Chad'])
name['Rwanda'] = 'Kigali'
print(name)
name['Senegal'] = 'Mbour'
print(name)
cle = str(input('input a key please: '))
print(name[cle])
print(name.get('France', 'Not found'))


scores = {"Alice": 90, "Bob": 85, "Charlie": 88}
print('Alice' in scores)
#print(scores.keys())
key = scores.keys()
print(key)
value = scores.values()
print(value)
#paires = scores.items()
#print(paires)
#for keys, values in scores.items():
 #   print(keys, values)
    #print(values)

students = {
"John": {"age": 15, "grade": "10th", "favorite_subject": "Math"},
"Jane": {"age": 14, "grade": "9th", "favorite_subject": "Science"},
"Flora":{"age":21, "grade":"1st", "favorite_subject":"Machine learning"}
}
students["Donal"]={"age":28,"grade":"4th","favorite_subject":"Physics"}
print(students)
specific_fav_sub = students["Flora"]["favorite_subject"]
print(specific_fav_sub)
#for values in students.items():
 #   print(values)


fruits = {"apple": 2, "banana": 1, "cherry": 3}
new_fruit = str(input('Name of a new fruit: '))
print(new_fruit in fruits)
if new_fruit in fruits:
    print( fruits[new_fruit])
else:
    print('It is not available')


candidate_vote = {}
for i in range(10):
    candidate_name = str(input('Entrer le nom du candidat: '))
    if candidate_name in candidate_vote:
        candidate_vote[candidate_name] += 1
    else:
        candidate_vote[candidate_name] = 1

print('Resultats des votes: ',candidate_vote)
for candidate_name, votes in candidate_vote.items():
    print(f"{candidate_name}:{votes} votes")
if candidate_name in candidate_vote:
    winner = max(candidate_vote, key = candidate_vote.get)
    print(f"The winner is {winner} with {candidate_vote[winner]}votes")
else:
    print("No vote registred")