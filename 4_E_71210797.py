import fractions

u = int(input("suku dari berapa : "))
un = int(input("suku akhir : "))
a = float(input("angka awal :"))
r = float(input("rasio :"))

hasil=0
for n in range(u, un+1):
    suku = a*(r**(n-1))
    hasil = hasil + suku
    print(suku)

print('jumlah semua suku (Sn) = ',hasil)

