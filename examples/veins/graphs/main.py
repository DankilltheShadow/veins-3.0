__author__ = 'Daniel'

import pandas as pd
import math
import matplotlib.pyplot as plt
from pylab import *


def flatten(seq):
    l = []
    for elt in seq:
        t = type(elt)
        if t is tuple or t is list:
            for elt2 in flatten(elt):
                if elt2 > 0:
                    l.append(elt2)
        else:
            l.append(elt)
    return l


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


##############################################
plt.hist2d(xcoordheat, ycoordheat, bins=40)
# figure = plt.figure()
# id = 0
# chsum = chstates.iloc[statestime_index[id]].sum()
# onsum = onstates.iloc[statestime_index[id]].sum()
# fnsum = fnstates.iloc[statestime_index[id]].sum()
#
# plt.pie([fnsum, onsum, chsum], labels=['FN', 'ON', 'CH'], autopct='%1.1f%%', shadow=False, startangle=90)
#
#
# def on_press(event):
#     global id
#     global chsum
#     global onsum
#     global fnsum
#
#     if event.key == u'right' and id < len(statestime_index)-1:
#         event.canvas.figure.clear()
#
#         id += 1
#         chsum += chstates.iloc[statestime_index[id]].sum()
#         onsum += onstates.iloc[statestime_index[id]].sum()
#         fnsum += fnstates.iloc[statestime_index[id]].sum()
#
#         event.canvas.figure.gca().pie([fnsum, onsum, chsum], labels=['FN', 'ON', 'CH'], autopct='%1.1f%%', shadow=False, startangle=90)
#         event.canvas.draw()
#     else:
#         if event.key == u'left' and id >= 0:
#             event.canvas.figure.clear()
#
#             chsum -= chstates.iloc[statestime_index[id]].sum()
#             onsum -= onstates.iloc[statestime_index[id]].sum()
#             fnsum -= fnstates.iloc[statestime_index[id]].sum()
#             id -= 1
#
#             event.canvas.figure.gca().pie([fnsum, onsum, chsum], labels=['FN', 'ON', 'CH'], autopct='%1.1f%%', shadow=False, startangle=90)
#             event.canvas.draw()
#
# figure.canvas.mpl_connect('key_press_event', on_press)
plt.show()
