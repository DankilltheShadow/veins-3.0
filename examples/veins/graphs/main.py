__author__ = 'Daniel'

import pandas as pd
import math
import matplotlib.pyplot as plt
import pylab
import time as tm
pylab.ion()

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


def get_fig(some_data, some_labels, title):
    ax = fig.add_subplot(111)
    ax.set_ylim([0.1, 0.8])
    ax.set_xlim([0.1, 0.8])
    ax.set_title(title)
    ax.pie(some_data, labels=some_labels, autopct='%1.1f%%', shadow=False, startangle=90)

my_labels = 'FN', 'ON', 'CH'
fig = pylab.figure(figsize=(8, 8), frameon=False)
chsum = 0.0
fnsum = 0.0
onsum = 0.0

for i in range(0, len(time.index)):
    if math.fmod(time.iloc[i].sum(), (beaconinterval/2)) == 0:
        fig.clear()
        title = str(time.iloc[i].sum())
        chsum += chstates.iloc[i].sum()
        onsum += onstates.iloc[i].sum()
        fnsum += onstates.iloc[i].sum()

        data = [fnsum, onsum, chsum]

        get_fig(data, my_labels, title)
        fig.canvas.draw()
        pylab.draw()
        tm.sleep(1)

pylab.show()