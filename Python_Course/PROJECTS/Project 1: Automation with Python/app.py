import openpyxl as xl
from pathlib import Path

p = Path("")
for item in p.glob("*"):
    print(item)

#wb = xl.load_workbook('transactions.xlsx')
#sheet = wb['Sheet1']
#cell = sheet['a1']
#print(cell)
#print(wb.sheetnames())