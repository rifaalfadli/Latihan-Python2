# ==========================================
# MATERI: DICTIONARIES (KEY-VALUE PAIRS)
# ==========================================

# 1. Inisialisasi Dictionary
# Berdasarkan identitas kamu, Rifa, sebagai software developer.
student = {
    "name": "Rifa",
    "age": 20,
    "major": "Teknik Informatika",
    "is_graduated": True, # Sesuai ketertarikan belajar Python saat ini
}

print("--- Akses & Keamanan Data ---")
# Akses Langsung (Bisa error jika key tidak ada)
print(f"Nama: {student['name']}") 

# Akses Aman menggunakan .get() 
# Jika key tidak ada, akan mengembalikan nilai default (Unknown/Bogor)
print(f"Umur: {student.get('age')}")
print(f"Major: {student['major']}") 
print(f"Domisili: {student.get('lives_in', 'Bogor')}") 


# 2. Manipulasi Data (CRUD)
print("\n--- Modifikasi & Update Data ---")
student["age"] = 21            # Mengubah nilai yang sudah ada
student["gender"] = "Male"     # Menambah key-value baru
student["Lives_in"] = "Bogor"  # Menambah domisili sesuai aktivitas kamu

# Menghapus data dengan .pop()
# Mengembalikan nilai yang dihapus
removed_major = student.pop("major")
print(f"Major '{removed_major}' telah dihapus.")


# 3. Iterasi Dictionary (Looping)
# Sesuai prinsip "Readability counts", gunakan format yang jelas
print("\n--- Iterasi Data Dictionary ---")

print("\n> Hanya Keys:")
for key in student:
    print(f"- {key}")

print("\n> Hanya Values:")
for value in student.values():
    print(f"- {value}")

print("\n> Pasangan Key & Value:")
for key, value in student.items():
    print(f"{key:10} = {value}")