import binascii 

def rgb2hex(r,g,b):
    return '#{:02x}{:02x}{:02x}'.format(r,g,b)

def hex2rgb(hexcode):
    h=hexcode.lstrip('#')
    return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))

def str2bin(message):
    binary= bin(int(binascii.hexlify(str.encode(message)),16))
    print(binary)
    return binary[2:]


def bin2str(binary):
    # message=binascii.unhexlify('%x' % (int('0b' +binary, 2)))
    # message=binascii.unhexlify('%x' % 45)
    # print(binary)
    message=int('0b'+binary,2)
    message=binascii.unhexlify('%x' % message)
    return message

def encode(hexcode,digit):
    if hexcode[-1] in ('0','1','2','3','4','5'):
        hexcode=hexcode[:-1]
        return hexcode

    else:
        return None

def decode(hexcode):
    if hexcode[-1] in ('0','1'):
        return hexcode[-1]
    else:
        return None