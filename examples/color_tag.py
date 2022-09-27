'''Penulisan tanda warna pada library rgbpy'''

from rgbpy import rtext

# Info
'''
Kami menyediakan sekitar 140 kunci tag warna. Untuk melihat semua kunci tag warna, anda
bisa mengeksekusi "default.py". Anda bahkan bisa menambahkan warna rgb yang anda inginkan,
lihat tutorial pada "set_color.py".
'''

#
'''
Tag warna

Untuk memberikan warna pada sebuah teks, anda hanya perlu memberikan sebuah tag
dibelakang teks tersebut. Tag warna pada library rgbpy hanya sesimple (red), yaitu
anda hanya perlu membuat kurung buka kemdian memasukkan nama tag warna yang ingin
digunakan dan kemudian membuat kurung tutup. Misalnya tag warna kuning adalah hanya
sesimple ini (yellow).

perhatikan contoh dibawah:
'''

teks = rtext('(lime)TEKS INI BERWARNA LIME')
print(teks)


#
'''
Anda bisa memberikan lebih dari 1 tag warna seperti berikut.
'''

teks = rtext('(magenta)TEKS INI BERWARNA MAGENTA (orange)TEKS INI BERWARNA ORANGE')
print(teks)


#
'''
Anda juga bisa membuat teks dengan backgroud berwarna. Tag yang bisa anda gunakan adalah
sebagai berikut: (cyan$red)
Yang berarti teks berwarna merah dengan background berwarna cyan.

Untuk lebih jelas lihat contoh dibawah.
'''

teks = rtext('(yellow$magenta)TEKS BERWARNA MAGENTA DENGAN BACKGROUND BERWARNA KUNING')
print(teks)


#
'''
Tag (*stop)

Tag (*stop) memiliki fungsi untuk menandai dimana sebuah tag warna akan berakhir.
'''

teks = rtext('(cyan)TEKS INI BERWARNA CYAN(*stop) & INI ADALAH AKHIR DARI WARNA CYAN')
print(teks)

teks = rtext('(lime$red)INI TEKS DENGAN BACKGROUND(*stop) & BERAKHIR DISINI')
print(teks)
