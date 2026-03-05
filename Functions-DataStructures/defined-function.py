# ==========================================
# DEFINED FUNCTIONS
# ==========================================

# 1. Definisi Fungsi Sederhana
# Menggunakan kata kunci 'def' diikuti nama fungsi dan tanda kurung.
# Sesuai prinsip "Readability counts", gunakan nama yang deskriptif.
def greet_user():
    """Fungsi ini digunakan untuk menyapa pengguna."""
    print("Hello from a function!")

# Memanggil fungsi
greet_user()


# 2. Fungsi dengan Parameter & Return Value
# Ini lebih efisien karena data bisa diolah dan dikembalikan (return).
def calculate_area(length, width):
    """Menghitung luas persegi panjang."""
    area = length * width
    return area

# Menyimpan hasil fungsi ke dalam variabel
result = calculate_area(10, 5)
print(f"Hasil perhitungan luas: {result}")


# 3. Fungsi dengan Default Parameter
# Memberikan nilai cadangan jika argumen tidak diisi.
def say_hello(name="Guest"):
    print(f"Welcome, {name}!")

say_hello("Rifa") # Output: Welcome, Rifa!
say_hello()        # Output: Welcome, Guest!