# 1️⃣ list awal
numbers = [1, 3, 4, 5, 6, 4, 2, 4, 5]

# 2️⃣ hilangkan duplikat pakai set
unique_set = set(numbers)

# 3️⃣ simpan ke list baru
unique_list = list(unique_set)

# 4️⃣ loop pakai enumerate
for i, number in enumerate(unique_list, start=1):
    print(i, number)
