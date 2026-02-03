name = input("masukan nama: ")
age = int(input("usia:" ))

if age >= 25:
    print(name,f"sudah dewasa")
elif age >= 10:
    print(name,f"masih remaja")
else:
    print(name,"masih anak anak")

print("=================================================")

header = input("Masukan judul konten: ")
status = input("status draft/scheduled/posted? ")

if status == "draft":
    print(header,f"masih draft")
elif status == "scheduled":
    print(header,f"sedang dijadwalkan")
elif status == "posted":
    print(header,f"sudah di posting")
else:
    print("Status tidak valid")