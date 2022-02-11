
jumlah_botol_susu = 10

jumlah_telur = 8

if jumlah_botol_susu > 0:
    if jumlah_telur > 6:
        print("Budi membeli 6 butir telur dan 1 botol susu")
        jumlah_botol_susu -= 1
        jumlah_telur -= 6
    else:
        print("Budi hanya membeli 1 Botol susu")
else:
    print("Budi tak membeli apapun")


