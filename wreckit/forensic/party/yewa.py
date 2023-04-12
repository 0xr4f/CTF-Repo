with open('ini.txt', 'r') as f:
    lines = f.readlines()

unique_lines = set(lines)
with open('unik.txt', 'w') as f:
    for line in unique_lines:
        if line.strip() != "":
            f.write(line)
