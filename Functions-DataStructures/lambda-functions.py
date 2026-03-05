# ==========================================
# LAMBDA FUNCTIONS (ANONYMOUS FUNCTIONS)
# ==========================================

# 1. Perbandingan: Fungsi Biasa vs Lambda
# Fungsi Biasa (Explicit)
def add_regular(a, b):
    return a + b

# Lambda Function (Concise)
# Format: lambda arguments : expression
add_lambda = lambda a, b : a + b

print(f"Hasil Fungsi Biasa: {add_regular(2, 2)}")
print(f"Hasil Lambda: {add_lambda(2, 2)}")


# 2. Lambda dengan Berbagai Jumlah Argumen
# Satu Argumen
plus_ten = lambda a : a + 10
print(f"\nPlus Ten (5): {plus_ten(5)}")

# Dua Argumen (Perkalian)
multiply = lambda a, b : a * b
print(f"Multiply (5 * 6): {multiply(5, 6)}")

# Tiga Argumen (Penjumlahan)
sum_three = lambda a, b, c : a + b + c
print(f"Sum Three (5 + 6 + 2): {sum_three(5, 6, 2)}")


# 3. Lambda untuk Action (Greeting)
# Sesuai identitas kamu sebagai Rifa
greet = lambda name : print(f"\nHello, {name}!")
greet("Rifa")


# 4. Lambda dengan Arbitrary Arguments (*args)
# Menangkap banyak argumen sekaligus dalam bentuk Tuple
greet_team = lambda *names : print(f"Team members: {names}")
greet_team("Hadis", "Rifa", "Reval")


# 5. Contoh Kasus Riil: Sorting dengan Lambda
# Sangat berguna untuk mengurutkan data list of dictionaries
students = [
    {"name": "Rifa", "score": 90},
    {"name": "Reval", "score": 85},
    {"name": "Hadis", "score": 95}
]

# Mengurutkan berdasarkan skor terkecil ke terbesar
students.sort(key=lambda x: x["score"])
print(f"\nSorted Students by Score: {students}")