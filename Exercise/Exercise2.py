def write_file():
    book = xlwt.Workbook(encoding='utf-8') #创建Workbook，相当于创建Excel

    # 创建sheet，Sheet1为表的名字，cell_overwrite_ok为是否覆盖单元格
    sheet1 = book.add_sheet(u'Sheet1', cell_overwrite_ok=True)

    #向表中添加数据
    sheet1.write(0, 0, 'Englishname')  #第0行第0列
    sheet1.write(1, 0, 'Hellen')  #第一行第0列
    sheet1.write(0, 1, '中文名字')
    sheet1.write(1, 1, '海伦')
