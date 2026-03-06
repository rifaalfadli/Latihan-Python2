from abc import ABC, abstractmethod

# Observer Interface
class Observer(ABC):
    @abstractmethod
    def update(self, video_title):
        pass


# Observer
class Subscriber(Observer):
    def __init__(self, name):
        self.name = name

    def update(self, video_title):
        print(f"{self.name} received a notification: New video uploaded - {video_title}!")


# Subject (YouTube channel)
class YouTubeChannel:
    def __init__(self):
        self.subscribers = []

    def subscribe(self, subscriber):
        self.subscribers.append(subscriber)

    def unsubscribe(self, subscriber):
        self.subscribers.remove(subscriber)

    def notify_subscribers(self, video_title):
        for subscriber in self.subscribers:
            subscriber.update(video_title)

    def upload_video(self, video_title):
        print(f"Uploading video: {video_title}")
        self.notify_subscribers(video_title)


# Usage
# channel = YouTubeChannel()

# sub1 = Subscriber("Alice")
# sub2 = Subscriber("Bob")

# channel.subscribe(sub1)
# channel.subscribe(sub2)

# channel.upload_video("Observer Pattern Explained")
# Example usage:
channel = YouTubeChannel()

subscriber1 = Subscriber("John")
subscriber2 = Subscriber("Alice")

channel.subscribe(subscriber1)
channel.subscribe(subscriber2)

video_titles = ["Cats vs. Dogs", "Python Tutorial", "Cooking Pasta"]

for title in video_titles:
    channel.upload_video(title)

channel.unsubscribe(subscriber1)

channel.upload_video("New Video for Subscribers")


class Observer:
    def update(self, message):
        raise NotImplemented

# Inventory
# case 1: barang terjual habis => notify seller dan user
class User(Observer):
    def __init__(self, name):
        self.name = name
    
    def update(self, message):
        print(f"{self.name}, {message}")

class Seller(Observer):
    def __init__(self, store_name):
        self.store_name = store_name

    def update(self, message):
        print(f"{self.store_name}, {message}")

class Inventory:
    def __init__(self, product_name, quantity):
        self.product_name = product_name
        self.quantity = quantity
        self.observers = []
        self.buyer_only_observers = []
    
    def register(self, observer, type):
        self.observers.append(observer)
        if type == 'buyer':
            self.buyer_only_observers.append(observer)

    def unRegister(self, observer):
        self.observers.remove(observer)
        if type == 'buyer':
            self.buyer_only_observers.remove(observer)
    
    def notify_all(self):
        for observer in self.observers:
            observer.update(f"The product {self.product_name} is out of stock.")

    def notify_buyer(self):
        for observer in self.buyer_only_observers:
            observer.update(f"The product {self.product_name} available!")
    
    def sell(self):
        self.quantity -= 1
        if self.quantity == 0:
            self.notify_all()
    
    # def add_stock(self, quantity):
    #     self.quantity += quantity
    def add_stock(self):
        self.quantity += 1
        if self.quantity == 1:
            self.notify_buyer()

iphone = Inventory("IPhone 16", 1)
macbook_pro = Inventory("MacBook Pro M3", 1)

ibox = Seller("ibox")
iphone.register(ibox)
macbook_pro.register(ibox)

rifa = User("Rifa")
iphone.register(rifa)

jane = User("Jane")
macbook_pro.register(ibox)

iphone.sell()
macbook_pro.sell()