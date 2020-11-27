import abc

class BaseAdvertising(abc.ABC):
    def __init__(self,id):
        self.id = id
        self.clicks = 0
        self.views = 0

    def getClicks(self):
        return self.clicks

    def getViews(self):
        return self.views

    def incClicks(self):
        self.clicks += 1

    def incViews(self):
        self.views += 1
    
    @abc.abstractmethod
    def describeMe(self):
        pass

