import xlwings as xw
from PIL import ImageGrab



app = xw.App(visible=True, add_book=False)  # 使用xlwings的app启动
wb = app.books.open('C:\\Users\\Administrator\\Desktop\\2020年7月份一号项目生产数据每小时汇报.xlsx')  # 打开文件
wb.visible=False
sheet = wb.sheets['氯化系统（7号炉）']  # 选定sheet
all = sheet.range('A1:Q141')  # 获取有内容的range
#print(all.value)
print("ok")
all.api.CopyPicture()  # 复制图片区域
sheet.api.Paste()  # 粘贴
img_name = '1氯化系统（7号炉）'
pic = sheet.pictures[0]  # 当前图片
pic.api.Copy()  # 复制图片
from PIL import ImageGrab
import PIL.Image as Image
img = ImageGrab.grabclipboard()  # 获取剪贴板的图片数据
img.save("C:\\Users\\Administrator\\Desktop\\Report\\" +  img_name + ".PNG")  # 保存图片
pic.delete()  # 删除sheet上的图片




#表2

sheet = wb.sheets['冷凝吸收']  # 选定sheet
all = sheet.range('A1:Q141')  # 获取有内容的range
#print(all.value)
print("ok")
all.api.CopyPicture()  # 复制图片区域
sheet.api.Paste()  # 粘贴
img_name = '2冷凝吸收'
pic = sheet.pictures[0]  # 当前图片
pic.api.Copy()  # 复制图片
from PIL import ImageGrab

img = ImageGrab.grabclipboard()  # 获取剪贴板的图片数据
img.save("C:\\Users\\Administrator\\Desktop\\Report\\" +  img_name + ".PNG")  # 保存图片
pic.delete()  # 删除sheet上的图片

#表3

sheet = wb.sheets['尾气处理']  # 选定sheet
all = sheet.range('A1:H141')  # 获取有内容的range
#print(all.value)
print("ok")
all.api.CopyPicture()  # 复制图片区域
sheet.api.Paste()  # 粘贴
img_name = '3尾气处理'
pic = sheet.pictures[0]  # 当前图片
pic.api.Copy()  # 复制图片
from PIL import ImageGrab

img = ImageGrab.grabclipboard()  # 获取剪贴板的图片数据
img.save("C:\\Users\\Administrator\\Desktop\\Report\\" +  img_name + ".PNG")  # 保存图片
pic.delete()  # 删除sheet上的图片

#表4

sheet = wb.sheets['精制系统']  # 选定sheet
all = sheet.range('A1:T141')  # 获取有内容的range
#print(all.value)
print("ok")
all.api.CopyPicture()  # 复制图片区域
sheet.api.Paste()  # 粘贴
img_name = '4精制系统'
pic = sheet.pictures[0]  # 当前图片
pic.api.Copy()  # 复制图片
from PIL import ImageGrab

img = ImageGrab.grabclipboard()  # 获取剪贴板的图片数据
img.save("C:\\Users\\Administrator\\Desktop\\Report\\" +  img_name + ".PNG")  # 保存图片
pic.delete()  # 删除sheet上的图片

#表5

sheet = wb.sheets['公辅系统']  # 选定sheet
all = sheet.range('A1:O142')  # 获取有内容的range
#print(all.value)
print("ok")
all.api.CopyPicture()  # 复制图片区域
sheet.api.Paste()  # 粘贴
img_name = '5公辅系统'
pic = sheet.pictures[0]  # 当前图片
pic.api.Copy()  # 复制图片
from PIL import ImageGrab

img = ImageGrab.grabclipboard()  # 获取剪贴板的图片数据
img.save("C:\\Users\\Administrator\\Desktop\\Report\\" +  img_name + ".PNG")  # 保存图片
pic.delete()  # 删除sheet上的图片

wb.close()  # 不保存，直接关闭
app.quit()  # 退出app



#添加白色背景
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

