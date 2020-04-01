#import inheritance

import inheritance, Classes,Bike

new_bike_1 = inheritance.Bike('Glamour','160',120000)
new_bike_1.nameindetail()

print('\n\n')
new_man = Classes.Man('Shaan',22, 'Lucknow')
new_man.eat()
print('\n\n')
new_bike_2 = Bike.Bike('Discover','150', 120000)
new_bike_2.printprice()