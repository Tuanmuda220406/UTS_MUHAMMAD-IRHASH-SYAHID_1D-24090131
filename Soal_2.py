inputtahun = int(input('Masukan Tahun : '))

if inputtahun % 400 == 0:
    print(f'Tahun {inputtahun} merupakan TAHUN KABISAT')
elif inputtahun % 4 == 0 and inputtahun % 100 != 0:
    print(f'Tahun {inputtahun} merupakan TAHUN KABISAT')
else:
    print(f'Tahun {inputtahun} bukan merupakan TAHUN KABISAT')
    