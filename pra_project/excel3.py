import xlrd
rb = xlrd.open_workbook("c:\\Users\\prabeena.panda\\sourcee.xlsx")
rb1 = xlrd.open_workbook("c:\\Users\\prabeena.panda\\targett.xlsx")
sheet = rb.sheet_by_index(0)
sh = rb1.sheet_by_index(0)


for i in range(sheet.nrows):
    for j in range(sheet.ncols):
         row = sheet.row_values(i)
         col = sheet.row_values(j)
         for k in range(sh.nrows):
             for l in range(sh.cols):
                 row = sheet.row_values(k)
                 col = sheet.row_values(l)
         for c_el in row and col:
                print(c_el)

for i in range(1, sr+1 ):
    for j in range(1, sc+1 ):
        c = ws1.cell(row=i+1, column=j)
        cc=ws1.cell(row=1, column=j)
        for k in range(1, tr+1 ):
               for l in range(1, tc+1 ):
                    d = ws2.cell(row=k+2, column=l)
                    dd=ws2.cell(row=2, column=l)
                    if cc == dd:
                          d.value =  c.value
