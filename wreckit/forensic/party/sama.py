import re

with open('ini.txt', 'r') as f:
    data = f.read()

flags = set(re.findall(r'6272305f636861:\w+', data))
for flag in flags:
    data = data.replace(flag, '')

print(data)

