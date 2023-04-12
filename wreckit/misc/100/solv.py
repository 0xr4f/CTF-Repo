from zipfile import ZipFile
def zip_file():
	for i in range(999,998,-1):
		low = ZipFile(f"{i}_password.zip")
def passwr():
	for i in range(999,0,-1):
		z = open(f"pw{i}.txt","r")
#zip_file()
import zipfile

for i in range(999, 0, -1):
    with zipfile.ZipFile(f'{i}_password.zip', 'r') as zip:
        passw = open(f"pw{i}.txt","r")
        z = passw.read()
        zip.extractall(None,None,z)

