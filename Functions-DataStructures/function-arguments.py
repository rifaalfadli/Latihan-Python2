# ==========================================
# FUNCTION ARGUMENTS & PARAMETERS
# ==========================================

# 1. Positional & Keyword Arguments
# Memberikan fleksibilitas saat memanggil fungsi
def describe_pet(animal_type, name):
    print(f"I have a {animal_type}.")
    print(f"My {animal_type}'s name is {name}.")

# Memanggil berdasarkan posisi (Positional)
describe_pet("cat", "Miko") 
# Memanggil berdasarkan nama parameter (Keyword)
describe_pet(animal_type="fish", name="Fiyu")


# 2. Default Parameter Value
# Memberikan nilai cadangan jika argumen tidak diisi
def show_address(country="Indonesia"):
    print(f"I am from {country}")

show_address("Malaysia")
show_address()  # Menggunakan default "Indonesia"


# 3. Arbitrary Arguments (*args)
# Mengumpulkan argumen tanpa nama ke dalam bentuk Tuple
def show_youngest_child(*kids):
    # 'kids' adalah Tuple, akses menggunakan indeks
    print(f"The youngest child is {kids[2]}")

show_youngest_child("Spongebob", "Patrick", "Garry")

def greet_many(*names):
    for name in names:
        print(f"Selamat belajar Python, {name}!")

greet_many("Haru", "Miti")


# 4. Arbitrary Keyword Arguments (**kwargs)
# Mengumpulkan argumen bernama ke dalam bentuk Dictionary
def build_user_profile(**kwargs):
    # 'kwargs' adalah Dictionary, akses menggunakan loop .items()
    for key, value in kwargs.items():
        print(f"{key.capitalize()}: {value}")

build_user_profile(name="Rifa", role="Developer", location="Bogor")


# 5. Keyword-Only Arguments
# Memaksa pengguna fungsi untuk menyebutkan nama parameter secara eksplisit
def greet_strict(*, name, greeting):
    print(f"{greeting.capitalize()}, {name}!")

# greet_strict("Rifa", "Selamat siang") # Ini akan ERROR
greet_strict(name="Rifa", greeting="selamat siang")


# 6. Pass Statement (Placeholder)
# Digunakan jika fungsi belum mau diimplementasikan agar tidak error
def add_order():
    pass # Kerjakan nanti