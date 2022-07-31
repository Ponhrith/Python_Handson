import openpyxl as xl

workbook = xl.load_workbook("students-result.xlsx")
sheet = workbook["Sheet1"]
print(sheet.cell(4, 4).value)
