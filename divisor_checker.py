def cari_angka_bagi_rekursif(angka, divisor):
    # Basis rekursi: Jika angka lebih kecil dari divisor, hentikan dan kembalikan list kosong
    if angka < divisor:
        return []
    
    # Rekursi: Periksa apakah angka sekarang bisa dibagi dengan divisor
    hasil_sekarang = [angka] if angka % divisor == 0 else []
    
    # Gabungkan hasil rekursi dari angka sebelumnya dengan hasil sekarang
    return cari_angka_bagi_rekursif(angka - 1, divisor) + hasil_sekarang

def filter_dengan_lambda(hasil, divisor):
    # Menggunakan fungsi lambda dan filter untuk menyaring angka yang habis dibagi divisor
    return list(filter(lambda x: x % divisor == 0, hasil))

# Contoh penggunaan
batas_atas = 100
divisor = 6

# Menggunakan fungsi rekursif untuk mendapatkan semua angka dari batas atas ke bawah
hasil_awal = cari_angka_bagi_rekursif(batas_atas, divisor)

# Menyaring hasil menggunakan lambda
hasil_akhir = filter_dengan_lambda(hasil_awal, divisor)

print(f"Angka yang dapat dibagi dengan {divisor} dari 1 hingga {batas_atas}:")
print(hasil_akhir)
