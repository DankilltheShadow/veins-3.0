__author__ = 'Daniel'

import pandas as pd

def graph():
    df = pd.read_csv('..\\results\\nodebug-0.csv', header=0)
    df.rename(columns=lambda x: x.replace('RSUExampleScenario.node','Car'), inplace=True)
    df.rename(columns=lambda x: x.replace('appl/',''), inplace=True)

    print df

graph()