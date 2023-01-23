####### contoh fungsi ######
def penjumlahan(x, y):
    return x + y



hasil = penjumlahan(23, 5)
print(hasil)
# Output: 28



###### contoh fungsi rekursif #####
def faktorial(n):
    if n == 1:
        return 1
    else:
        return n * faktorial(n-1)




hasil = faktorial(5)
print(hasil)
# Output: 120