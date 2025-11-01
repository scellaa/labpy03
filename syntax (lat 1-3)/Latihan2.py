m_a = 10000000
t_l = 0
tingkat_laba = [0,0,1,1,5,5,5,3]
print('Laporan laba selama 8 bulan')
print('---------------------------')


for bulan in range(8):
    keuntungan_bulanan = (tingkat_laba [bulan]) * m_a
    t_l += keuntungan_bulanan
    print('Bulan',{bulan+1},'Keuntungan =',{keuntungan_bulanan})
print("Total keuntungan selama 8 bulan:",{t_l})
