import openpyxl
from openpyxl import workbook

wb = openpyxl.Workbook()
hoja = wb.active
hoja.title = "Prueba"
a1 = hoja.cell(row=1, column=1, value="Informacion")
wb.save("C:\\Users\\Hanami\\Desktop\\excel_de_prueba.xlsx")