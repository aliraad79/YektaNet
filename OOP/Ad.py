from BaseAdvertising import BaseAdvertising

class Ad(BaseAdvertising):
    def __init__(self, id, title,img_url, link, advertiser):
        super().__init__(id)
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

    def getLink(self):
        return self.link

    def setLink(self, link):
        self.link = link

    def setAdvertiser(self, advertiser):
        self.advertiser = advertiser

    def incClicks(self):
        super().incClicks()
        self.advertiser.incClicks()

    def incViews(self):
        super().incViews()
        self.advertiser.incViews()
    
    def describeMe(self):
        return f'This class make an ad and store it with a title and a id.'
    

