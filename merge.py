from PIL import Image
import sys

infirst = Image.open(sys.argv[1])
insecond = Image.open(sys.argv[2])

output = Image.new('1', infirst.size)

for x in range(infirst.size[0]):
    for y in range(infirst.size[1]):
        output.putpixel((x, y), min(infirst.getpixel((x, y)), insecond.getpixel((x, y))))

output.save("merge.png")