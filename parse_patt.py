
abr = open("46383d7a-cc22-11dd-a850-c6af221b7b0b", "rb")

MODE = 1


# Index color table is only present when image mode is 'indexed color'
if MODE == 2:
    COLOR_TABLE = abr.read(256 * 3) 
    # print(COLOR_TABLE)

    print("UNKNOWN DATA!!!:", abr.read(4))

print("Virtual Memory Array (VMA) Version:",
        int.from_bytes(abr.read(4), byteorder='big'), "(Expecting 3)")

VMA_TOTAL_LEN = int.from_bytes(abr.read(4), byteorder='big')
print("VMA Length:", VMA_TOTAL_LEN)

RECTANGLE = {
    "top": int.from_bytes(abr.read(4), byteorder='big'),
    "left": int.from_bytes(abr.read(4), byteorder='big'),
    "bottom": int.from_bytes(abr.read(4), byteorder='big'),
    "right": int.from_bytes(abr.read(4), byteorder='big')
}

print("VMA Full Rectangle:", RECTANGLE)

NUM_CHANNELS = int.from_bytes(abr.read(4), byteorder='big')
print("VMA Number of Channels:", NUM_CHANNELS)

# number of channels + one for a user mask + one for a sheet mask
for i in range(NUM_CHANNELS + 2):
    # is array written
    if abr.read(4) != b'\x00\x00\x00\x00':
        VMA_LEN = int.from_bytes(abr.read(4), byteorder='big')
        print(VMA_LEN)
        if VMA_LEN != 0:
            print("\tVMA Pixel Depth:", int.from_bytes(
                abr.read(4), byteorder='big'))

            RECTANGLE = {
                "top": int.from_bytes(abr.read(4), byteorder='big'),
                "left": int.from_bytes(abr.read(4), byteorder='big'),
                "bottom": int.from_bytes(abr.read(4), byteorder='big'),
                "right": int.from_bytes(abr.read(4), byteorder='big')
            }

            print("\tVMA Rectangle:", RECTANGLE)

            print("\tVMA Pixel Depth:", int.from_bytes(
                abr.read(2), byteorder='big'))

            print("\tVMA Compression Mode (1 is zip):", int.from_bytes(abr.read(1), byteorder='big'))

            abr.read(VMA_LEN - 23)

