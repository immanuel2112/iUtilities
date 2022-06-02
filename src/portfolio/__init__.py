# API Key
# bXCrQFuR1MifUGnTQOmMfjT0cuHtW8yZcCMkmv91KdDaMrvLTntujZYz6g6hxBpN
# Secret Key
# bbYsHivTqQZ2R6D3ie52L4vHJYpKmpwkS1MWcNmDgYCYEwYKLMZuYBl5HnfnNI5H
from binance.spot import Spot

client = Spot(key='bXCrQFuR1MifUGnTQOmMfjT0cuHtW8yZcCMkmv91KdDaMrvLTntujZYz6g6hxBpN', secret='bbYsHivTqQZ2R6D3ie52L4vHJYpKmpwkS1MWcNmDgYCYEwYKLMZuYBl5HnfnNI5H')
account = client.account()
# Get account information
print(account)
#print(client.account_snapshot('SPOT'))
print(client.coin_info())
for item in account['balances']:
    if float(item['free']) > 0:
        print(item['asset'] +':'+item['free'])

# # Post a new order
# params = {
#     'symbol': 'BTCUSDT',
#     'side': 'SELL',
#     'type': 'LIMIT',
#     'timeInForce': 'GTC',
#     'quantity': 0.002,
#     'price': 9500
# }
#
# response = client.new_order(**params)
# print(response)