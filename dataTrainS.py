import random

p = [1,2] #harga yang ditawarkan producer
d = [3,1] #hari kirim

q = [3,7] #harga yang diterima konsumen
e = [5,2] #hari dibutuhkan

untung = []
banding = 0


m = 1 #produsem
n = 2 #konsumen

print("Banyak producer = ",m)
print("Banyak Konsumen = ",n)

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

print("Keuntungan yang cocok adalah = ",banding)