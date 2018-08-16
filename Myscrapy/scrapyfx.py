import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pad
import seaborn as sns
import numpy as np

sns.set_style('dark')
kf = pad.read_csv('kf.csv')

def sinplotone():
    fig,ax = plt.subplots()
    ax.violinplot(kf['price'])
    plt.show()

def sinplottwo():
    sns.set_style('whitegrid')
    sns.boxplot(kf['price'],palette='deep')
    # sns.despine(left=True)
    plt.show()

def sinplotthree():
    sns.distplot(kf['price'])
    plt.show()

def s():
    df = pad.DataFrame(kf['area'],kf['price'])
    sns.jointplot(x='x',y='y',data=df)
    plt.show()

if __name__ == '__main__':
    fig,ax = plt.subplots()
    ax.scatter(kf['area'],kf['price'],12)
    plt.show()