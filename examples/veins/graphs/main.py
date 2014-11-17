__author__ = 'Daniel'

import pandas as pd
import math
import matplotlib.pyplot as plt
import pylab
import time as tm

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
##############################################

figure = plt.figure()
# plotting
chsum = 0.0
fnsum = 0.0
onsum = 0.0

for i in range(0, len(time.index)):
    if math.fmod(time.iloc[i].sum(), (beaconinterval/2)) == 0:
        chsum += chstates.iloc[i].sum()
        onsum += onstates.iloc[i].sum()
        fnsum += fnstates.iloc[i].sum()

        index = i
        break

plt.pie([fnsum, onsum, chsum], labels=['FN', 'ON', 'CH'], autopct='%1.1f%%', shadow=False, startangle=90)


def on_press(event):
    global index
    global chsum
    global onsum
    global fnsum
    if event.key == u'right':
        event.canvas.figure.clear()
        for c in range(index+1, len(time.index)):
            if math.fmod(time.iloc[c].sum(), (beaconinterval/2)) == 0:
                chsum += chstates.iloc[c].sum()
                onsum += onstates.iloc[c].sum()
                fnsum += fnstates.iloc[c].sum()

                index = c
                break
        event.canvas.figure.gca().pie([fnsum, onsum, chsum], labels=['FN', 'ON', 'CH'], autopct='%1.1f%%', shadow=False, startangle=90)
        event.canvas.draw()
    else:
        if event.key == u'left':
            event.canvas.figure.clear()
            for c in range(index, -1, -1):
                if math.fmod(time.iloc[c].sum(), (beaconinterval/2)) == 0:
                    chsum -= chstates.iloc[c].sum()
                    onsum -= onstates.iloc[c].sum()
                    fnsum -= fnstates.iloc[c].sum()

                    index = c-1
                    break
            event.canvas.figure.gca().pie([fnsum, onsum, chsum], labels=['FN', 'ON', 'CH'], autopct='%1.1f%%', shadow=False, startangle=90)
            event.canvas.draw()

figure.canvas.mpl_connect('key_press_event', on_press)
plt.show()
