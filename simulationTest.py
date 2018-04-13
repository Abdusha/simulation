import random

#inisiasi var
p = [] #harga yang ditawarkan producer
d = [] #hari kirim

q = [] #harga yang diterima konsumen
e = [] #hari dibutuhkan

untung = []
banding = 0

#input batasan
batas_m = 10000 #produsem
batas_n = 10000 #konsumen
batas_p = 10000 #harga yang ditawarkan producer
batas_d = 10 #hari pengiriman barang
batas_q = 10000 #harga yang disanggupi konsumen
batas_e = 10 #hari dibutuhkan barang

m = random.randrange(1,batas_m) #produsem
n = random.randrange(1,batas_n) #konsumen

print("Banyak producer = ",m)
print("Banyak Konsumen = ",n)

#Random penawaran producer
print("\nPenawaran Producer")
for i in range(m):
    p.append(random.randrange(1,batas_p))
    d.append(random.randrange(1,batas_d))
    print("Harga = ",p[i]," Hari = ",d[i])

#random permintaan pelanggan
print("\nPermintaan Konsumen")
for i in range(n):
    q.append(random.randrange(1, batas_q))
    e.append(random.randrange(1, batas_e))
    print("Harga = ", q[i], " Hari = ", e[i])

for i in range(m):
    for j in range(n):
        if (p[i] <= q[j]):
            if (d[i] <= e[j]):
                untung.append(q[j]-p[i])
            else:
                untung.append(0)
        else:
            untung.append(0)

print("\nKeuntungan dari penawaran dan permintaan : ")
x = m*n
for i in range(x):
    print("Ke-",i," = ",untung[i])
    if(untung[i] > banding):
        banding = untung[i]
    else:
        banding = banding

print("\nKeuntungan yang cocok adalah = ",banding)