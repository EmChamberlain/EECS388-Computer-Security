from roots import *
import hashlib
import sys
import math
from bisect import bisect

def trailing(n):
    """Count the number of trailing zero bits in abs(n)."""
    if not n:
        return 0
    t = 0
    while not n & 1:
        n >>= 1
        t += 1
    return t

def bitcount(n):
    """Calculate bit size of the nonnegative integer n."""
    bc = bisect(powers, n)
    if bc != 300:
        return bc
    bc = int(math.log(n, 2)) - 4
    return bc + bctable[n>>bc]




# message = sys.argv[1]
message = "eecs388+jdoe+1.23"

e = 3

msg_beg = "0001FF003031300d060960864801650304020105000420"

sha = hashlib.sha256()
sha.update(message)
hash = sha.hexdigest()

msg = (msg_beg + hash + ("00" * 201))
forged_signature = integer_nthroot(int(msg.encode(), 16), e)[0]
integer = 1
while (forged_signature**e < int(msg, 16)):
    forged_signature = integer_nthroot(int(msg.encode(), 16) + integer, e)[0]
    integer <<= 8



hex_str_sig = "%0512x"%(forged_signature**e)
print msg[:110]
print hex_str_sig[:110]

print integer_to_base64(forged_signature)
