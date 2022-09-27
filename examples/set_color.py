'''Set color (menambahkan warna) pada library rgbpy'''

import rgbpy


#
'''
Anda dapat menambahkan sendiri tag warna dengan kode rgb yang diinginkan.
Untuk contoh penggunaannya silahkan lihat dibawah.


Ada beberapa aturan yang harus anda ikuti yaitu sebagai berikut:

1. Anda bisa menambahkan tag warna yang telah ada tetapi anda tidak bisa menambahkan
   tag warna dengan nama *stop karena tag tersebut memiliki fungsi spesifik.
2. Nama untuk tag tidak boleh mengandung kurung buka & kurung tutup karena bisa
   menyebabkan ketidak terbacaan tag pada saat dipanggil.
3. Value harus bertipe data tuple dengan 3 item didalamnya & masing-masing item tersebut
   harus bertipe data integer dengan nilai min 0 max 255.

'''

#
'''
Misalnya saya ingin menambahkan tag birumuda dengan value (79,195,247) & tag
ungu_pudar dengan value (255,183,252) maka saya perlu membuat setter seperti dibawah:
'''

rgbpy.SetColor({
	'birumuda': (79,195,247),
	'ungu_pudar': (255,183,252),
})


#
'''
Kemudian anda bisa menggunakannya seperti biasa.
'''

teks = rgbpy.rtext('(birumuda)INI TAG BIRUMUDA YANG SAYA TAMBAHKAN')
print(teks)

teks = rgbpy.rtext('(ungu_pudar)INI TAG UNGU_PUDAR YANG SAYA TAMBAHKAN')
print(teks)

teks = rgbpy.rtext('(ungu_pudar$black)SEKARANG SAYA BISA MENGGUNAKAN TAG YANG SAYA TAMBAHKAN(*stop)')
print(teks)


#
'''
Anda bisa menemukan komponen warna rgb di https://redketchup.io/color-picker atau
wesite/aplikasi lainnya.
'''
