from bs4 import BeautifulSoup

# Baca file HTML
with open("pewa.html", "r") as f:
    html = f.read()

# Parsing HTML dengan Beautiful Soup
soup = BeautifulSoup(html, "html.parser")

# Cari tag yang mengandung string "flag:"
for tag in soup.find_all(string=lambda text: "flag:" in str(text)):
    z = tag.replace("flag:","").strip()
    print(z)
#Skrip di atas akan membuka file HTML dengan nama "file.html", kemudian mem-parsing-nya dengan menggunakan Beautiful Soup. Setelah itu, skrip akan mencari semua tag dalam file HTML yang mengandung string "flag:" dan akan menampilkan semua tag yang ditemukan.





