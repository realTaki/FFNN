class LPool:
    def __init__(self, rD, rF):
        self.rD = rD
        self.rF = rF
        self.sD = rD
        self.sF = rF
        self.limitrF = rF
    
    def getNetPrice(self):
        return self.sD/self.sF