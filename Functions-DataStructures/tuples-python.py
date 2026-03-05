# ==========================================
# TUPLES (IMMUTABLE SEQUENCES)
# ==========================================

# 1. Inisialisasi Tuple
# Sifat utama: Immutable (Tidak bisa ditambah, dihapus, atau diubah)
my_tuple = (1, 2, 3)

# PENTING: Jika hanya satu elemen, wajib menggunakan koma (,)
# Tanpa koma, Python akan menganggapnya sebagai integer dalam kurung.
single_element_tuple = (4,) 
print(f"Tipe data single_element: {type(single_element_tuple)}")


# 2. Akses Data (Sama seperti List)
my_fruits = ("pisang", "kelapa", "durian", "manggis")

print("\n--- Akses Elemen Tuple ---")
print(f"Buah pertama: {my_fruits[0]}")
print(f"Buah ketiga : {my_fruits[2]}")


# 3. Sifat Immutability (Keamanan Data)
# Keuntungan: Lebih cepat secara performa dan aman dari perubahan tidak sengaja.
print("\n--- Percobaan Modifikasi ---")
try:
    my_fruits[2] = "jeruk" 
except TypeError as e:
    print(f"⚠️ Error Terdeteksi: {e}")
    print("Ingat: Tuple tidak bisa di-append, di-remove, atau diubah isinya.")


# 4. Fungsi Mengembalikan Multiple Values
# Secara default, jika fungsi mengembalikan lebih dari satu nilai, 
# Python akan membungkusnya ke dalam Tuple.
def get_data():
    """Simulasi mengambil data dari database atau sensor."""
    return "hello", "world", "python"

result = get_data()
print(f"\nHasil dari fungsi: {result} (Tipe: {type(result)})")

# Unpacking Tuple (Memecah isi tuple ke variabel terpisah)
msg1, msg2, msg3 = get_data()
print(f"Pesan terpisah: {msg1}, {msg2}, {msg3}")