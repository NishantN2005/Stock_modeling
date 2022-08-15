import requests
def get_price_history(**kwargs):
    key='ZTHLZTU4U9FROM66OZ3RUKL7GGLIVJVP'
    url="https://api.tdameritrade.com/v1/marketdata/{}/pricehistory".format(kwargs.get('symbol'))
    params={}
    params.update({'apikey':key})
    for arg in kwargs:
        parameter={arg: kwargs.get(arg)}
        params.update(parameter)
    return requests.get(url, params=params).json()
