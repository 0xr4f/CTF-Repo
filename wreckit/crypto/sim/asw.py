from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from Crypto.Util.number import bytes_to_long, long_to_bytes

enc1_hex = input("Masukkan ciphertext pertama dalam bentuk hex: ")
enc2_hex = input("Masukkan ciphertext kedua dalam bentuk hex: ")
added_fake_flag = int(input("Masukkan nilai yang digunakan untuk 'menambah' pesan asli dengan fake flag: "))

enc1 = bytes.fromhex(enc1_hex)
enc2 = bytes.fromhex(enc2_hex)

# Mengambil key dari pesan yang pertama dienkripsi
key = enc1[:32]

# Mengambil bagian pesan yang sesuai
ct1 = enc1[32:]
ct2 = enc2[32:]

# Mengembalikan nilai fake flag
fake_flag = ct2[:32]
fake_flag_int = bytes_to_long(fake_flag) - bytes_to_long(fake_flag[:16] + bytes([0]) * 15)
fake_flag_int -= added_fake_flag
fake_flag = long_to_bytes(fake_flag_int)

# Dekripsi pesan asli
cipher1 = AES.new(key, AES.MODE_CBC, bytes([0] * 16))
cipher2 = AES.new(key, AES.MODE_CBC, bytes([0] * 16))
pt1 = unpad(cipher1.decrypt(ct1), 16)
pt2 = unpad(cipher2.decrypt(ct2), 16)

# Hapus bagian flag dari pesan asli dan ambil bagian pesan asli yang sesuai
flag_idx = pt1.index(flag)
pt1 = pt1[:flag_idx] + pt1[flag_idx + len(flag):]
pt2 = pt2[:flag_idx] + pt2[flag_idx + len(flag):]
pt2 = pt2[:16] + fake_flag + pt2[16 + len(fake_flag):]

# Hasil dekripsi
print("Hasil dekripsi:")
print(pt1)
print(pt2)
