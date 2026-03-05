# ==========================================
# LIST MANIPULATION & SLICING
# ==========================================

# 1. Inisialisasi & Akses Dasar
my_fruits = ["apple", "banana", "manggo", "durian"]

print("--- Akses & Modifikasi ---")
first_fruit = my_fruits[0]
print(f"Buah pertama: {first_fruit}")

# Mengubah elemen (Mutable)
my_fruits[1] = "orange"
print(f"Setelah diubah: {my_fruits}")


# 2. Menambah & Menghapus Elemen
print("\n--- Operasi List (CRUD) ---")
my_fruits.append("melon")        # Tambah di akhir
my_fruits.insert(0, "salak")      # Tambah di indeks spesifik
print(f"Setelah ditambah: {my_fruits}")

# Menghapus dengan aman (Handling Exception)
try:
    my_fruits.remove("coconut")
except ValueError:
    print("⚠️ Warning: 'coconut' tidak ditemukan dalam list.")

# Cek keberadaan sebelum menghapus (Standard Practice)
if "durian" in my_fruits:
    my_fruits.remove("durian")
    print("✅ Berhasil menghapus durian dari list.")

print(f"Total buah sekarang ({len(my_fruits)}): {my_fruits}")


# 3. List Slicing (Memotong List)
# Format: list[start:stop:step]
print("\n--- Teknik List Slicing ---")
my_foods = ["martabak", "risol mayo", "mie ayam pangsit", "pizza", "telur"]

print(f"Indeks 1 sampai 2     : {my_foods[1:3]}")  # risol mayo, mie ayam
print(f"4 elemen pertama      : {my_foods[:4]}")   # indeks 0 sampai 3
print(f"Dari indeks 2 ke akhir: {my_foods[2:]}")
print(f"Copy seluruh list     : {my_foods[:]}")


# 4. Advanced Slicing (Step & Reverse)
angka = [1, 2, 3, 4, 5, 6, 7, 8]
print("\n--- Advanced Slicing ---")
print(f"Angka Loncat 2 (Step) : {angka[0:8:2]}") # [1, 3, 5, 7]
print(f"Membalikkan List      : {angka[::-1]}")  # [8, 7, 6, 5, 4, 3, 2, 1]


# 5. Menggabungkan List
# extend() menggabungkan isi list lain ke list asal
my_foods.extend(["sate maranggi", "ayam bakar"])
print(f"\nSetelah extend: {my_foods}")