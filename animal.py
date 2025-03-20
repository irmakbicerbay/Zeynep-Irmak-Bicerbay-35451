class Animal:
    def __init__(self, name, group, number_of_legs, skills):
        self.name = name
        self.group = group
        self.number_of_legs = number_of_legs
        self.skills = skills
    
    def __repr__(self):
        return f"Animal(name='{self.name}', group='{self.group}', number_of_legs={self.number_of_legs}, skills={self.skills})"

cat = Animal("Cat", "Mammals", 4, ["jumping", "climbing", "hunting"])
dog = Animal("Dog", "Mammals", 4, ["running", "digging", "loyalty"])
rabbit = Animal("Rabbit", "Mammals", 4, ["jumping", "digging", "fast running"])
eagle = Animal("Eagle", "Birds", 2, ["flying", "hunting", "sharp vision"])
snake = Animal("Snake", "Reptiles", 0, ["slithering", "camouflage", "venomous bite"])

animals = [cat, dog, rabbit, eagle, snake]

for animal in animals:
    print(animal)
