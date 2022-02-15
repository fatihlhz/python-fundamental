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

# Cara ambil value berdasarkan index dan disimpan di temp.variabel
buku1 = list_buku.pop(0)
for buku in list_buku:
    print(buku)

print(buku1)

# Cara hapus list di index tertentu
del list_buku[0 : 2]
for buku in list_buku:
    print(buku)
