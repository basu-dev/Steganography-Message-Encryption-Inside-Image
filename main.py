from PIL import Image
import binascii 
import optparse


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
    message=binascii.unhexlify('%x' % {int('0b' +binary, 2)})
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

def hide(filename,message):
    img =Image.open(filename)
    binary=str2bin(message) + '111111111111110'
    if img.mode in ('RGBA'):
        img=img.convert('RGBA')
        datas=img.getdata()
        newData=[]
        digit = 0
        for item in datas:
            if (digit < len(binary)):
                newpix = encode(rgb2hex(item[0],item[1],item[2]),binary[digit])
                if newpix == None:
                    newData.append(item)
                else:
                    r , g, b=hex2rgb(newpix)
                    newData.append((r,g,b,255))
            else:
                newData.append(item)
        img.putdata(newData)
        img.save("abc.png",'PNG')
        return "Completed"
    else:
        return "Incorrect Image Mode Detected"
    
hide("basua.png","This is first message ")