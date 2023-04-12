import zipfile

for i in range(999, 0, -1):
    with zipfile.ZipFile.extractall(f"{i}.zip") as ker: 
        with zipfile.ZipFile(f'{i}_password.zip', 'r') as zip:
            with open(f"pw{i}.txt", "r") as passw:
              z = passw.read().strip()
              zip.extractall(pwd=z.encode())
#		with zipfile.extractall(f"{i}.zip")
