# study_case_5_irfan

Nama    : Muhammad Irfan Nazir
Kelas   : B
NIM     : 2609116070
Soal    : Genap



# Sistem Perhitungan Biaya Parkir

>> Penjelasan

1. def hitung_biaya_parkir(jenis_kendaraan, lama_parkir):

Membuat function dengan dua parameter: jenis kendaraan dan lama parkir dalam jam. Ini akan diisi datanya saat function dipanggil nanti.

2. if jenis_kendaraan == "mobil": elif jenis_kendaraan == "motor":

percabangan (conditional statement) yang menentukan tarif per jam berdasarkan jenis kendaraan.

3. total_biaya = tarif_per_jam * lama_parkir

Menghitung total biaya dengan mengalikan (operator *) tarif per jam dengan lama parkir.

4. return total_biaya

Mengembalikan hasil perhitungan dari dalam function ke bagian program yang memanggilnya.

5. Looping pertama — validasi jenis kendaraan

while True akan terus meminta input selama jenis kendaraan yang dimasukkan bukan "mobil" atau "motor". Kalau sudah valid, break menghentikan loop.

6. Looping kedua — validasi jam masuk & keluar

while True memastikan jam_keluar lebih besar dari jam_masuk, sehingga lama_parkir (hasil pengurangan) selalu positif dan masuk akal.

7. total_biaya = hitung_biaya_parkir(jenis_kendaraan, lama_parkir)

Pemanggilan function (mengirim data yang sudah divalidasi ke function, lalu menyimpan hasil return-nya ke variabel total_biaya.)

8. Print(f"...")

Menampilkan hasil akhir sebagai struk parkir menggunakan f-string, supaya nilai variabel bisa langsung disisipkan ke dalam teks output.

>> Output

<img width="899" height="354" alt="Screenshot 2026-09-22 182234" src="https://github.com/user-attachments/assets/77ebaf92-b020-4c84-9a96-822a189a898a" />
