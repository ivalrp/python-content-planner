secret_number = 3

try:
    number = int (input("Masukan angka 1-5: "))
    if 1 <= number <= 5:
        if secret_number == number:
            print("adalah benar")
        else:
              print("salah")
    else:
        print("masukan angka 1-5")
except ValueError:
    print("input harus angka")