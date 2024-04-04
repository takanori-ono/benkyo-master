import json

# JSON文字列を読み込む
with open('conversations.json', 'r', encoding='utf-8') as file:
    json_data = file.read()

# UnicodeエスケープシーケンスをPythonの文字列に変換する
decoded_data = json.loads(json_data)

# 変換されたデータを使って何かをする（例えば、表示する）
#print(decoded_data)

formatted_json = json.dumps(decoded_data, indent=2, ensure_ascii=False)
print(formatted_json)
