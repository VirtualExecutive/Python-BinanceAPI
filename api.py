import requests
from url import URL
import numpy as np


class API():

    url:URL

    def Get(self, symbol, interval, startTime=None, endTime=None, limit=None):
        self.url.ResetUrl()
        self.url.AddParameter("symbol", symbol)
        self.url.AddParameter("interval", interval)

        if startTime is not None:
            try:
                startTime = int(startTime)
                if startTime < 0:
                    raise ValueError("startTime must be greater than or equal to 0.")
                self.url.AddParameter("startTime", startTime)
            except ValueError:
                raise ValueError("startTime must be a valid integer.")

        if endTime is not None:
            try:
                endTime = int(endTime)
                if endTime < 0:
                    raise ValueError("endTime must be greater than or equal to 0.")
                self.url.AddParameter("endTime", endTime)
            except ValueError:
                raise ValueError("endTime must be a valid integer.")

        if limit is not None:
            try:
                limit = int(limit)
                if not (1 <= limit <= 1000):
                    raise ValueError("limit must be in the range [1, 1000].")
                self.url.AddParameter("limit", limit)
            except ValueError:
                raise ValueError("limit must be a valid integer.")
            
        return self.Request()

    def Request(self):
        response = requests.get(self.url.url)

        if response.status_code == 200:
            data = response.json()
            return np.array(data)
        else:
            print("Error: Not was got data.")
            print("URL: ",self.url.url)
            return None
        
    def GetUTCTime(self, data):
        return data[0]
    
    def GetOpenPrice(self,data):
        return data[1]
    def GetHighPrice(self,data):
        return data[2]
    def GetLowPrice(self,data):
        return data[3]
    def GetClosePrice(self,data):
        return data[4]
    def GetUTCTimeLast(self,data):
        return data[6]
    

    
