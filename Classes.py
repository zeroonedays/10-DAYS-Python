# What is classes
# classes are the collection of objects and it's properties.
#Anything that occupies space and has weight is object.
class Man():
    
    """classes for man"""
    
    def __init__(self, name, age, location):
        self.name = name
        self.age = age
        self.location = location
        
    def eat(self):
        print(self.name.title()+' is eating.')
        
    def sleep(self):
        print(self.name.title()+' is sleeping.')
    
    def code(self):
        print(self.name.title()+' is coding.')
        
    def infoman(self):
        print('Name is '+self.name.title())
        print('Age is '+str(self.age))
        print('Lives in '+self.location.title())

man1 = Man('alexa',21,'location')
print(man1.name)
man1.infoman()
man1.eat()

man2 = Man('rahul',22, 'lucknow')
man2.sleep()
