from PIL import Image

"Takes in string, returns concatenated binary"
def string_to_binary_line(text):
    orded = [ord(c) for c in text]
    bins = [bin(c) for c in orded]
    cut = [c[2:] for c in bins]
    fixes = [("0"*(8-len(g)) + g) for g in cut]
    returner = ""
    for r in fixes:
        returner += r
    return returner

"Takes in contatenated binary, returns string"
def binary_line_to_string(digits):
    chunks = []
    chars = ""
    digits += "0"* (8 - (len(digits) % 8))
    for i in range(0,len(digits),8):
        chunks.append(chr(int(digits[i:i+8],2)))
    for g in chunks:
        chars += g
    return(chars)

def read_lsb(filename):
    im = Image.open(filename)
    width, length = im.size

    #Extract the least significan bit from each coordinate
    bits = ""
    for x in range(0, width):
        for y in range(0, length):
            for r in range(0, 3):
                bits += str(im.getpixel((x, y))[r] & 1)
    return(binary_line_to_string(bits))

def write_lsb(message, readFrom, writeTo):
    im = Image.open(readFrom)
    width, length = im.size


    bits = string_to_binary_line(message)
    available_bits = length*width*3

    bits += "0"*(3-(len(bits) % 3))

    if (len(bits) > available_bits):
        print("Error: Ciphertext too large for this image.")

    tick = 0
    for x in range(0, width):
        for y in range(0, length):
            r, g, b, z = (im.getpixel((x, y)))

            #This isn't perfect, but couldn't make the bitwise thing work today
            if (r % 2 != int(bits[tick])): r += 1
            if (g % 2 != int(bits[tick+1])): g += 1
            if (b % 2 != int(bits[tick+2])): b += 1

            im.putpixel((x, y), (r, g, b, z))
            tick += 3
            if tick >= len(bits):
                break
        if tick >= len(bits):
            break
    im.save(writeTo)
    return

text = "THIS IS A SECRET, PROTECT IT"
write_lsb(text, 'small.png', 'encoded.png')
var2 = read_lsb('encoded.png')

print(var2)
