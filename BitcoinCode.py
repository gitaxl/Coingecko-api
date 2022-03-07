from pycoingecko import CoinGeckoAPI
import datetime

cg = CoinGeckoAPI()
dt = datetime.datetime.fromtimestamp(0)

class bitcoin_price():

    def __init__(self):
        pass

    def getRange(self, rangeStart, rangeEnd):
        self.rangeStart = rangeStart
        self.rangeEnd = rangeEnd
        priceRange = cg.get_coin_market_chart_range_by_id(id='bitcoin', vs_currency='eur', from_timestamp=rangeStart, to_timestamp=rangeEnd)
        return priceRange
    
  

    #def unixToDate(self, )

    #def getPriceRange(self):



d = bitcoin_price()
a = d.getRange(1642774737,1642861137)

def bearOrBull():
    for i in range(len(a['prices'])):
        print(a['prices'][i][1])
        i += 1
    
    if a['prices'][i][1] < a['prices'][i-1][1]:
        print('BEAR')
    else:
        print('BULL')
bearOrBull()

#Get the first price of the range and last UNIX DATE AND PRICE
#print(a['prices'][0][1], a['prices'][-1])


#d.getPriceRange(1642774737,1642861137)
#print(d.getRange(1642774737,1642861137))

''''
OLD SHIT THAT WORKS
a = cg.get_coin_market_chart_range_by_id(id='bitcoin', vs_currency='eur', from_timestamp=1642774737, to_timestamp=1642861137)
range1 = a['prices']
length = len(range1)
i = 0

for i in range(length):
    print(range1[i])
    i += 10
   

#startDate = input("Input start date in form 'DD-MM-YYYY': ")
#endDate = input("Input end date in form 'DD-MM-YYYY': ")
#print(cg.get_coin_market_chart_range_by_id(id='bitcoin', vs_currency='eur', from_timestamp='01-01-2021', to_timestamp='02-01-2022'))

#a = cg.get_coin_history_by_id(id='bitcoin', date = startDate)
#b = cg.get_coin_history_by_id(id='bitcoin', date = endDate)

#def bearOrBull():
 #   print(a['market_data']['current_price']['eur'] - b['market_data']['current_price']['eur'] )
  #  if a['market_data']['current_price']['eur'] - b['market_data']['current_price']['eur'] < 0:
   #     print('BEAR')
    #else:
     #   print('BULL!')
        
#bearOrBull()
'''

