import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
#API data reception
def PolyReg(data):
    y1=np.empty(len(data['candles']))
    y=y1[:,np.newaxis]
    #adding data to be graphed
    for x in range(len(data['candles'])):
        y[x,0]=data['candles'][x]['close']
        #np.append(y,data['candles'][x]['close'],axis=None)
        #print(y)
        x1=np.empty(len(data['candles']))
        x=x1[:,np.newaxis]
        #x=x.reshape(-1,1)
        i=1
        while(i<=len(data['candles'])):
            x[i-1,0]=i
            i=i+1



    #Regression
    poly=PolynomialFeatures(degree=4)
    x_poly=poly.fit_transform(x)

    pilreg=LinearRegression()
    pilreg.fit(x_poly,y)
    LinearRegression(copy_X=True, fit_intercept=True, n_jobs=None, normalize=False)
    valueHolder={}
    valueHolder['cRegPrice']= pilreg.predict(poly.fit_transform(x))
    #x, pilreg.predict(poly.fit_transform(x))

    new=np.empty(300-len(data['candles']))
    new2=new[:,np.newaxis]
    g=len(data['candles'])
    n=0
    while(n<300-len(data['candles'])):
        new2[n,0]=g
        g=g+1
        n=n+1
    valueHolder['pRegPrice'] = pilreg.predict(poly.fit_transform(new2))
    return valueHolder
