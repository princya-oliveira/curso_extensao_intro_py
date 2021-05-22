#script file: listaVendas.pow

import openpyxl

name = input('Enter file name: ')

wb = openpyxl.load_workbook(name)
wb_sheet = wb['Sheet1']

wb_row = []
for i, row_cells in enumerate(wb_sheet.iter_rows()):
  if i == 0:
    continue
  for cell in row_cells:
    wb_row.append(cell.value)

  print(wb_row)
  wb_row.clear()

print('------{:d}'.format(i))

#desafio: produto que vendeu mais(com valor total de venda do período) e produto de maior giro com valor total vendido. 

#criar dicionários 
lojas = dict()
produtos = dict()

