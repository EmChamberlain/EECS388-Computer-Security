from pymd5 import md5
from pymd5 import padding
import httplib, urlparse, sys
from urllib import quote


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
    # test()

    url = sys.argv[1]
    # url = "https://eecs388.org/project1/api?token=dfedf63833fcfe1221223a83185ca81c&user=admin&command1=ListFiles&command2=NoOp"

    token = url[url.find("token=") + 6:url.find("&user=")]
    user_command = url[url.find("user="):]

    message = "&command3=UnlockAllSafes"

    h = md5(state=token.decode("hex"), count=512)
    h.update(message)

    new_token = h.hexdigest()
    url = url.replace("token=" + token, "token=" + new_token)

    url = url + quote(padding((8 + len(user_command))*8)) + message

    parsedUrl = urlparse.urlparse(url)
    conn = httplib.HTTPSConnection(parsedUrl.hostname, parsedUrl.port)
    conn.request("GET", parsedUrl.path + "?" + parsedUrl.query)
    print conn.getresponse().read()

if __name__ == "__main__":
    main()