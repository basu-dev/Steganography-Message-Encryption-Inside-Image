from PIL import Image
from utilities import *
import optparse




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
            digit+=1
        img.putdata(newData)
        img.save("abc.png",'PNG')
        return "Completed"
    else:
        return "Incorrect Image Mode Detected"

def retr(filename):
    img = Image.open(filename)
    binary=''
    if img.mode in ('RGBA'):
        img = img.convert('RGBA')
        datas=img.getdata()

        for item in datas:
            digit= decode(rgb2hex(item[0],item[1],item[2]))
            if digit== None:
                pass
            else:
                binary=binary + str(digit)
                if (binary[-16:] == '111111111111110'):
                    print("Success")
                    return bin2str(binary[:-16])
        return bin2str(binary)
    return "Incorrect Image Mode"

def Main():
    parser= optparse.OptionParser('usage %prog '+\
        '-e/-d <target file> ')
    parser.add_option('-e',dest='hide',type='string', \
        help='target pictgure path to hide')
    parser.add_option('-d',dest='retr',type='string', \
        help='target pciture to retrieve')
    (options, args) = parser.parse_args()
    if (options.hide !=None):
        text= input("Enter message to hide : ")
        print(hide(options.hide,text))
    elif (options.retr !=None):
        print(retr(options.retr))
    else:
        print( parser.usage)
        exit(0)

if __name__ =='__main__':
    Main()

    
# hide("basua.png","This is first message ")

