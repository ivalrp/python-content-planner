# String di py immutable/ tidak bisa diubah secara langsung
text = "ini text"
kodok = "kodok"
text = kodok
print(text)

# sama seperti java
# yang terjadi sebenarnya bukan mengganti isi tapi membuat variable baru
# ibarat buku, saat text = kodok, text ini adalah halaman kedua, halaman 1nya tetap "ini text"

# join, split, strip, upper, lower, replace, slice
name = " ival racha 01 "
print(name.upper())
print(name.lower())
print(name.capitalize()) # mengubah huruf awal jadi kapital

print(name.strip()) #menghapus spasi diawal atau akhir huruf
print(name.replace("01", "pratama")) # mengganti string

strip_name = name.strip()
split_result = strip_name.split(" ") # split string 
print(split_result)

join_text = " ".join(split_result) # kebalikan split
print(join_text)

# string slice
text = "python"
print(text[0]) # p
print(text[0:3]) # pyt
print(text[-1]) # n

# ini namanya format string
age = 27
print(f"nama: {name}, umur: {age}")

# hal umum terjadi 
input_data = "  IVVAL@GMAIL.COM  "
email = input_data.strip().lower() # jadiin kecil dan menghyilangkan spasi di awal atau dan atau akhir kalimat
print(email)

input_email = email #input("Masukan Alamat Email: ").strip().lower()
if "@" in input_email:
    username, domain = input_email.split("@", 1) # angka 1 batas split
    print(f"Username: {username} | Domain: {domain}")
