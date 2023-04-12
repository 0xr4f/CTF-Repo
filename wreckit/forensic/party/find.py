import re

# membaca file
with open('pewa.html', 'rb') as f:
    file_data = f.read()

# mencari pola hex tanpa 0x atau \xx
pattern = re.compile(rb'[0-9a-fA-F]+')

# mencetak semua string hex yang ditemukan
for match in re.findall(pattern, file_data):
    print(match.decode())
