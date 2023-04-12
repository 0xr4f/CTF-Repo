from PIL import Image

# Load gambar
img = Image.open('output.jpg')

# Ubah ke mode RGB (jika tidak sudah)
img = img.convert('RGB')

# Ambil semua piksel
piksel = img.load()

# Set untuk menyimpan semua warna yang ada
daftar_warna = set()

# Loop untuk setiap piksel
for i in range(img.size[0]):
    for j in range(img.size[1]):
        # Ambil warna piksel
        warna = piksel[i, j]

        # Tambahkan warna ke set
        daftar_warna.add(warna)

# Cetak semua warna yang ada
print("Warna yang ada pada gambar:")
for warna in daftar_warna:
    print(warna)
