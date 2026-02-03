# sudah pernah bahas di tipe-data

def separator():
    print()
    print("======================================================")
#list
names = ["ival", "kirom", "riski", "dimas"]

print(names)
names.append("sena")
names.append("ari")

print(names)
names.remove("ari")

print(names)

names.remove(names[4])
for name in names:
    print(name)

# tuple (immutable/tidak bisa diubah)
queue = ("001", "002", "003")

# dictionary
user = {
    "name" : "ival",
    "age" : 27
}
separator()
print(user)
for key,value in user.items():
    print(value)

# set (anti duplikat)
separator()
numbers = {1,2,4,3,4,4}
print(numbers)
numbers.add(9)
numbers.remove(3)
print(numbers)

# real case
users = [
    {"name" : "ival", "age" : 27},
    {"name" : "dimas", "age" : 28}
]
for us in users:
    print(us["name"])

separator()
# exercise
numberLists = [1,3,4,5,6,4,22,4,5]
setList = set()

for numberList in numberLists:
    setList.add(numberList)

numberLists.clear()

for item_set in sorted(setList):
    numberLists.append(item_set)

for i,itemList in enumerate(numberLists, start= 1):
    print(i, itemList)

# result

r_numbers = [1,32,56,4,23,42,45,3,2,32,2,4,5,2]

# di python bisa langsung convert
r_unique_set = set(r_numbers)

# balikin lagi jadi list juga bisa
r_unique_list = list(r_unique_set)

print(r_unique_list)