import os
path = r'F:\BaiduNetdiskDownload'#引号内为路径
filenames = os.listdir(path)
for filename in filenames:
    print(filename)

