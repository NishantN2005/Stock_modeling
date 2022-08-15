import numpy as np
import matplotlib.pyplot as plt
import requests
import pandas as pd
import math

def standard_dev(data):
    #Use pandas to process mean, deviation, etc. it will make it easier to organize marketdata
    df=pd.DataFrame(columns=['Price','Mean','Deviation','DeviationSquared', 'MDS'])

    #create price column
    closingPrice=[]
    for candle in data['candles']:
        closingPrice.append(candle['close'])
    df['Price']=closingPrice

    #get/create mean column
    mean=0
    for price in closingPrice:
        mean+=price
    mean/=len(closingPrice)
    df['Mean']=mean

    #fill deviation column (deviation from mean pretty much)
    df['Deviation']=df['Price']-df['Mean']
    #deviaton Deviation
    df['DeviationSquared'] = df['Deviation']**2

    #mean DeviationSquared
    df['MDS'] = df.mean(axis=0)['DeviationSquared']

    sd=math.sqrt(df['MDS'][0])

    return sd

'''
Originally created skew & skewtwo to test. After testing
'''

def skew(data):
    df=pd.DataFrame(columns = ['Price','Mean','SD', 'StandardizedVal', 'S3'])
    closingPrice=[]
    for candle in data['candles']:
        closingPrice.append(candle['close'])
    df['Price']=closingPrice

    mean=0
    for price in closingPrice:
        mean+=price
    mean/=len(closingPrice)
    df['Mean']=mean

    df['SD'] = standard_dev(data)
    df['StandardizedVal'] = (df['Price']-df['Mean'])/df['SD']
    df['S3']= df['StandardizedVal']**3
    skew = (df.sum(axis=0)['S3'])

    coefficient = 1/len(closingPrice)

    return skew*coefficient






def skewtwo(data):
    df=pd.DataFrame(columns = ['Price','Median','SD','Mean'])
    closingPrice=[]
    for candle in data['candles']:
        closingPrice.append(candle['close'])
    df['Price']=closingPrice
    mean=0
    for price in closingPrice:
        mean+=price
    mean/=len(closingPrice)
    df['Mean']=mean
    df['SD']=standard_dev(data)
    if(len(closingPrice)%2==1):
        pop=0
        while(len(closingPrice)>1):
            closingPrice.pop(pop)
            closingPrice.pop(len(closingPrice)-1)
        df['Median']=closingPrice[0]
    else:
        pop=0
        while(len(closingPrice)!=2):
            closingPrice.pop(pop)
            closingPrice.pop(len(closingPrice)-1)
        df['Median']=(closingPrice[0]+closingPrice[1])/2
    skew=((df['Mean'][0]-df['Median'][0])*3)/df['SD'][0]
    print("mean:"+str(df['Mean'][0]))
    print("median"+str(df['Median'][0]))
    return skew
