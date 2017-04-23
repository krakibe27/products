class Product:

    def __init__(self,price,itemName,weight,brand,cost):
        self.price = price
        self.itemName = itemName
        self.weight = weight
        self.brand = brand
        self.cost = cost
        self.status = 'for sale'
    
    def displayInfo(self):
        print 'Price :',self.price
        print 'itemName :',self.itemName
        print 'Weight :',self.weight
        print 'Brand :',self.brand
        print 'Cost :',self.cost
        print 'Status :',self.status
        return self
    
    def sell(self):
        print 'After selling'
        self.status = 'sold'
        #print 'Status :',self.status
    
        return self
    
    def addTaxWithTotalAmount(self,tax):
        total = self.price*tax + self.price
        print "Tax= {} ".format(tax)  + "Total Price : {}".format(total)
        return self
    
    def returnItem(self,ret):
        print "after return"
        if (ret == 'defective'):
            self.status = 'defective'
            self.price = 0
        self.displayInfo()
        return self


def main():
    prd1 = Product(2000,'Laptop','1.2Lb','Mac',1000)
    print prd1.displayInfo()
    print prd1.sell().displayInfo().addTaxWithTotalAmount(.10)
    print prd1.returnItem('defective')
   
    #print prd1.addTaxWithTotalAmount(.10).sell()
  

if __name__=="__main__":
    main()


