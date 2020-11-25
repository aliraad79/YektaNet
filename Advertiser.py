from BaseAdvertising import BaseAdvertising


class Advertiser(BaseAdvertising):
    instances = []
    def __init__(self, id, name):
        super().__init__()
        self.id = id
        self.name = name
        self.__class__.instances.append(self)

    def getName(self):
        return self.name
    
    def setName(self, name):
        self.name = name

    @staticmethod
    def help():
        return f'Each advertiser has an id and a name.(We can change the name with setName method)\nit also have two fields named views and clicks which have the sum of times a advertiser clicked or viewed.'

    @staticmethod
    def getTotalClicks():
        total_clicks = 0
        for i in Advertiser.instances:
            total_clicks += i.clicks
        return total_clicks

    def getClicks(self):
        return self.clicks

    def getViews(self):
        return self.views

    def incClicks(self):
        self.clicks += 1

    def incViews(self):
        self.views += 1
    
    @staticmethod
    def describeMe():
        return f'This class implement a advertiser with an id and its name.'
