from api import API
from url import URL
from interval import Interval

class BinanceAPI(API):
    interval = Interval()
    def __init__(self):
        self.url = URL().SetBaseUrl("https://api.binance.com/api/v3/klines?")



if __name__ == "__main__":
    print(BinanceAPI().Get("BTCUSDT", BinanceAPI.interval._3m,limit=5))
        
