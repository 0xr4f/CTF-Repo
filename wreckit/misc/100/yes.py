import zipfile

for i in range(999, 0, -1):
    with zipfile.ZipFile(f"{i}.zip", 'r') as ker:
        ker.extractall()
        for j in range(i - 1, 0, -1):
            try:
                with zipfile.ZipFile(f'{j}_password.zip', 'r') as zip:
                    with open(f"pw{j}.txt", "r") as passw:
                        z = passw.read().strip()
                        zip.extractall(pwd=z.encode())
            except FileNotFoundError:
                print(f"File 'pw{j}.txt' or '{j}_password.zip' not found.")
            except Exception as e:
                print(f"Error occurred while extracting 'pw{j}.txt' or '{j}_password.zip': {e}")
