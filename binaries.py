text = "This should be easier"

def string_to_binary_line(text):
    orded = [ord(c) for c in text]
    bins = [bin(c) for c in orded]
    cut = [c[2:] for c in bins]
    fixes = [("0"*(8-len(g)) + g) for g in cut]
    returner = ""
    for r in fixes:
        returner += r
    return returner

def binary_line_to_string(digits):
    chunks = []
    chars = ""
    digits += "0"* (8 - (len(digits) % 8))
    for i in range(0,len(digits),8):
        chunks.append(chr(int(digits[i:i+8],2)))
    for g in chunks:
        chars += g
    return(chars)

a = string_to_binary_line("This should be easier")
print(binary_line_to_string(a))
