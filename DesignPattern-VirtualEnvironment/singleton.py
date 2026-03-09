# ==========================================
# DESIGN PATTERN: SINGLETON
# ==========================================

# --- STUDI KASUS 1: DatabaseConnection Dummy ---

class DatabaseConnection:
    """Singleton sederhana untuk koneksi database."""
    _instance = None

    def __init__(self):
        # Inisialisasi private connection (dummy)
        self.connection = None

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls()
            cls._instance._initialize_connection()
        return cls._instance
    
    def _initialize_connection(self):
        """Simulasi inisialisasi koneksi database."""
        self.connection = "Dummy Database Connection"
        print("✅ DatabaseConnection: Initialized")

# --- TESTING SINGLETON ---
print("\n--- Testing DatabaseConnection Singleton ---")
db1 = DatabaseConnection.get_instance()
db2 = DatabaseConnection.get_instance()

print(f"db1 is db2? {db1 is db2}")  # True
print(f"Connection object: {db1.connection}")


# --- STUDI KASUS 2: Database dengan Print Messages ---

class Database:
    """Singleton dengan log output untuk tracing."""
    _instance = None

    def __init__(self):
        print("🏗️ Database instance created")
        self.connection = None

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls()
            cls._instance._init_connection()
        return cls._instance
    
    def _init_connection(self):
        """Inisialisasi koneksi database nyata / dummy."""
        self.connection = "Database connection initialized"
        print("✅ Database connection initialized")

# --- TESTING SINGLETON ---
print("\n--- Testing Database Singleton ---")
db1 = Database.get_instance()
db2 = Database.get_instance()

print(f"db1 is db2? {db1 is db2}")  # True
print(f"db1.connection: {db1.connection}")
print(f"db2.connection: {db2.connection}")
print(db1)
print(db2)