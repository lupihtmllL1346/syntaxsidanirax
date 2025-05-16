#NILAI SIDANIRA
def minta_nilai(pelajaran):
    while True:
        try:
            return int(input(f"{pelajaran}?: "))
        except ValueError:
            print("0")

print("NILAI SIDANIRA")

#kelas 7 8 9 mtk
m1tujuh = minta_nilai('Matematika Semester 1')
m2tujuh = minta_nilai('Matematika Semester 2')

m1delapan = minta_nilai('Matematika Semester 3')
m2delapan = minta_nilai('Matematika Semester 4')

m1sembilan = minta_nilai('Matematika Semester 5')

total1 = (m1tujuh + m2tujuh + m1delapan + m2delapan + m1sembilan) / 5
print(f"\n Rata-rata Matematika: {total1}")

#kelas 7 8 9 ipa
i1tujuh = minta_nilai('IPA Semester 1')
i2tujuh = minta_nilai('IPA Semester 2')

i1delapan = minta_nilai('IPA Semester 3')
i2delapan = minta_nilai('IPA Semester 4')

i1sembilan = minta_nilai('IPA Semester 5')

total2 = (i1tujuh + i2tujuh + i1delapan + i2delapan + i1sembilan) / 5
print(f"\n Rata-rata IPA: {total2}")

#kelas 7 8 9 ips
ii1tujuh = minta_nilai('IPS Semester 1')
ii2tujuh = minta_nilai('IPS Semester 2')

ii1delapan = minta_nilai('IPS Semester 3')
ii2delapan = minta_nilai('IPS Semester 4')

ii1sembilan = minta_nilai('IPS Semester 5')

total3 = (ii1tujuh + ii2tujuh + ii1delapan + ii2delapan + ii1sembilan) / 5
print(f"\n Rata-rata IPS: {total3}")

#kelas 7 8 9 Bindo
bi1tujuh = minta_nilai('BAHASA INDONESIA Semester 1')
bi2tujuh = minta_nilai('BAHASA INDONESIA Semester 2')

bi1delapan = minta_nilai('BAHASA INDONESIA Semester 3')
bi2delapan = minta_nilai('BAHASA INDONESIA Semester 4')

bi1sembilan = minta_nilai('BAHASA INDONESIA Semester 5')

total4 = (bi1tujuh + bi2tujuh + bi1delapan + bi2delapan + bi1sembilan) / 5
print(f"\n Rata-rata BAHASA INDONESIA: {total4}")

#kelas 7 8 9 Binggris
bing1tujuh = minta_nilai('BAHASA INGGRIS Semester 1')
bing2tujuh = minta_nilai('BAHASA INGGRIS Semester 2')

bing1delapan = minta_nilai('BAHASA INGGRIS Semester 3')
bing2delapan = minta_nilai('BAHASA INGGRIS Semester 4')

bing1sembilan= minta_nilai('BAHASA INGGRIS Semester 5')

total5 = (bing1tujuh + bing2tujuh + bi1delapan + bing2delapan + bing1sembilan) / 5
print(f"\n Rata-rata BAHASA INGGRIS: {total5}")

#total nilai semester 1 2 3 4 5

print('Rata-Rata Kelas dari Semester 1-5')
totalsemester1kelas7 = (m1tujuh + i1tujuh + ii1tujuh + bi1tujuh + bing1tujuh) / 5
print(f"\n Rata-rata Kelas 7 Semester 1: {totalsemester1kelas7}")

totalsemester2kelas7 = (m2tujuh + i2tujuh + ii2tujuh + bi2tujuh + bing2delapan) / 5
print(f"\n Rata-rata Kelas 7 Semester 2: {totalsemester2kelas7}")

totalsemester1kelas8 = (m1delapan + i1delapan + ii1delapan + bi1delapan + bing1delapan) / 5
print(f"\n Rata-rata Kelas 8 Semester 1: {totalsemester1kelas8}")

totalsemester2kelas8 = (m2delapan + i2delapan + ii2delapan + bi2delapan + bing2delapan) / 5
print(f"\n Rata-rata Kelas 8 Semester 2: {totalsemester2kelas8}")

totalsemester1kelas9 = (m1sembilan + i1sembilan + ii1sembilan + bi1sembilan + bing1sembilan) / 5
print(f"\n Rata-rata Kelas 9 Semester 1: {totalsemester1kelas9}")


totalall = (total1 + total2 + total3 + total4 + total5)

print(f"\n Rata-rata Keseluruhan/SIDANIRA: {totalall / 5}")
