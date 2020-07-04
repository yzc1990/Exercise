from PIL import ImageGrab, Image
from win32com.client import Dispatch, DispatchEx
import pythoncom, os, itertools, time

file = 'C:\\Users\\Administrator\\Desktop\\2020年7月份一号项目生产数据每小时汇报.xlsx'
file_name = os.path.abspath(file)  # 把相对路径转成绝对路径
pythoncom.CoInitialize()  # 开启多线程
# 创建Excel对象
excel = DispatchEx('excel.application')
excel.visible = False  # 不显示Excel
excel.DisplayAlerts = 0  # 关闭系统警告(保存时不会弹出窗口)
# excel.ScreenUpdating = 1    # 关闭屏幕刷新

workbook = excel.workbooks.Open(file_name)  # 打开Excel文件
sheet = workbook.worksheets['氯化系统（7号炉）']
img_name = '1氯化系统（7号炉）'
# screen_area = sheet.used_range # 有内容的区域
# creen_area.CopyPicture()  # 复制图片区域
# 设置复制的区域
sheet.Range('A1:Q109').CopyPicture()
sheet.Paste()  # 粘贴
excel.Selection.ShapeRange.Name = img_name  # 将刚刚选择的Shape重命名，避免与已有图片混淆
sheet.Shapes(img_name).Copy()  # 选择图片
img = ImageGrab.grabclipboard()  # 获取剪贴板的图片数据
# time.sleep(2)
print(img)  # 可以弄个报错
img.save("C:\\Users\\Administrator\\Desktop\\Report\\" + img_name + ".PNG")
workbook.Close(False)  # 关闭Excel文件，不保存
excel.Quit()  # 退出Excel
pythoncom.CoUninitialize()  # 关闭多线程


