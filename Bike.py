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
        
        
bike_1 = Bike('apache','180',110000)

bike_1.printprice()
print('My bike is '+bike_1.name+ ' '+ bike_1.model)

bike_2 = Bike('yamaha','R 15', 180000)
print('Your bike is '+bike_2.name + ' '+bike_2.model+ '.')
print('Your bike price is '+str(bike_2.price))

bike_1.distancetravelled()
bike_1.odometer = 200
bike_1.distancetravelled()
bike_1.update_odometer(800)
bike_1.distancetravelled()
bike_1.update_odometer(500)
bike_1.distancetravelled()
