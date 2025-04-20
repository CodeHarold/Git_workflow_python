class Animal:
    def speak(self):
        return "I make a sound"

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

class Bird(Animal):
    def speak(self):
        return "Chirp!"
    
class Fish(Animal):
    def speak(self):
        return "Blub!"

class Cow(Animal):
    def speak(self):
        return "Moo!"
       

    
def animal_sound(animal: Animal):
    print(animal.speak())

# Demonstrating Polymorphism
dog = Dog()
cat = Cat()
bird = Bird()
fish = Fish()
cow = Cow()


animal_sound(dog)  # Output: Woof!
animal_sound(cat)  # Output: Meow!
animal_sound(bird)  # Output: Chirp!
animal_sound(Fish())  # Output: Blub!
animal_sound(cow)  # Output: Moo!

