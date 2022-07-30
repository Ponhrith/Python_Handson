class Car:
    def brand(self):
        print("Audi")
        
    def color(self):
        print("Black")
        
car = Car() #Object
car.brand() #magic method or dundes
car.start = "Start"
car.stop = car.start
print(car.start)
car2 = Car()
car2 = Car()
car2.stop = "Stop"
print(car2.stop) 