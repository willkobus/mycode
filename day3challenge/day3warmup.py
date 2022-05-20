#!/usr/bin/env python3

# dictionary that contains a list of dictionaries containing student info
classinfo = {'all': [
         {'name': 'Cat',
          'skill level': 'amazing',
          'spirit animal': 'Chinchilla',
          'super power': 'Body Part Substitution'},
         {'name': 'Chris',
          'skill level': 'astonishing',
          'spirit animal': 'Chipmunk',
          'super power': 'Camouflage'},
         {'name': 'Dao',
          'skill level': 'astounding',
          'spirit animal': 'Clam',
          'super power': 'Bone Manipulation'},
         {'name': 'David',
          'skill level': 'awe-inspiring',
          'spirit animal': 'Clownfish',
          'super power': 'Claw Retraction'},
         {'name': 'Henwin',
          'skill level': 'breathtaking',
          'spirit animal': 'Cobra',
          'super power': 'Deflection'},
         {'name': 'Herman',
          'skill level': 'imposing',
          'spirit animal': 'Condor',
          'super power': 'Fang Retraction'},
         {'name': 'Jose',
          'skill level': 'inspiring',
          'spirit animal': 'Constrictor',
          'super power': 'Helicopter Propulsion'},
         {'name': 'Justin',
          'skill level': 'magnificent',
          'spirit animal': 'Coral',
          'super power': 'Invisibility'},
         {'name': 'Kris',
          'skill level': 'majestic',
          'spirit animal': 'Cougar',
          'super power': 'Immobility'},
         {'name': 'Mannie',
          'skill level': 'miraculous',
          'spirit animal': 'Coyote',
          'super power': 'Immutability'},
         {'name': 'Marcos',
          'skill level': 'spectacular',
          'spirit animal': 'Crab',
          'super power': 'Invulnerability'},
         {'name': 'Marshall',
          'skill level': 'staggering',
          'spirit animal': 'Crane',
          'super power': 'Jet Propulsion'},
         {'name': 'Michael',
          'skill level': 'stunning',
          'spirit animal': 'Crawdad',
          'super power': 'Invulnerability'},
         {'name': 'Mike',
          'skill level': 'stupefying',
          'spirit animal': 'Crocodile',
          'super power': 'Muscle Manipulation'},
         {'name': 'Nikko',
          'skill level': 'sublime',
          'spirit animal': 'Crow',
          'super power': 'Needle Projection'},
         {'name': 'Phil',
          'skill level': 'wonderful',
          'spirit animal': 'Cuckoo',
          'super power': 'Prehensile Tongue'},
         {'name': 'Ryan',
          'skill level': 'wondrous',
          'spirit animal': 'Cicada',
          'super power': 'Regenerative Healing Factor'},
         {'name': 'Sachin',
          'skill level': 'affecting',
          'spirit animal': 'Damselfly',
          'super power': 'Replication'},
         {'name': 'Samekh',
          'skill level': 'arresting',
          'spirit animal': 'Deer',
          'super power': 'Self-Detonation'},
         {'name': 'Will',
          'skill level': 'august',
          'spirit animal': 'Dingo',
          'super power': 'Super Strength'}]}

# prints my name
print("Just my first name")
print(f"{classinfo['all'][-1]['name']}\n")

# prints my name and spirit animal in a more complex string
print("My name and super power in a formatted string")
print(f"My name is {classinfo['all'][-1]['name']} and my spirit animal is....ugh...a {classinfo['all'][-1]['spirit animal']}\n")

# loops through list all inside dictionary classinfo until it finds my name
# when name is found it grabs name, skill level, spirit animal, and super power based on the current student (in this case me) and is used in the formatted string
print("Used loop to find me in 'classinfo' and then details grabbed and displayed in formatted string")
for student in classinfo['all']:
    if student['name'] == "Will":
        print(f"{student['name']}, an {student['skill level']} {student['spirit animal']} of a programmer, possesses {student['super power']} for moonlighting as a superhero!\n")

# loops through list and prints everyones details
print("Used loop to find all students in 'classinfo' and then details grabbed and displayed in formatted string")
for student in classinfo['all']:
        print(f"{student['name']}, a(n) {student['skill level']} {student['spirit animal']} of a programmer, possesses {student['super power']} for moonlighting as a superhero!\n")
