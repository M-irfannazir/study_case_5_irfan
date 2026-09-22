def hitung_biaya_parkir(jenis_kendaraan, lama_parkir):
    # Percabangan untuk menentukan tarif berdasarkan jenis kendaraan
    if jenis_kendaraan == "mobil":
        tarif_per_jam = 5000
    elif jenis_kendaraan == "motor":
        tarif_per_jam = 3000

    total_biaya = tarif_per_jam * lama_parkir
    return total_biaya


# validasi jenis kendaraan dan jam masuk/keluar
while True:
    jenis_kendaraan = input("Masukkan jenis kendaraan (mobil/motor): ").lower()
    if jenis_kendaraan in ["mobil", "motor"]:
        break
    else:
        print("Jenis kendaraan tidak tersedia! Hanya menerima mobil atau motor.\n")

while True:
    jam_masuk = int(input("Masukkan jam masuk (contoh 8): "))
    jam_keluar = int(input("Masukkan jam keluar (contoh 11): "))
    lama_parkir = jam_keluar - jam_masuk

    if lama_parkir > 0:
        break
    else:
        print("Jam keluar harus lebih besar dari jam masuk!\n")

# Memanggil function untuk menghitung biaya
total_biaya = hitung_biaya_parkir(jenis_kendaraan, lama_parkir)

# Menampilkan hasil
print("\n===== STRUK PARKIR =====")
print(f"Jenis Kendaraan : {jenis_kendaraan}")
print(f"Jam Masuk       : {jam_masuk}:00")
print(f"Jam Keluar      : {jam_keluar}:00")
print(f"Lama Parkir     : {lama_parkir} jam")
print(f"Total Biaya     : Rp{total_biaya}")