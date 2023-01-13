import requests
class BazaarItem():
    def __init__(self, item) -> None:
        self.item = item
        self.data = requests.get('https://api.hypixel.net/skyblock/bazaar').json()
    def refresh(self) -> None:
        self.data = requests.get('https://api.hypixel.net/skyblock/bazaar').json() 
    def grab_price(self):
        return ((self.data['products'])[self.item])['quick_status']['buyPrice']

class Bazaar():
    def __init__(self) -> None:
        pass
    
    def get(self, item) -> BazaarItem:
        return BazaarItem(item)

