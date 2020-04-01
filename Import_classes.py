#from inheritance import Bike
#from inheritacne import SportsBike

from inheritance import Bike, SportsBike

import_bike = Bike('Pulsar','220', 180000)
import_bike.nameindetail()
print('\n\n')
new_bike = SportsBike('Karizma','ZMR',150000)
new_bike.nameindetail()
new_bike.bikemileage(15)