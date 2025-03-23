# 1 Classes and Objects
# Define a class (blueprint)
class Drone:
    # Constructor: a special method that is called when an object is created, in other words, a special method to initialize properties
    def __init__(self, model, usage):
        self.model = model # property 1
        self.usage = usage # property 2

    # Define an action for the drone to perform, such as flying
    def fly(self):
        print(f"{self.model} is flying")

    def neutrelize(self):
        print(f"{self.model} is neutrlizing the threat")

# Create objects (instances of the class)
drone1 = Drone("SR1", "surveillance")
drone2 = Drone("SR2", "security")

# Access properties and call methods
print(f"{drone1.model} is for {drone1.usage}")
print(f"{drone2.model} is for {drone2.usage}")

# Call the fly method and neutrelize method
drone1.fly()
drone2.neutrelize()


#2 Encapsulation
# Encapsulation is the bundling of data (properties) and methods that operate on the data into a single unit (class). It restricts direct access to some of an object's components.
# Encapsulation is used to protect the data from accidental corruption.
# Public attributes: Accessible from anywhere (e.g., self.name).
# Private attributes: Marked with _ or __ to indicate they shouldn’t be accessed directly (but Python doesn’t enforce strict privacy)

class Investment:
    def __init__(self, principal, rate, time):
        self.__principal = principal # private property
        self.__rate = rate # private property
        self.__time = time # private property

    # Define a method to calculate the interest
    def interest(self):
        print(f"Interest: {self.__principal * self.__rate * self.__time}")

# Create an object
investment = Investment(1000, 0.05, 2)

investment.interest() # Access the method to calculate the interest 


#3 Inheritance
# Inheritance is a mechanism in which a new class (child) inherits properties and methods from an existing class (parent).
# We will use the Drone class from earlier as the parent class and create a child class called Quadcopter.
# The Quadcopter class will inherit the properties and methods from the Drone class.
class Drone: # Parent class
    def __init__(self, model, usage):
        self.model = model # property 1
        self.usage = usage # property 2

# Child class
class Recondrone(Drone):  # Recondrone is a child class of Drone
    def __init__(self, model, usage):
        super().__init__(model, usage)  # Call the parent class constructor

    def fly(self):
        print(f"{self.model} is flying and performing reconnaissance.")

    def scan(self):
        return f"{self.model} is conducting a scan of the suspected area."


# Create objects (instances of the class)
recondrone = Recondrone("RD01", "reconnaissance")

# Call methods on the object
recondrone.fly()
print(recondrone.scan())
    
    
        