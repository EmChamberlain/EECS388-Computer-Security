from pymd5 import md5
from pymd5 import padding


def test():
    m = "Use HMAC, not hashes"
    h = md5()
    h.update(m)
    print h.hexdigest()

    h = md5(state="3ecc68efa1871751ea9b0b1a5b25004d".decode("hex"), count=512)
    x = "Good advice"
    h.update(x)
    print h.hexdigest()

    h = md5()
    h.update(m + padding(len(m)*8) + x)
    print h.hexdigest()


def main():
    test()

if __name__ == "__main__":
    main()