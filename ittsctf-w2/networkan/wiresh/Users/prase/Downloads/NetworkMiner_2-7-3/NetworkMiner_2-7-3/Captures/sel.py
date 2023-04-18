import re

# Membuka file yang akan di-scrape
with open("NM_2022-05-14T11-38-55.pcap",encoding="iso-8859-1") as f:
    data = f.read()

# Mencari semua alamat IP dalam file
ip_addresses = re.findall(r"\b(?:\d{1,3}\.){3}\d{1,3}\b", data)

# Mencari semua nomor port dalam file
ports = re.findall(r"\b\d{1,5}\b", data)

# Menampilkan hasil pencarian
print("IP Addresses:")
for ip in ip_addresses:
    print(ip).split()

print("\nPorts:")
for port in ports:
    print(port).split()
