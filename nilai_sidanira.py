def minta_nilai(pelajaran):
    while True:
        try:
            return int(input(f"{pelajaran}?: "))
        except ValueError:
            print("0")

print("SIDANIRA")

#kelas 7 8 9 mtk
mtujuh = minta_nilai('Matematika')
mdelapan = minta_nilai('Matematika')
msembilan = minta_nilai('Matematika')
total1 = (mtujuh + mdelapan + msembilan) / 3

#kelas 7 8 9 ipa
itujuh = minta_nilai('IPA')
idelapan = minta_nilai('IPA')
isembilan = minta_nilai('IPA')
total2 = (itujuh + idelapan + isembilan) / 3

#kelas 7 8 9 ips
iitujuh = minta_nilai('IPS')
iidelapan = minta_nilai('IPS')
iisembilan = minta_nilai('IPS')
total3 = (iitujuh + iidelapan + iisembilan) / 3

#kelas 7 8 9 Bindo
bitujuh = minta_nilai('BAHASA INDONESIA')
bidelapan = minta_nilai('BAHASA INDONESIA')
bisembilan = minta_nilai('BAHASA INDONESIA')
total4 = (bitujuh + bidelapan + bisembilan) / 3

#kelas 7 8 9 Binggris
bingtujuh = minta_nilai('BAHASA INGGRIS')
bingdelapan = minta_nilai('BAHASA INGGRIS')
bingsembilan= minta_nilai('BAHASA INGGRIS')
total5 = (bingtujuh + bidelapan + bingsembilan) / 3

totalall = (total1 + total2 + total3 + total4 + total5)

print(f"\n Rata-rata: {totalall / 5}")