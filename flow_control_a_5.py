import py_compile

py_compile.compile("flow_control_a_5.py")
file = open('flow_control_a_5.pyc', 'rb')
count = 0

while 1:
    byte = file.read(1)
    if byte == "": break
    else:
        byte_str = '{0:08b}'.format(ord(byte))
        count += byte_str.count("1")
        print byte_str

file.close()
print "bity zapalone: " + str(count)

