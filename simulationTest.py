import random
import time

#inisiasi var
p = [] #harga yang ditawarkan producer
d = [] #hari kirim

q = [] #harga yang diterima konsumen
e = [] #hari dibutuhkan

untung = []
upj = [] #array list untung penjual
upm = [] #array list untung pembeli
banding = 0
bpj = 0 #array list temp banding penjual
bpm = 0 #array list temp banding pembeli

#input batasan
batas_m = 6000 #penjual
batas_n = 6000 #pembeli
batas_p = 1000000000 #harga yang ditawarkan penjual
batas_d = 30 #hari pengiriman barang
batas_q = 1000000000 #harga yang disanggupi penjual
batas_e = 30 #hari dibutuhkan barang

m = random.randrange(1,batas_m) #penjual
n = random.randrange(1,batas_n) #pembeli

print("Banyak Penjual = ",m)
print("Banyak Pembeli = ",n)

#Random penawaran producer
# print("\nPenawaran Penjual . . . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .") #matiin juga
for i in range(m):
    p.append(random.randrange(1,batas_p))
    d.append(random.randrange(1,batas_d))
    # print("Penjual ke-",i,", Harga = ",p[i]," Hari = ",d[i]) #kalo ga pengen liat hidden aja

#random permintaan pelanggan
# print("\nPermintaan Pembeli . . . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .") #matiin juga
for i in range(n):
    q.append(random.randrange(1, batas_q))
    e.append(random.randrange(1, batas_e))
    # print("Pembeli ke-",i,", Harga = ", q[i], " Hari = ", e[i]) #kalo ga pengen liat hidden aja

print("\nProgress. . . . . . . . .\n") #buka ini

start = time.time()
for i in range(m):
    for j in range(n):
        if (p[i] <= q[j]):
            if (d[i] <= e[j]):
                untung.append(q[j]-p[i])
                upj.append(i)
                upm.append(j)
            else:
                untung.append(0)
                upj.append(i)
                upm.append(j)
        else:
            untung.append(0)
            upj.append(i)
            upm.append(j)

x = m*n
for i in range(x):
    # print("Ke-",i," = ",untung[i])
    if(untung[i] > banding):
        banding = untung[i]
        bpj = upj[i]
        bpm = upm[i]
    else:
        banding = banding
        bpj = bpj
        bpm = bpm

print("\nPenjual dan Pembeli yang cocok adalah:")
print("Penjual ke-",bpj,"dan Pembeli ke-",bpm,"dengan keuntungan =",banding)
end = time.time()
print("\nLama running =",(end - start),"detik")
