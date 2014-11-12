__author__ = 'Daniel'

import pandas as pd
import matplotlib.pyplot as plt

def graph():
    df = pd.read_csv('..\\results\\nodebug-0.csv', header=0)
    df.rename(columns=lambda x: x.replace('RSUExampleScenario.node', 'Car'), inplace=True)
    df.rename(columns=lambda x: x.replace('appl/', ''), inplace=True)

    chchannels = df.filter(regex="CH state")
    chsum = chchannels.sum().sum()
    onchannels = df.filter(regex="ON state")
    onsum = onchannels.sum().sum()
    fnchannels = df.filter(regex="FN state")
    fnsum = fnchannels.sum().sum()

    labels = 'FN', 'ON', 'CH'
    sizes = [fnsum, onsum, chsum]
    colors = ['yellowgreen', 'lightskyblue', 'lightcoral']
    explode = (0, 0, 0)

    plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=90)

    plt.axis('equal')

    plt.show()

graph()