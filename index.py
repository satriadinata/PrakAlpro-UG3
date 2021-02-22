# satriadinata ratnanto 71200626
# ada seorang siswa yang kesulitan untuk mencari urutan bilangan prima
# dari n sampai n dimana dia bisa custom input bilangan itu
awal = int(input('Masukkan angka awal : '))
akhir = int(input('Masukkan angka akhir : '))
result=[]
for i in range(awal,akhir+1):
    if i > 1 and i <= 10 and i % 2 !=0 and i % 3 !=0 or i == 2 or i == 3:
        result.append(i)
    elif i > 10 and i%2 !=0 and i%3!=0 and i%4!=0 and i%5!=0 and i%6!=0 and i%7!=0 and i%8!=0 and i%9!=0:
        result.append(i)
print('Diantara', awal,'sampai', akhir, 'ada bilangan prima yaitu :', result)
print('Ada sejumlah', len(result),'bilangan')