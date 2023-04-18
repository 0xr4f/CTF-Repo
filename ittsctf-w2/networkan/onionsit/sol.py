from PIL import Image
import struct
import io

# membuka file PNG yang rusak
with open('flag4.png', 'rb') as f:
    data = f.read()

# memperbaiki kesalahan dengan mengganti panjang chunk yang tidak valid
fixed_data = data.replace(b'\x00\r\n\x00\x00\x00\x0D', b'\x00\r\n\x00\x00\x00\x0A')

# membaca gambar menggunakan PIL
img = Image.open(io.BytesIO(fixed_data))

# menyimpan gambar yang telah diperbaiki
img.save('fixed_flag4.png')
