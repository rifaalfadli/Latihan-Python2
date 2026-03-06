# Subsystem classes
class CPU:
    def start(self):
        print("CPU is starting")

class Memory:
    def load(self):
        print("Memory is loading data")

class Ssh:
    def read(self):
        print("HardDrive is reading data")

class PowerSupply:
    def turn_on(self):
        print("PowerSupply is turning on")

# Facade class
class Computer:
    def __init__(self):
        self.cpu = CPU()
        self.memory = Memory()
        self.hard_drive = Ssh()
        self.power_supply = PowerSupply()
    
    def start_computer(self):
        print("Starting the computer....")
        self.cpu.start()
        self.memory.load()
        self.hard_drive.read()
        self.power_supply.turn_on()
        print("Computer is ready to use")

# Client code
computer_facade = Computer()
computer_facade.start_computer()


class Product:
    def __init__(self, id):
        self.id = id

class Inventory:
    def check_inventory(self, product):
        print(f"Checked inventory for product {product.id}")
        return True

class Payment:
    def make_payment(self):
        print("Made payment")
        return True

class Shipping:
    def ship_product(self, product):
        print(f"Shipped product {product.id}")


class OrderService:
    def __init__(self):
        self.inventory = Inventory()
        self.payment = Payment()
        self.shipping = Shipping()

    def place_order(self, product_id):
        product = Product(product_id)
        if self.inventory.check_inventory(product):
            print("Inventory is available")
            if self.payment.make_payment():
                print("Payment success")
                self.shipping.ship_product(product)
            else:
                print("Payment failed")
        else:
            print("Product out of stock")


order_service = OrderService()
order_service.place_order("P123456")