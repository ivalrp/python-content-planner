#tidak seperti java harus pakai nama variable dan tanda ; (semicolon)

# String
name = "ival"

#Integer/int
age = 27

#float
#pembedanya koma
ipk = 3.47

# boolean
is_work = False

#print

# print("nama: ", name) | bisa seperti ini
print(f"nama: {name}, umur: {age}") 
print(f"IPK: {ipk}, apakah sedanng bekerja: {is_work}")


print("==================input======================")

name_2 = input("Nama: ")
print("Halo ", name_2)

# calculator sederhana banget 
angka1 = int(input("masukan angka 1: "))
angka2 = int(input("masukan angka 2: "))

print("hasilnya: ", angka1+angka2)