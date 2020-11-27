from BaseAdvertising import BaseAdvertising

class Ad(BaseAdvertising):
    def __init__(self, id, title,img_url, link, advertiser):
        super().__init__()
        self.id = id
        self.title = title
        self.img_url = img_url
        self.link = link
        self.advertiser = advertiser

    def getTitle(self):
        return self.title
    
    def setTitle(self, title):
        self.title = title
    
    def getImgUrl(self):
        return self.img_url
    
    def setImgUrl(self, img_url):
        self.img_url = img_url

    def getLInk(self):
        return self.link

    def setLink(self, link):
        self.link = link

    def setAdvertiser(self, advertiser):
        self.advertiser = advertiser

    def getClicks(self):
        return self.clicks

    def getViews(self):
        return self.views

    def incClicks(self):
        self.clicks += 1
        self.advertiser.incClicks()

    def incViews(self):
        self.views += 1
        self.advertiser.incViews()
    
    @staticmethod
    def describeMe():
        return f'This class make an ad and store it with a title and a id.'
    

