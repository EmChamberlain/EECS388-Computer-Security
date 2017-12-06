#!/usr/bin/python
import subprocess
import os
import base64
import sys
import random
import string
import base64
import json
"""
successTestCases = []

for x in range(100):
    dict = {}
    length = random.randrange(2,1000)
    for y in range(length):
        key = ''.join(random.choice(string.printable) for _ in range(length) )    
        val = ''.join(random.choice(string.printable) for _ in range(length) )
        dict[key] = val
    successTestCases.append(json.dumps(dict, separators=('',':')))

length = 10000
a = ''.join(random.choice(string.printable) for _ in range(length) )
b = ''.join(random.choice(string.printable) for _ in range(length) )
c = ''.join(random.choice(string.printable) for _ in range(length) )
tr = ''.join(random.choice(string.printable) for _ in range(length) )
fa = ''.join(random.choice(string.printable) for _ in range(length) )
nu = ''.join(random.choice(string.printable) for _ in range(length) )

successTestCases.append("{" + "\"" + a + "\":" + tr + ",\"" + b + "\":" + fa + ",\"" + c + "\":" + nu + "}")


dict = {}
dict[sys.maxint**5] = sys.maxint ** 6
dict[sys.float_info.max] = sys.float_info.max
dict[sys.float_info.min] = sys.float_info.min
dict[float("inf")] = float("inf")

strin = "{"

for x in xrange(1000):
    strin += "\"a\":" + str(x) + ","
strin = strin[:-1]
strin += "}"

#str = ''.join(os.urandom(10) for _ in xrange(1000))
#successTestCases.append("{" + str + "}")
successTestCases.append(strin)
#successTestCases.append(json.dumps(dict, separators=('',':')))

dict = {}
length = 1000
a = ''.join(random.choice(string.ascii_letters) for _ in range(length) )
b = ''.join(random.choice(string.ascii_letters) for _ in range(length) )
c = ''.join(random.choice(string.ascii_letters) for _ in range(length) )
d = ''.join(random.choice(string.ascii_letters) for _ in range(length) )
e = ''.join(random.choice(string.ascii_letters) for _ in range(length) )
f = ''.join(random.choice(string.ascii_letters) for _ in range(length) )

dict[a] = b
dict[b] = c
dict[c] = d
dict[d] = e
dict[e] = f
dict[f] = a


dict = {}
dict[5] = sys.maxint**20
dict[sys.maxint**20] = 8
successTestCases.append(json.dumps(dict, separators=('',':')))

for x in range(100):
    dict = {}
    for y in range(random.randrange(0,100)):
        key = random.randrange(2,100000000)
        val = random.randrange(2,100000000)
        dict[key] = val
        successTestCases.append(json.dumps(dict, separators=('',':')))



dict = {}

for x in xrange(100):
    dict[x] = [{"a":[{"a":[{"a":[{"a":[{"a":"b"}]}]}]}]}]

successTestCases.append(json.dumps(dict, separators=('',':')))
    

for x in range(10):
    dict = {}
    
    dict[4611686012420609] = sys.maxint ** 3
    successTestCases.append(json.dumps(dict, separators=('',':')))


#list = []
#dict = {}
for x in xrange(100):
    rand = ''.join(os.urandom(1) for _ in xrange(10))
    successTestCases.append(rand)
#dict["rand bytes"] = list
#successTestCases.append(json.dumps(dict, separators=('',':')))
    


list = []
dict = {}
for x in xrange(1000):
    rand = ''.join(random.choice(string.printable[:-5]) for _ in xrange(25))
    list.append(rand)
dict["rand bytes"] = list
successTestCases.append(json.dumps(dict, separators=('',':')))
    


dict = {}
prev_dict = dict
for x in xrange(100):
    new_dict = {}
    prev_dict[x] = new_dict
    prev_dict = prev_dict[x]
prev_dict["a"] = "apple"

successTestCases.append(json.dumps(dict, separators=('',':')))


st = ""
length = 10
for x in xrange(length):
    st+= '''{"''' + str(0xFFFFFFFFFFFFFFFF) + '''":'''
st += '''{"a":"apple"}'''
for x in xrange(length):
    st += "}"

overall = "{"
for x in xrange(1000):
    overall += "\"" + str(x) + "\":" + st
overall += "}"
successTestCases.append(overall)


dict = {}
for x in xrange(1000):
    dict[str(sys.maxint + x)*100] = sys.maxint*x
successTestCases.append(json.dumps(dict, separators=('',':')))

testcases = []
i = 1000000
temp = '''{"list":''' + '['*i + '''"apple"''' + ']'*i + "]"
testcases.append(temp)
print temp

for testcase in successTestCases :
    child = subprocess.Popen("./jsonParser", stdin=subprocess.PIPE, stderr=subprocess.PIPE)
    _, stdErrOut = child.communicate(input = testcase)
    #print testcase
    if child.returncode == -11:# != 0 or stdErrOut != "":
        print "BROKEN SUCCESS TEST CASE (%d): %s" % (child.returncode, "testcase")
        print "|%s|" % stdErrOut
        print
        print
        #print base64.b64encode(testcase)
        sys.exit(0)
"""
testcases = []
 
i=1000000
temp ='''{"list":''' +  '['*i + '''"apple"''' + ']'*i + "}"
testcases.append(temp)
#print temp
 
for testcase in testcases:
 
    child = subprocess.Popen("./jsonParser", stdin=subprocess.PIPE, stderr=subprocess.PIPE)
    _, stdErrOut = child.communicate(input = testcase)
    #print child.returncode
    if child.returncode != 0 or stdErrOut != "":
        #print "BROKEN FAILURE TEST CASE (%d): %s" % (child.returncode, testcase)
        #print "|%s|" % stdErrOut
        #print child.returncode
        #f = open('tmp', 'w+')
        #f.write(base64.b64encode(testcase))
        #f.close()
        print base64.b64encode(testcase)
        sys.exit(0)
 
print "EVERYTHING PASSES"
        








print "EVERYTHING PASSES"
