from tools.get_price_history import *
from tools.Polynomial_Regression import *
from tools.Standard_Deviation import standard_dev, skew, skewtwo

import numpy as np

#ticker=input("Enter ticker symbol in all caps (EX: APPL).")
# array for dependant variable (closing price)
data= get_price_history(symbol='TSLA', period=1, periodType='year', frequencyType='daily', frequency=1)
print(skewtwo(data))
print(skew(data))
closingPrice=[]
for close in data['candles']:
    closingPrice.append(close['close'])

minPrice=100000000
for min in closingPrice:
    if(min<minPrice):
        minPrice=min

maxPrice=0
for max in closingPrice:
    if(max>maxPrice):
        maxPrice=max
frequency, bins = np.histogram(closingPrice, 10, range =[minPrice, maxPrice])

for b, f in zip(bins[1:], frequency):
    print(round(b, 1), ' '.join(np.repeat('*', f)))
#print(PolyReg(data))
#print(standard_dev(data))



#figure out how to do SD and incorporate level of skewness; try to predict trends by seeing if in a normal distribution the price exceeds 1 SD or something of that nature
#find correlation between COIN & SPY; if significant develop trading strat
#calculate probability of certain predicted price and then once statistically significant use it as a price target or buy/sell order
