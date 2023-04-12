from PIL import Image

# load gambar
img = Image.open("nama_gambar_baru.png")

# ambil data pixel gambar
pixel_data = img.load()

# loop melalui semua piksel gambar dan ganti warna yang sesuai
for i in range(img.size[0]):
    for j in range(img.size[1]):
        if pixel_data[i, j] == (247, 223, 211):
            pixel_data[i, j] = (0, 0, 0)

# simpan gambar yang sudah diubah warnanya
img.save("baru.png")
