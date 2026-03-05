# ==========================================
# SETS (UNIQUE & UNORDERED)
# ==========================================

# 1. Inisialisasi Set
# Set otomatis menghapus duplikat saat dibuat
my_set = {1, 2, 3, 3, 3} 
print(f"Set awal (duplikat otomatis hilang): {my_set}")

# Menggunakan set() constructor untuk membersihkan list
second_numbers = [1, 2, 3, 4, 5, 5, 5, 6, 7, 7, 8]
unique_numbers = set(second_numbers)
print(f"List asli: {second_numbers}")
print(f"Setelah dikonversi ke Set: {unique_numbers}")


# 2. Manipulasi Set (CRUD)
numbers = {20, 21, 22, 23, 24, 25}

# Menambah elemen baru
numbers.add(6)
# Menambah elemen yang sudah ada (tidak akan berpengaruh)
numbers.add(20) 

# Menghapus elemen
if 23 in numbers:
    numbers.remove(23)

print(f"\nNumbers set setelah manipulasi: {numbers}")


# 3. Operasi Himpunan (Set Operations)
# Sangat berguna untuk membandingkan dua kelompok data
set1 = {1, 2, 3}
set2 = {3, 4, 5}

print("\n--- Operasi Matematika Set ---")

# Union: Menggabungkan semua (tanpa duplikat)
union_result = set1.union(set2) 
print(f"Union (Gubung)        : {union_result}")

# Intersection: Mengambil yang ada di keduanya
intersection_result = set1.intersection(set2) 
print(f"Intersection (Irisan) : {intersection_result}")

# Difference: Mengambil selisih/perbedaan
diff_1_2 = set1.difference(set2) # Ada di 1 tapi tidak ada di 2
diff_2_1 = set2.difference(set1) # Ada di 2 tapi tidak ada di 1
print(f"Difference (1 - 2)    : {diff_1_2}")
print(f"Difference (2 - 1)    : {diff_2_1}")