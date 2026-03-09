# ==========================================
# DESIGN PATTERN: FACADE (SIMPLE INTERFACE)
# ==========================================

# --- STUDI KASUS 1: COMPUTER STARTUP ---

class CPU:
    def start(self):
        print("⚡ CPU: Memulai pemrosesan instruksi...")

class Memory:
    def load(self):
        print("💾 Memory: Memuat data ke RAM...")

class HardDrive:
    def read(self):
        print("💿 HardDrive: Membaca sektor boot...")

class PowerSupply:
    def turn_on(self):
        print("🔌 PowerSupply: Menyuplai daya listrik...")

# Facade Class
# Menyediakan satu pintu (interface) untuk menjalankan banyak subsistem
class ComputerFacade:
    def __init__(self):
        self.cpu = CPU()
        self.memory = Memory()
        self.hd = HardDrive()
        self.power = PowerSupply()
    
    def start_computer(self):
        print("--- Prosedur Sistem Dimulai ---")
        self.power.run_on() if hasattr(self.power, 'run_on') else self.power.turn_on()
        self.cpu.start()
        self.memory.load()
        self.hd.read()
        print("✅ Sistem Siap: Selamat datang, Rifa!")


# --- STUDI KASUS 2: E-COMMERCE ORDER SERVICE ---

class Product:
    def __init__(self, product_id):
        self.id = product_id

class Inventory:
    def check(self, product):
        print(f"🔍 Inventory: Mengecek stok untuk {product.id}...")
        return True

class Payment:
    def process(self):
        print("💳 Payment: Memverifikasi transaksi pembayaran...")
        return True

class Shipping:
    def ship(self, product):
        print(f"📦 Shipping: Produk {product.id} telah diserahkan ke kurir.")

# Facade Class untuk Pemesanan
class OrderServiceFacade:
    def __init__(self):
        self.inventory = Inventory()
        self.payment = Payment()
        self.shipping = Shipping()

    def place_order(self, product_id):
        """Menyederhanakan proses belanja yang kompleks."""
        print(f"\n--- Memproses Pesanan: {product_id} ---")
        product = Product(product_id)
        
        # Logika alur kerja (Workflow)
        if self.inventory.check(product):
            if self.payment.process():
                self.shipping.ship(product)
                print("🎉 Pesanan Selesai!")
            else:
                print("❌ Kesalahan: Pembayaran ditolak.")
        else:
            print("❌ Kesalahan: Stok tidak tersedia.")

# --- TESTING CLIENT CODE ---

# Contoh 1: Menyalakan Komputer
my_pc = ComputerFacade()
my_pc.start_computer()

# Contoh 2: Melakukan Pemesanan
store_service = OrderServiceFacade()
store_service.place_order("P-BOLT-2026") 