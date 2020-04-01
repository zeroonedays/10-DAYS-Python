""" classes for bike """
class Bike():
    
    def __init__(self, name, model, price):
        self.name = name
        self.model = model
        self.price = price
        self.odometer = 0
        
    def nameindetail(self):
        print('Bike name is '+self.name)
        print('Model is '+self.model)
        
    def distancetravelled(self):
        #self.odometer = 100
        print('Bike has run '+str(self.odometer)+ ' km.')
        
    def update_odometer(self, distance):
        self.odometer += distance
        
    def printprice(self):
        print('Price is '+str(self.price))
        
class SportsBike(Bike):
    
    def __init__(self, name, model, price):
        super().__init__(name, model, price)
        self.mileage = 0

    
    def bikemileage(self, distan):
        self.mileage = distan
        print('My bike mileage is '+str(self.mileage)+' km.')
        
            
bike_1 = Bike('apache','180',110000)
#bike_2 = SportsBike('Yamaha','R 15', 180000)
bike_3 = SportsBike('Ducati','750', 500000)

print('My sports bike is '+bike_2.name+' .')
bike_2.distancetravelled()
bike_2.update_odometer(100)
bike_2.distancetravelled()
bike_2.bikemileage()

#bike_3.nameindetail()
#bike_3.bikemileage(50)