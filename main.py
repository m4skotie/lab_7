from PIL import Image , ImageFilter

def z1():
    f = "papi4.png"
    image = Image.open(f)
    image.show("papi4.png")
    height, width = image.size
    f = image.format
    m = image.mode
    print("Ширина: " , width)
    print("Высота: " , height)
    print("Формат: " , f)
    print("Цветовая модель: " , m)

def z2():
    file = Image.open('papi4.png')
    file1 = file.reduce(3)
    file1.save('papi4_melkiy.png')
    file1.show('small_image.png')
    m1 = file.transpose(method=Image.FLIP_LEFT_RIGHT)
    m1.save('mirrored_h.png')
    m2 = file.transpose(method=Image.FLIP_TOP_BOTTOM)
    m2.save('mirrored_v.png')
    m1.show('horizontal_mirror.png')
    m2.show('vertical_mirror.png')

def z3():
    for i in range(1, 5+1):
        file = Image.open(str(i) + '.png')
        file = file.filter(ImageFilter.EDGE_ENHANCE_MORE)
        file.save('filtered_' + str(i) + '.png')
        file.show()

def z4():
    watermark = Image.open("watermark.png")
    file = Image.open("papi4.png")
    file.paste(watermark, (500,80), watermark)
    file.save('watermarked.png')
    file.show()
z4()