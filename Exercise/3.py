import xlwings as xw
from PIL import ImageGrab

app = xw.App(visible=True, add_book=False)  # 使用xlwings的app启动
wb = app.books.open('C:\\Users\\Administrator\\Desktop\\2020年7月份一号项目生产数据每小时汇报.xlsx')  # 打开文件
sheet = wb.sheets['氯化系统（7号炉）']  # 选定sheet
all = sheet.range('A1:Q109')  # 获取有内容的range
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
all = sheet.range('A1:Q109')  # 获取有内容的range
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
all = sheet.range('A1:H109')  # 获取有内容的range
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
all = sheet.range('A1:T109')  # 获取有内容的range
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
all = sheet.range('A1:O110')  # 获取有内容的range
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

