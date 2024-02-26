

class URL():
    baseUrl:str
    url:str
    isQSS=False
    
    def __init__(self) -> None:
        pass

    def SetBaseUrl(self, url, isChangeUrl=True):
        self.baseUrl = url
        if isChangeUrl : self.SetUrl(url)
        return self
    
    def SetUrl(self, url):
        self.url = url
        return self

    def ResetUrl(self):
        self.url = self.baseUrl
        return self

    def IsQSS(self):
        if "?" in self.url: return True
        return False
    
    def DoQSS(self):
        self.url+="?"
    
    def AddParameter(self, key,value):
        if not self.isQSS:
            if not self.IsQSS():
                self.DoQSS()
        self.url+=f"&{key}={value}"
        return self
    

        