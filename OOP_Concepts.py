# class Car:
#     def __init__(self, start, stop):
#         self.start = start
#         self.stop = stop
    
#     def brand(self):
#         print("Audi")
        
#     def color(self):
#         print("Black")
        
#     def move(self):
#         print("Move")
        
# # A constructor is a function that gets called at the time of creating an object.

# car = Car("Start", "Stop")
# car.start = "start"
# print(car.start)

#-----------Exercise-----------#

# class Dog:
#     def __inint__(self, breed):
#         self.breed = breed
    
#     def bark(self):
#         print("Bark")
        
#     def introduction(self):
#         print(f"This is a {self.breed}")
        
# dog = Dog("German Shepherd")
# dog.introduction()
# dog2 = Dog("BullDog")
# dog2.introduction()

#---------------Magic/Dunder Methods---------------#

class MagicMethods:
    x = 5 + 3
    y = (5).__add__(3)
    name1 = "John Shelby".__repr__()
    name2 = "Finn Shelby"
    print(name1)
    print(name2)
    
MagicMethods()