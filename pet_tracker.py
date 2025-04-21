class pet:
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age

    def __str__(self):
        return f"{self.name} is a {self.age} year old {self.species}"
    
    def birthday(self):
        self.age += 1
        
pet1 = pet("Buddy", "dog", 4)
print(pet1)
pet2 = pet("Mittens", "cat", 2)


pet1.birthday()
print(pet1)