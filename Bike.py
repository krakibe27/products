class Bike:

    def __init__(self,price,max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 200
        #self.miles = self.miles + self.miles
    
    def displayInfo(self):
        print "Price :", self.price
        print "max_speed :" + self.max_speed
        print "total miles :", self.miles
        return self  

    def ride(self):
        k = self.miles/10

        for i in range(10,self.miles,10):
            
            #k = self.miles/10
            print "Miles increased by :", i
        return self

    def reverse(self):
        for i in reversed(range(10,self.miles,10)):
            print "Reversed Miles by 10 :", i
        return self

bike1 = Bike(200,'10 mph')

#print bike1.displayInfo().ride().reverse()
print bike1.displayInfo()
