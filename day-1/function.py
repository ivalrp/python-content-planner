# function atau method

# pada python lebih sederhana lagi

def say_hello():
     print("heloo")

# cara panggilnya pun sama
say_hello()

# dengan parameter

def greet(name):
     print("Hello", name)

greet("tami")

# return tidak sama dengan print

def sum(a,b):
     return a+b

print(sum(1,4))

# bisa juga menggunakan default parameter
def welcome(name="guest"):
     print("hello",name)

welcome("rohim")

# blok dalam python bukan di kurung kurawal
# sehingga perlu di perhatikan tata letak

#coba coba 

def is_even(numbers):
     for number in numbers:
          if number == 7:
               print("true")

def count_data(data_list):
     return len(data_list)

def unique_sorted(data_list):
     unique_data = set(data_list)
     return list(unique_data)

data_lists = [1,2,3,4,7,7,4,32,54,32,1,4,6]

is_even(data_lists)
print(count_data(data_lists))
print(unique_sorted(data_lists))