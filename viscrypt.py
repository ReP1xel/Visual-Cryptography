import argparse
import random

from PIL import Image


def two_of_two(filename):
    original = Image.open(filename)
    
    original = original.convert("1")
    o_pixels = original.load()
    
    first = Image.new("1", (original.size[0]*2, original.size[1]*2))
    f_pixels = first.load()
    
    second = Image.new("1", (original.size[0]*2, original.size[1]*2))
    s_pixels = second.load()
    
    for i in range(original.size[0]):
        for j in range(original.size[1]):
            if o_pixels[i,j] == 0:
                if random.randint(0, 1):
                    f_pixels[i * 2,j * 2    ] = 1
                    f_pixels[i * 2,j * 2 + 1] = 0
                    s_pixels[i * 2,j * 2    ] = 0
                    s_pixels[i * 2,j * 2 + 1] = 1
                else:
                    f_pixels[i * 2,j * 2    ] = 0
                    f_pixels[i * 2,j * 2 + 1] = 1
                    s_pixels[i * 2,j * 2    ] = 1
                    s_pixels[i * 2,j * 2 + 1] = 0
            else:
                if random.randint(0, 1):
                    f_pixels[i * 2,j * 2    ] = 0
                    f_pixels[i * 2,j * 2 + 1] = 1
                    s_pixels[i * 2,j * 2    ] = 0
                    s_pixels[i * 2,j * 2 + 1] = 1
                else:
                    f_pixels[i * 2,j * 2    ] = 1
                    f_pixels[i * 2,j * 2 + 1] = 0
                    s_pixels[i * 2,j * 2    ] = 1
                    s_pixels[i * 2,j * 2 + 1] = 0
    
    first.save(filename.split('.')[0] + "_share1.png")
    second.save(filename.split('.')[0] + "_share2.png")
    

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("IMAGE", help="The image to encrypt")
    args = parser.parse_args()

    two_of_two(args.IMAGE)
