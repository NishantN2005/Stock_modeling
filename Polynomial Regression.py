import numpy as np
import matplotlib.pyplot as plt
import requests
import pandas as pd
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
#API data reception

key=#Enter TD Ameritrade API key here
def get_price_history(**kwargs):
    url="https://api.tdameritrade.com/v1/marketdata/{}/pricehistory".format(kwargs.get('symbol'))
    params={}
    params.update({'apikey':key})
    for arg in kwargs:
        parameter={arg: kwargs.get(arg)}
        params.update(parameter)
    return requests.get(url, params=params).json()
ticker=input("Enter ticker symbol in all caps (EX: APPL).")
# array for dependant variable (closing price)
data= get_price_history(symbol=ticker, period=1, periodType='year', frequencyType='daily', frequency=1)

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

fig=plt.figure()
ax=fig.add_axes([0,0,1,1])
ax.set_xlim(1,300)
ax.scatter(x,y,color='r')

#Regression
poly=PolynomialFeatures(degree=4)
x_poly=poly.fit_transform(x)

pilreg=LinearRegression()
pilreg.fit(x_poly,y)
LinearRegression(copy_X=True, fit_intercept=True, n_jobs=None, normalize=False)
plt.plot(x, pilreg.predict(poly.fit_transform(x)))

new=np.empty(300-len(data['candles']))
new2=new[:,np.newaxis]
g=len(data['candles'])
n=0
while(n<300-len(data['candles'])):
    new2[n,0]=g
    g=g+1
    n=n+1
plt.plot(new2,pilreg.predict(poly.fit_transform(new2)))

plt.show()
