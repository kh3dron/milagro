from PIL import Image

def read_lsb(filename):
    im = Image.open(filename)
    width, length = im.size

    #Extract the least significan bit from each coordinate
    bits = ""
    for x in range(0, width):
        for y  in range(0, length):
            for r in range(0, 3):
                bits += str(im.getpixel((x, y))[r] & 1)

    #add zeroes to pad to 8s
    bits += "0"*(8 - (len(bits)%8))

    #extract characters from binary
    returnInts = ""
    for i in range(0,len(bits),8):
        returnInts += (chr(int(bits[i:i+8],2)))

    return(returnInts)

def write_lsb(message, readFrom, writeTo):
    im = Image.open(readFrom)
    #Format characters
    bits = ""
    for g in message:
        term = "0"*(8-len(str(bin(ord(g)))[2:])) + (str(bin(ord(g))))[2:]
        bits += term

    #Pad with 3 zeroes
    bits += "0"*(3 - (len(bits)%3))

    width, length = im.size
    available_bits = width*length*3

    if (len(bits) > available_bits):
        print("Error: Ciphertext too large for this image.")

    tick = 0
    for x in range(0, width):
        for y in range(0, length):
            colors = (im.getpixel((x, y)))

            r = colors[0]
            g = colors[1]
            b = colors[2]
            #This isn't perfect, but couldn't make the bitwise thing work today
            if (colors[0] % 2 != int(bits[tick])): r += 1
            if (colors[1] % 2 != int(bits[tick+1])): g += 1
            if (colors[2] % 2 != int(bits[tick+2])): b += 1

            im.putpixel((x, y), (r, g, b))
            tick += 3
            if tick >= len(bits):
                break
        if tick >= len(bits):
            break
    im.save(writeTo)
    return

text = "Test this out, why don't ya"
var1 = read_lsb('pic.jpg')
write_lsb(text, 'pic.jpg', 'encoded.png')
var2 = read_lsb('encoded.jpg')
