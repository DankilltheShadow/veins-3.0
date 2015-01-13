__author__ = 'Daniel'

import pandas as pd
from pylab import *
from Utils import *


class Car:
    __data = {}

    def __init__(self, id):
        self.__id = id

    def set_data(self, time, data):
        self.__data[time] = data

    def get_data(self, time, data):
        if time in self.__data.keys():
            return self.__data[time]
        return -1


###importazione dei dati######################
df = pd.read_csv('..\\results\\nodebug-0.csv', header=0)
#df.fillna(0, inplace=True)
df.rename(columns=lambda x: x.replace('RSUExampleScenario.node', 'Car'), inplace=True)
df.rename(columns=lambda x: x.replace('appl/', ''), inplace=True)
beaconinterval = 10  #frequenza di taglio per la raccolta di statistiche. E' il beaconInterval nel .ini
time = df.filter(regex="X")
chstates = df.filter(regex="CH state")
onstates = df.filter(regex="ON state")
fnstates = df.filter(regex="FN state")
statestime_index = time.select(lambda x: math.fmod(time.iloc[x].sum(), (beaconinterval/2)) == 0).index.tolist()
xcoord = df.filter(regex="Posizione x")
ycoord = df.filter(regex="Posizione y")
xcoordheat = xcoord.select(lambda x: x not in statestime_index)
ycoordheat = ycoord.select(lambda y: y not in statestime_index)
xcoordheat = flatten([tuple(z) for z in xcoordheat.values])
ycoordheat = flatten([tuple(v) for v in ycoordheat.values])

#for index, row in time.iterrows():
#    if row.values > 100:
#        print 'y'
# for index, row in chstates.iterrows():
#     asd = row['Car[33].CH state']
#     print asd, index
# for r in chstates.itertuples():
#     print r
# for col in chstates.columns:
#     print col
dictchstates = {}
dictonstates = {}
dictfnstates = {}
dictfnstates = {}