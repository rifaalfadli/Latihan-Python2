# ==========================================
# DESIGN PATTERN: OBSERVER (PUBLISH-SUBSCRIBE)
# ==========================================
from abc import ABC, abstractmethod

# 1. Interface / Blueprint untuk Pengamat
class Observer(ABC):
    @abstractmethod
    def update(self, message):
        """Metode yang akan dipanggil saat Subject berubah."""
        pass

# --- STUDI KASUS 1: YOUTUBE NOTIFICATION ---

class Subscriber(Observer):
    def __init__(self, name):
        self.name = name

    def update(self, video_title):
        print(f"🔔 Notifikasi untuk {self.name}: Video baru diunggah - '{video_title}'!")

class YouTubeChannel:
    def __init__(self, channel_name):
        self.channel_name = channel_name
        self._subscribers = []

    def subscribe(self, observer):
        if observer not in self._subscribers:
            self._subscribers.append(observer)

    def unsubscribe(self, observer):
        self._subscribers.remove(observer)

    def upload_video(self, title):
        print(f"\n🎬 {self.channel_name} mengunggah: {title}")
        for sub in self._subscribers:
            sub.update(title)


# --- STUDI KASUS 2: SMART INVENTORY SYSTEM ---

class User(Observer):
    def __init__(self, name):
        self.name = name
    
    def update(self, message):
        print(f"📱 [User {self.name}] Info: {message}")

class Seller(Observer):
    def __init__(self, store_name):
        self.store_name = store_name

    def update(self, message):
        print(f"🏪 [Seller {self.store_name}] Log: {message}")

class Inventory:
    def __init__(self, product_name, quantity):
        self.product_name = product_name
        self.quantity = quantity
        self._observers = [] # List berisi (observer, role)

    def register(self, observer, role='buyer'):
        self._observers.append({'obs': observer, 'role': role})

    def notify(self, message, target_role=None):
        """Mengirim notifikasi berdasarkan role tertentu atau semua."""
        for entry in self._observers:
            if target_role is None or entry['role'] == target_role:
                entry['obs'].update(message)

    def sell(self):
        if self.quantity > 0:
            self.quantity -= 1
            print(f"\n📦 Transaksi: 1 unit {self.product_name} terjual.")
            if self.quantity == 0:
                self.notify(f"Stok {self.product_name} HABIS! Segera restock.", target_role='seller')
        else:
            print(f"❌ Gagal: Stok {self.product_name} sudah kosong.")

    def add_stock(self):
        self.quantity += 1
        print(f"\n📥 Restock: 1 unit {self.product_name} ditambahkan.")
        if self.quantity == 1:
            self.notify(f"Kabar gembira! {self.product_name} kini tersedia kembali.", target_role='buyer')


# --- TESTING IMPLEMENTATION ---

# Inisialisasi Produk & Aktor
iphone = Inventory("iPhone 16", 1)
iBox = Seller("iBox Central")
rifa = User("Rifa")

# Registrasi
iphone.register(iBox, role='seller')
iphone.register(rifa, role='buyer')

# Simulasi Kejadian
iphone.sell()       # Stok jadi 0, seller dapat notif
iphone.add_stock()  # Stok jadi 1, buyer dapat notif