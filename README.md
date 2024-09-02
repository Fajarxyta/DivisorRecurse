# DivisorRecurse

**DivisorRecurse** adalah program Python sederhana yang digunakan untuk mencari angka-angka dalam suatu rentang yang dapat dibagi dengan angka lain (divisor) tanpa sisa. Program ini menggunakan pendekatan rekursif dan fungsi lambda untuk menyaring angka yang sesuai dengan divisor yang ditentukan.

## Fitur

- Mencari angka yang dapat dibagi dengan angka lain dalam suatu rentang tertentu.
- Menggunakan rekursi untuk menghitung angka-angka yang memenuhi kriteria.
- Penyaringan tambahan menggunakan fungsi lambda dan filter.

## Penggunaan

*Clone repository ini ke komputer Anda.*
   
   ```bash
   git clone https://github.com/Fajarxyta/DivisorRecurse
   cd DivisorRecurse
   python
   ```

## Contoh Code
```bash
batas_atas = 40
divisor = 7

hasil_awal = cari_angka_bagi_rekursif(batas_atas, divisor)
hasil_akhir = filter_dengan_lambda(hasil_awal, divisor)

print(f"Angka yang dapat dibagi dengan {divisor} dari 1 hingga {batas_atas}:")
print(hasil_akhir)
```
