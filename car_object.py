class Car:
    
    def __init__(self,price,speed,fuel,mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if(self.price>10000):
            self.tax = 0.15
        else:
            self.tax = .12
    
    def display(self):
        print "Price : {}".format(self.price)
        print "Speed : {}mph".format(self.speed)
        print "Fuel : {}".format(self.fuel)
        print "Mileage : {}mpg".format(self.mileage)
        print "Tax : {}".format(self.tax)
        return self

car1 = Car(2000,35,'Full',15)
print "**************************"
car2 = Car(2000,5,'Not Full',105)
print "**************************"
car3 = Car(2000,15,'Kind of Full',95)
print "**************************"
car4 = Car(2000,25,'Full',25)
print "**************************"
car5 = Car(2000,45,'Empty',25)
print "**************************"
car6 = Car(20000000,35,'Empty',15)

print car1.display()
print car2.display()
print car3.display()
print car4.display()
print car5.display()
print car6.display()