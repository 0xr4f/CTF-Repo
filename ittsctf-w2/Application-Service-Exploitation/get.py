from ftplib import FTP

ftp = FTP('103.146.182.227')  # Ganti 'ftp.example.com' dengan alamat FTP yang diinginkan
ftp.login(user='anonymous', passwd='anonymous')  # Ganti 'username' dan 'password' dengan kredensial login FTP yang valid

directory = '.'  # Ganti '/path/to/directory' dengan direktori yang ingin di-download

ftp.cwd(directory)  # Pindah ke direktori yang diinginkan

files = ftp.nlst()  # Mengambil daftar file dalam direktori

for filename in files:
    with open(filename, 'wb') as f:
        ftp.retrbinary('RETR ' + filename, f.write)

ftp.quit()

print('Semua file di dalam direktori', directory, 'telah berhasil di-download.')
