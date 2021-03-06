
# Instructions:
# Work through the following prompts. Prompts marked with "We Do", we will work
# on together, as a class; prompts marked with "You Do", you will be given time
# to work through on your own.
#
# Tip: comment out your solution to each prompt before moving on to the next
# one! This will keep your console clear.
#

#
# Prompt 1: We Do
#
# Define a class for a Car. Your Car class should have the following
# properties:
#
#    - make
#    - model
#    - color
#
# Your Car class should have the following methods:
#
#    - drive: print 'vroom vroom' to the console
#
# Once you create your class definition create two instances.
#


# define a class 

class Car:   

 # properties - Given: Make, Model, Color
    
    def __init__(self, make, model, color):
        self.make = make
        self.model = model
        self.color = color
        
    def __str__(self):
        return f"{self.make} {self.model} {self.color}"

# Method is called given: drive 
    def drive(self):
        return ('Vroom Vroom')
        # print("Vroom Vroom")
  

# Create 2 Instancs 

instance1 = Car("Ford","Chrysler","Tesla")
instance2 = Car("Ranger", "Dodge", "Toyota")


# Print Out
print(instance1.drive())
print(instance2.drive())
print(instance1)
print(instance2)

     

#
# Prompt 2: We Do
#
# We're going to modify our Car class from the previous prompt and extend it to
# create a Toyota class:
#
#   - Extend your Car class to create a Toyota class. The make property will always
#     be 'Toyota'. Add a drive method to your Toyota class.
#
# Make an instance of your Toyota class.
#

# Create a Toyota Class (extend to Car Class)
class Toyota(Car):
    
    def __init__(self, make, model, color):
        
        # The property MAKE is set to Toyota
        super().__init__("Toyota", model, color)	
      

# Add a Drive Method to your Toyota Class
    def drive(self):
        return("Toyota Is a Nice Vehicle")
        
 # make 1 Instance but MAKE is always Toyota

instanceOne = Toyota("MAKE is alway TOYOTA","Minivan","Car")

# Print out 
print(instanceOne.drive())
print(instanceOne)



#
# Prompt 3: You Do
#
# Define a class for your favorite animal (dog, cat, giraffe, etc). Give your
# class 3 attributes and two methods.
#
# After you've defined your class, create 3 instances.
#


# define a class 

class Dog:   

 # properties Need 3 Attributes- breed, color, size
    
    def __init__(self, breed, color, size ):
        self.breed = breed
        self.color = color
        self.size = size
        
    def __str__(self):
        return f"{self.breed} {self.color} {self.size}"

# Method 1is called style
    def style(self):
       return("I love small Poodles")
  
    # Method 2 is called owner
    def owner(self):
        print("Great Owners love Dogs")
        
  # make 2 Instancs 

ins1 = Dog ("poodles","german Shephard", "bulldog")
ins2 = Dog ("retriever", "Lab","Husky")
ins3 = Dog ("Greyhound","Dane","Pomerian")


# Print Methods Comments
print(ins1.style())
print(ins2.owner())

# Print Instances 
print(ins1)
print(ins2)
print(ins3)



# Prompt 4: You Do
#
# Once we've completed the above, work through the following changes to your
# Car and Toyota classes:
#
#   - move the color property to your Toyota class
#   - move the drive method to your Car class
#   - add a property to your Toyota class
#   - add a property to your Car class and "fill it in" for your Toyota class
#

#
# Prompt 5: You Do
#
# Define and Animal class with the following properties and methods:
#
#   - group (Invertebrates, Fish, Amphibians, Reptiles, Birds, and Mammals)
#   - eat: log "yum yum" to the console
#   - sleep: log "zzzzz" to the console
#
# Modify your animal from the previous prompt so that it extends your new
# Animal class.
#
# Create an instance of your animal class (the one that extends the Animal
# class).
#

#
# Prompt 6: You Do
#
# Define a Card class with the following properties:
#
#   - suit (hearts, spades, clubs, diamonds)
#   - rank (Ace, 2, 3, 4, .. Jack, King, Queen)
#   - score (1, 2, 3, 4, ... 11, 12, 13)
#
# Define a Deck class with the following properties and methods:
#
#   - length (the number of cards - should start at 52)
#   - cards (an array of cards in the deck)
#   - draw: return a random card from the cards array
#
# When you create an instance of your Deck class (i.e. in your constructor),
# fill in the cards array with 52 instances of your Card class. You can do
# this with a nested for loop - first loop through an array of all possible
# suits, then loop through an array of all possible ranks. Inside your inner
# loop, create an instance of your Card class and push it into the Deck's cards
# array.
#
# Instantiate an instance of your Deck and start drawing random cards!
#
