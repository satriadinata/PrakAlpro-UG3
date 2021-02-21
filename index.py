# satriadinata ratnanto 71200626
# ada seorang siswa yang kesulitan untuk mencari urutan bilangan prima
# dari n sampai n dimana dia bisa custom input bilangan itu
awal = int(input('Masukkan bilangan awal : '))
akhir = int(input('Masukkan bilangan akhir : '))
result=[]
for i in range (awal,akhir+1):
    if i >1 and i % 2 != 0 and i % 3 != 0 and i % 5!=0 and i%6 != 0 and i%7 != 0 and i%8 !=0 and i%9!=0 or i==9 or i==8  or i==7 or i==6 or i==5 or i == 2 or i == 3 :
        result.append(i)
print('Diatara', awal, 'dan', akhir,'ada bilangan prima yaitu', result)
print('Ada sejumlah', len(result),'bilangan')