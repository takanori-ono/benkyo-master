from openpyxl import Workbook

# 新しいワークブックを作成
wb = Workbook()

# デフォルトのアクティブなワークシートを取得
ws = wb.active

# セルに値を設定
ws['A1'] = 'Hello'
ws['B1'] = 'World!'

# Excelファイルを保存
wb.save('example.xlsx')
