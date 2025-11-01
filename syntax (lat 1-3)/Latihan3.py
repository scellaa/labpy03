S_awal = 1000000

print('Hello, Welcome to Autori Bank!')
print('Saldo anda saat ini 1000000')
print('1. Tarik tunai')
print('2. Exit')

while True:
    n =input('1/2: ')
    if n == "1":
        jml =int(input('Masukkan jumlah penarikan: '))
        if S_awal > jml:
            print('Penarikan Berhasil')
            print('Sisa saldo:', (S_awal - jml))
            print('Ingin menarik lagi? [1/2]:')
    elif n == "2":
            print('Terimakasih sudah menggunakan Bank Autori')
            break

            
            
