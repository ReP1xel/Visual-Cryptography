from PIL import Image
import sys

original = Image.open(sys.argv[1])
original = original.convert("1")

merge = Image.open(sys.argv[2])
unmerge = Image.new('1', original.size)

o_pixels = original.load()
m_pixels = merge.load()
u_pixels = unmerge.load()

# reverse decrypt merge image
for i in range(unmerge.size[0]):
    for j in range(unmerge.size[1]):
        if m_pixels[i*2,j*2] == 0 and m_pixels[i*2,j*2+1] == 0 and \
        m_pixels[i*2+1,j*2] == 0 and m_pixels[i*2+1,j*2+1] == 0:
            u_pixels[i,j] = 0
        else:
            u_pixels[i,j] = 255 # to match with original pixel format

#verify, comparison
total = unmerge.size[0]*unmerge.size[1]
count = 0
for i in range(unmerge.size[0]):
    for j in range(unmerge.size[1]):
        if o_pixels[i,j] == u_pixels[i,j]:
            count += 1

print(total)
print(count)
print('Accuracy: ', count*100/total)

unmerge.save(sys.argv[1].split('.')[0] + "_unmerge.png")