# labpy03
#---------------------------------------------------------------------------
NAMA: Mayscela Herliyawati 

NIM: 312510371

KELAS: TI.25.C5

Pertemuan 7

## LAPORAN PRATIKUM 4 
#---------------------------------------------------------------------------
### LATIHAN 1 (BILANGAN KURANG DARI 0.5) 
Perhatikan syntax berikut ini : 

![image](https://github.com/scellaa/labpy03/blob/5307a549bf7026e8f34e311b0a7c54b01a4a2b66/python%20picture%20(input%20n%20output)/INPUT%20LAT%201%20(KURANG%20DARI%200.5)%20PERTEMUAN%207.jpg) 

Pada latihan pertama ini kita perlu menentukan bilangan yang lebih besar dibanding dengan bilangan 0,5. Untuk memenuhi kriteria tersebut kita harus memasukan variabel < (less than) 0.5 agar programan mengetahui intruksi yang kita inginkan. 
1. Penggunaan kode random.random untuk menghasilkan hasil acak pada outputnya.
2. Pada line 2, kita harus memasukan nilai pada saat runtime code nya
3. for i in range (n), pada kode syntax ini kita akan melakukan pengulangan sesuai dengan jumlah yang di input pada line 2 (n)
4. Sementara while True digunakan untuk perulangan non sequence dan berkolaborasi dengan syntax for range yang terdapat pada line 2, dimana for range sendiri adalah perulanga sequence (terkira). perulangan for ini hanya menentukan bahwa program harus menghasilkan output perulangan sesuai dengan (n).
5. Dapat dilihat pada line 6 bahwa kita harus menjelaskan perhitungan seperti apa yang kita butuhkan, karena kita sedang mencari bilangan yang kurang dari 0.5 maka gunakan (<) dan kode akan menghasilkan hasil yang kurang dari 0.5
6. Break merupakan bagian penutup dari kode ini
   
Ini adalah outputnya:

![image](https://github.com/scellaa/labpy03/blob/b1d5ae605358c8608cea700af0af35ac1b59a21d/python%20picture%20(input%20n%20output)/OUTPUT%20LAT%201%20(KURANG%20DARI%200.5)%20PERTEMUAN%207.jpg)

#----------------------------------------------------------------------------
### LATIHAN 2 (MENGHITUNG LABA SELAMA 8 BULAN) 
Perhatikan syntax dibawah ini: 

![image](https://github.com/scellaa/labpy03/blob/0b3ed2fb4a1f156491c49385c26ce24805353d60/python%20picture%20(input%20n%20output)/LABA%201%20.jpg)

Sebuah pengusaha mempunyai modal awal sebesar RP100,000,000,00 dan pada bulan ke-3 hingga ke-4 mendapatkan laba sebesar 1%, kemudian pada bulan ke-5 hingga bulan ke-7 mendapatkan kenaikan laba yang signifikan sebanyak 5%, namun pada bulan ke-8 mengalami penuruan laba sebanyak 2% jadi hanya mendapatkan laba sebanyak 3%. Berikut penjelasan kodenya:
1. Pada line 8, kita menggunakan range 8 karena yang ingin dicari adalah laba selama 8 bulan
2. Lalu setelah itu kita menentukan keuntungan laba selama 8 bulan itu dengan menggunakan rumus yang tertera pada line 9
3. Setelah itu cetak laba keuntungan perbulan dengan syntax seperti di line 11, maksud dari {bulan+1} adalah setiap variabel bulan bertambah 1 sebanyak 8x
   
Berikut merupakan hasil outputnya:

![image](https://github.com/scellaa/labpy03/blob/c2d69d183b4f29c0bb321befc5d09e0caf40c646/python%20picture%20(input%20n%20output)/LABA%202.jpg)

#-----------------------------------------------------------------------------
### LATIHAN 3 (MEMBUAT ATM SEDERHANA)
Perhatikan syntax dibawah ini:

![image](https://github.com/scellaa/labpy03/blob/b1d5ae605358c8608cea700af0af35ac1b59a21d/python%20picture%20(input%20n%20output)/INPUT%20LAT%203%20(ATM)%20PERTEMUAN%207.jpg)

Seseorang ingin menarik uang dari sebuah atm sederhana, dan saldo yang ia miliki adalah Rp1000,0000,00. Begini penjelasan kodenya:
1. Kita menggunakan rumus while True karena perulangan ini non sequence, perulangan while true akan berhenti jika sudah mendapatkan hasil yang diinginkan.
2. Pada syntax ini kita menggunakan rumus if dan elif untuk mengetahui keputusan yang di input seorang user
3. Untuk menghitung sisa saldo yang tertera pada rekening, kita menggunakan rumus operan (-) contohnya antaralain adalah {s_awal - jml}
perhatikan output dibawah ini:

![image](https://github.com/scellaa/labpy03/blob/b1d5ae605358c8608cea700af0af35ac1b59a21d/python%20picture%20(input%20n%20output)/OUTPUT%20LAT%203%20(ATM)%20PERTEMUAN%207.jpg)
