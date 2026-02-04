import os
import json

FILE_NAME = "contents.json"
def load_contents():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file :
            return json.load(file)
    return []

def save_contents(data):
    with open(FILE_NAME,"w") as file:
        json.dump(data, file, indent=4)

contents = load_contents()

def add_content(content_name, status):
    content = {
        "header" : content_name,
        "status" : status
    }
    print("Data Berhasil Ditambahkan")
    contents.append(content)
    save_contents(contents)

def view_contents():
    for i,content in enumerate(contents, start= 1):
        print(f"{i}. {content["header"]} [{content["status"]}] ")


def convert_status(status):
    if status == "1":
        return "draft"
    elif status == "2":
        return "scheduled"
    else :
        return "published"

def update_status(index, status):
        if len(contents) != 0:
            contents[int(index)-1]["status"] = status   
            save_contents(contents)
            print("data berhasil diubah")
        else:
            print("tidak ada data")
            


while True:
    print("====================================")
    print("1. Tambah konten")
    print("2. Lihat konten")
    print("3. Ubah status")
    print("4. Keluar")

    choice = input("Pilih menu: ")
    if choice == "1":
        header = input("Masukan Header Content: ")
        while True:
            status = input("masukan status 1/2/3: ")
            if status.isdigit():
                if 1 <= int(status) <= 3:
                    result_status = convert_status(status)
                    add_content(header, result_status)
                else:
                    print("angka 1-3")                 
            else:
                print("Angka Tidak Valid")
    elif choice == "2":
        view_contents()
    elif choice == "3":
        header = input("Masukan Nomor Yang Mau Diubah: ")
        done = False
        while done != True :
            status = input("masukan status 1/2/3: ")
            if status.isdigit():
                if 1 <= int(status) <= 3:
                    result_status = convert_status(status)
                    update_status(header, result_status)
                    done = True
                else:
                    print("angka 1-3")                 
            else:
                print("Angka Tidak Valid")
    elif choice == "4":
        print("See Youu ~")
        break
    else:
        print("Masukan Angka Yang Valid")

