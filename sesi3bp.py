print("NIM : 20210801180")
print("NAMA : Sadat Ardiansyah")

#Penjumlahan
print("buah")
print(13 + 2)
kurma = 13
kedondong = 2
buah = kurma + kedondong 

#Pengurangan
hutang = 25000
bayar = 5000
sisaHutang = hutang - bayar
print("Sisa hutang Anda adalah ", sisaHutang)

#Perkalian
panjang = 20
lebar = 5
luas = ("20 * 5")
print("luas")

#Pembagian
masker = 50
remaja = 5
maskerPerRemaja = masker / remaja
print("Setiap remaja akan mendapatkan bagian masker sebanyak ", maskerPerRemaja)

print ("Penjumlahan matriks ordo 2x2")

matriks1 = [
        [22,24] ,
        [25,26] ,

]

matriks2 = [
    [30, 40] ,
    [45, 55] ,

]
for x in range(0, len(matriks1)) :
    for y in range(0, len(matriks1[0])) :
        print (matriks1 [x] [y] + matriks2 [x] [y], end='')
    print ('')
    