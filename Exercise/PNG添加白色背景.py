from PIL import Image


def alphabg2white_PIL(img):
    img = img.convert('RGBA')
    sp = img.size
    width = sp[0]
    height = sp[1]
    print(sp)
    for yh in range(height):
        for xw in range(width):
            dot = (xw, yh)
            color_d = img.getpixel(dot)
            if (color_d[3] == 0):
                color_d = (255, 255, 255, 255)
                img.putpixel(dot, color_d)
    #img.show()
    return img


if __name__ == '__main__':
    img = Image.open('C:\\Users\\Administrator\\Desktop\\Report\\1氯化系统（7号炉）.PNG')
    whiteback = alphabg2white_PIL(img)
    whiteback.save('C:\\Users\\Administrator\\Desktop\\Report\\1氯化系统（7号炉）.PNG')
    #whiteback.show()

    img = Image.open('C:\\Users\\Administrator\\Desktop\\Report\\2冷凝吸收.PNG')
    whiteback = alphabg2white_PIL(img)
    whiteback.save('C:\\Users\\Administrator\\Desktop\\Report\\2冷凝吸收.PNG')
    # whiteback.show()

    img = Image.open('C:\\Users\\Administrator\\Desktop\\Report\\3尾气处理.PNG')
    whiteback = alphabg2white_PIL(img)
    whiteback.save('C:\\Users\\Administrator\\Desktop\\Report\\3尾气处理.PNG')
    # whiteback.show()

    img = Image.open('C:\\Users\\Administrator\\Desktop\\Report\\4精制系统.PNG')
    whiteback = alphabg2white_PIL(img)
    whiteback.save('C:\\Users\\Administrator\\Desktop\\Report\\4精制系统.PNG')
    # whiteback.show()

    img = Image.open('C:\\Users\\Administrator\\Desktop\\Report\\5公辅系统.PNG')
    whiteback = alphabg2white_PIL(img)
    whiteback.save('C:\\Users\\Administrator\\Desktop\\Report\\5公辅系统.PNG')
    # whiteback.show()

# 同样的haveAlpha.png改成自己需要处理的透明背景图片