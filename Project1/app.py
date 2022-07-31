import openpyxl as xl

workbook = xl.load_workbook("students-result.xlsx")
sheet = workbook["Sheet1"]

for row in range(2, sheet.max_row + 1):
    physics = sheet.cell(row, 3).value
    maths = sheet.cell(row, 4).value
    history = sheet.cell(row, 5).value
    geography = sheet.cell(row, 6).value
    biology = sheet.cell(row, 7).value
    chemistry = sheet.cell(row, 8).value
    print(physics, maths, history, geography, biology, chemistry)

