import os
import json

class Contents:
    def __init__(self, title, status):
        self.title = title
        self.status = status
    
    def to_dict(self):
        return{
            "title" : self.title,
            "status" : self.status
        }
    

contents = []

def save_to_file():
    data = [c.to_dict() for c in contents]
    with open("contents_2.json", "w") as file:
        json.dump(data,file, indent = 4)

def load_from_file():
    contents.clear()
    if os.path.exists("contents_2.json"):
        with open("contents_2.json","r") as file:
            data = json.load(file)

            for item in data:
                contents.append(
                    Contents(item["title"], item["status"])
                )
def add_content(title, status):
    content = Contents(title,status)
    contents.append(content)
    save_to_file()

def view_contents():
    if not contents:
        print("Belum ada konten")
        return
    
    for i,content in enumerate(contents, start= 1):
        print(f"{i}. {content.title} [{content.status}] ")


def convert_status(status):
    if status == "1":
        return "draft"
    elif status == "2":
        return "scheduled"
    else :
        return "published"

def update_status_by_index(index, status):
    if len(contents) != 0:
        contents[int(index)-1].status = status
        save_to_file()
        print("data berhasil diubah")
    else:
        print("tidak ada data")

def header_status():
    header = input("Masukan Judul Content: ")
    while True:
        status = input("masukan status 1/2/3: ")
        if status.isdigit():
            if 1 <= int(status) <= 3:
                result_status = convert_status(status)
                return header,result_status
            else:
                print("angka 1-3")     
        else:
            print("Angka Tidak Valid")     

load_from_file()
while True:
    print("====================================")
    print("1. Tambah konten")
    print("2. Lihat konten")
    print("3. Ubah status")
    print("4. Keluar")

    choice = input("Pilih menu: ")
    if choice == "1":
        header, status = header_status()
        add_content(header, status)
    elif choice == "2":
        view_contents()
    elif choice == "3":
        done = False
        while done != True :
            header = input("Masukan Nomor Yang Mau Diubah: ")
            if header.isdigit():
                idx = int(header)
                if idx <= 0 or idx > len(contents) :
                    print("masukan angka dari 1")
                    continue
            else:
                print("Masukan angka !!")
                continue    
            status = input("masukan status 1/2/3: ")
            if status.isdigit():
                if 1 <= int(status) <= 3:
                    result_status = convert_status(status)
                    update_status_by_index(header, result_status)
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

