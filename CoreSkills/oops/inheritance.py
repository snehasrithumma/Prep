class Animal:
    def speak(self):
        return 'makes sound'
    
class Dog(Animal):
    def speak(self):
        return 'Woof'
    
class Cat(Animal):
    def speak(self):
        return 'meow'
    
class PetOwner:
    def __init__(self, pet) -> None:
        self.pet = pet

    def pet_speak(self):
        return self.pet.speak()
    
aniaml = Animal()
dog = Dog()
cat = Cat()

print(aniaml.speak())
print(dog.speak())
print(cat.speak())

dog_owner = PetOwner(dog)
cat_owner = PetOwner(cat)
print(dog_owner.pet_speak())
print(cat_owner.pet_speak())