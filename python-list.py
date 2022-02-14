# Ini adalah contoh tipe data list(array) di python
list_buku = ['Pulang-Pergi', 'Negeri Ujung Tanduk', 'Satu Hati']

# Cara akses value di index tertentu
print(list_buku[0])
print(list_buku[1])
print(list_buku[2])

# Cara iterasi list
for buku in list_buku:
    print(buku)

# Cara tambah value baru di list
list_buku.append('Mink')
for buku in list_buku:
    print(buku)
