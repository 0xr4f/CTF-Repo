binary = input("Masukkan bilangan biner: ")

# Memastikan input merupakan bilangan biner
if set(binary) - set('01'):
    print("Input bukan bilangan biner.")
    exit()

# Mengkonversi biner menjadi desimal
decimal = int(binary, 2)

# Memastikan bilangan desimal berada dalam rentang IP yang valid
if not 0 <= decimal <= 4294967295:
    print("Bilangan biner tidak valid untuk IP.")
    exit()

# Mengkonversi desimal menjadi alamat IP
octets = []
for i in range(4):
    octet = decimal % 256
    octets.append(str(octet))
    decimal //= 256

# Membalikkan urutan oktet untuk menghasilkan format yang benar
octets.reverse()

ip_address = ".".join(octets)
print("Alamat IP yang sesuai adalah:", ip_address)
