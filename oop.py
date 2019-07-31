#deine a class and give it an attribute    
class SampleClass:
  pass
  
#define a class,give it an attribute,use init method to create object attributes.this object will be created later 
class Dog:
    Species = 'Mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age

#instantiate SampleClass object,no parameter is passed here
Sample = SampleClass()

#Instantiate the Dog object
philo = Dog("Philo", 5)
mikey = Dog("Mikey", 6)
ben = Dog("tolu",9)
me = Dog("jid",7)
ds = Dog("nb",5)

#using the object(instance of the class) created to  access the class and object attributes using print method
print(mikey.name,mikey.age)
print(ben.name,ben.age)
print(me.name,me.age)
print(ds.name,ds.age
      
def get_biggest_number(*ages):
    u = max(ages)
    print("This is the list out of the listed ages" , u)
       
    
get_biggest_number(4,3,8,9)    
      
#object method
class Dog:

    # Class Attribute
    species = 'mammal'

    # Initializer / Object Attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Object method
    def description(self):
        return "{} is {} years old".format(self.name, self.age)

    # Object method
    def speak(self, sound):
        return "{} says {}".format(self.name, sound)
    
    def description2(self):
        return "{} is {} years old".format(self.name, self.age)

    # Object method
    def speak2(self, sound):
        return "{} says {}".format(self.name, sound)

# Instantiate the Dog object
mikey = Dog("Mikey", 6)

# call our object methods
print(mikey.description())

print(mikey.speak("Gruff Gruff"))

Lucky = Dog("Mohr", 1)

# call our object methods
print(Lucky.description())

print(Lucky.speak2("bark bark"))


      
class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00
    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str
 
car1 = Vehicle()
car1.name="Fer"
car1.color="red"
car1.kind="convertible"
car1.value=60000

car2 = Vehicle()
car2.name="Jump"
car2.color="blue"
car2.kind="van"
car2.value=10000

# test code
print(car1.description())
print(car2.description())      