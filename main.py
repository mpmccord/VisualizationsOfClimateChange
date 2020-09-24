import matplotlib.pyplot as plt
import matplotlib
import numpy as np 
import seaborn as sns
import pandas as pd
import os
import matplotlib.dates as dates
import scipy.stats
def getPath(myfile):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(dir_path, myfile)
    return file_path
def graphAllData(myDataFrame, X, Y):
    plt.plot((X),(Y))
    plt.show()
def scatterPlot(df, X, Y):
    scipy.stats.linregress(X, df.index.to_pydatetime)
    sns.scatterplot(x=df.getloc(X), y=df.getloc(Y), data=df)
    plt.show()
def getMeans(df):
    return df.groupby(pd.Grouper(key='dt', freq='A')).mean().dropna()
def getStDev(df):
    return df.groupby(pd.Grouper(key='dt', freq='A')).std().dropna()
def getVar(df):
    return df.groupby(pd.Grouper(key='dt', freq='A')).var().dropna()
def getCov(df):
    return df.groupby(pd.Grouper(key='dt', freq='A')).cov().dropna()
def graphClimateChange():
    globalTemp = pd.read_csv(getPath("GlobalLandTemperaturesbyState.csv"))
    flTemp = globalTemp[globalTemp['State'] == 'Florida']
    # graphAllData(flTemp, flTemp['dt'], flTemp['AverageTemperature'])
    flTemp['dt'] = pd.to_datetime(flTemp['dt'])
    flMeans = getMeans(flTemp)
    flMeans['dt'] = flMeans.index
    scatterPlot(flMeans, flMeans['dt'], flMeans['AverageTemperature'])
    plt.show()
    globalTemp['dt'] = pd.to_datetime(globalTemp['dt'])
    plt.title("Average Temperature by Year")
    tempMeans = globalTemp.groupby(pd.Grouper(key='dt', freq='A')).mean().dropna()
    tempMeans['dt'] = tempMeans.index
    scatterPlot(tempMeans, tempMeans['dt'], tempMeans['AverageTemperature'])
def graphIris():
    iris = pd.read_csv(getPath("iris.data"))
    print(iris.columns)
    plt.title="Pair plot of iris"
    sns.pairplot(iris, kind='scatter')
    plt.show()
    plt.title = "Sepal length by petal width"
    scatterPlot(iris, iris['sepalLength'], iris['petalLength'])
    plt.show()
    plt.title = "Boxplot grouped by class"
    boxplot = iris.boxplot(by='class')
    plt.show()
    plt.title = "Sepal length by class"
    sns.barplot(x='class', y='sepalLength', data=iris)
    plt.show()
    iris_mean = iris.groupby(iris['class']).mean()
    plt.title = "Means"
    sns.scatterplot(data=iris_mean)
    plt.show()
    iris_std = iris.groupby(iris['class']).std()
    sns.scatterplot(data=iris_std)
    plt.show()
    iris_var = iris.groupby(iris['class']).var()
    sns.scatterplot(data=iris_var)
    plt.show()
    plt.matshow(iris.cov())
    plt.show()
def main():
    # sns.distplot(tempMeans['AverageTemperature'])   
    # plt.show()
    graphClimateChange()
    """
    is_florida = tempMeans['State']=='Florida'
    fl_temp = tempMeans[is_florida]
    
    sns.set(style="darkgrid")
    sns.lineplot(x="dt", y="AverageTemperature",data=fl_temp)
    plt.xlabel="Month by Year"
    plt.ylabel="Average Temperature"
    plt.show()
    """
if __name__ == '__main__':
    print(main())