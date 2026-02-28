from typing import TypedDict

class Person(TypedDict):

    name: str
    age: int

# using the dictionary

new_person : Person = {
   'name': "Jatin",
   'age': 24
}

print(type(new_person))