from csv import reader
dogs = []

class Dog:
    def __init__(self, index, name, breed):
        self.index = index
        self.name = name
        self.breed = breed
    def __str__(self) -> str:
        return f"This is {self.name}. They are a(n) {self.breed}."

with open("dogs.csv") as csv_file:
    csv_reader = reader(csv_file, delimiter=",")
    for index, name, breed, in csv_reader:
        dogs.append(Dog(index, name, breed))

for dog in dogs:
    print(dog)