print('KALKULATOR KESEHATAN BMI')

berat_badan = int(input('MASUKAN BERAT BADAN : (KG) '))
tinggi_badan = int(input('MASUKAN TINGGI BADAN : (M) '))

hasil_BMI = (berat_badan) / ( tinggi_badan / 100 )

if hasil_BMI < 18.5:
    print('Berat badan kurang')
elif hasil_BMI > 18.5 and hasil_BMI < 24.9:
    print('Berat badan normal')
elif hasil_BMI > 25 and hasil_BMI < 29.9:
    print('Kelebihan berat badan')
else:
    print('OBESITAS')

