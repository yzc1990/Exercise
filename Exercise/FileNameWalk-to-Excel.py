import os
import xlwt  # 操作excel模块
import sys
#不同文件夹需要更改feile_path中的路径和f.save中的路径及Excel文件名
file_path = r'F:\BaiduNetdiskDownload'  # 要获取当前路径，filenamelist为要写入的文件
f = xlwt.Workbook(encoding='utf-8', style_compression=0)  # 新建一个excel
sheet = f.add_sheet('FileName')  # 新建一个sheet
pathDir = os.listdir(file_path)  # 文件放置在当前文件夹中，用来获取当前文件夹内所有文件目录

#设置格式，写入标题
sec_col=sheet.col(1)
sec_col.width=256*90   #width = 256 * 90    256为衡量单位，90表示90个字符宽度
i = 0  # 将文件列表写入test.xls
sheet.write(0, 0, '序号')  #第0行第0列
sheet.write(0, 1, '名称')  #第0行第1列

#写入数据
for s in pathDir:
    sheet.write(i+1,0,i+1)  #写入序号
    sheet.write(i+1, 1, s)  # 参数i,0,s分别代表行，列，写入值
    i = i + 1

print(file_path)
print(i)  # 显示文件名数量
f.save(r'F:\BaiduNetdiskDownload\Filename.xls') #保存文件
