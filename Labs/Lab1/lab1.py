print("Hello, World!")

a = 10
print(a)

a = "String"
print(a)

# b = '1'
# b = b + 5
# print(b)

stringForSplitting = "Seminar pachete software"
print("a[1]: " + stringForSplitting[1])
print("a[2:5]: ", stringForSplitting[2:5])
print("a.strip(): ", stringForSplitting.strip())

lista = ["laptop", "creion", "flipchart"]
lista.insert(1, "rucsac")
print(lista) 

lista = ["laptop", "creion", "flipchart"]
lista.remove("laptop")
print(lista) 

lista = ["laptop", "creion", "flipchart"]
lista.pop()
print(lista) 

lista = ["laptop", "creion", "flipchart"]
del lista [0]
print(lista)