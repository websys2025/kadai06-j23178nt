import requests
import pandas as pd

# 【取得するデータの説明】
# 統計データID: 0004019020
# データ内容: 在留外国人統計（旧登録外国人統計）
# 国籍・地域別、在留資格別の在留外国人数のデータ
# 提供元: 法務省
# エンドポイント: http://api.e-stat.go.jp/rest/3.0/app/json/getStatsData
# 機能: 指定した統計データIDに基づいて、JSON形式で統計データを取得し、
# 在留資格や国籍の分類ごとの人数を取得して表示する。

APP_ID = "c472b4b5fc14c89a63fe410bb7a7e01b97975964"
API_URL = "http://api.e-stat.go.jp/rest/3.0/app/json/getStatsData"

params = {
    "appId": APP_ID,
    "statsDataId": "0004019020",
    "lang": "J"  # 日本語データを取得
}

response = requests.get(API_URL, params=params)
data = response.json()

# 統計データの値の部分を取得
values = data['GET_STATS_DATA']['STATISTICAL_DATA']['DATA_INF']['VALUE']

# DataFrame化
df = pd.DataFrame(values)

# メタ情報（分類情報）を取得し、IDを名称に変換するための準備
meta_info = data['GET_STATS_DATA']['STATISTICAL_DATA']['CLASS_INF']['CLASS_OBJ']

# 各分類IDを意味のある名称に置換する
for class_obj in meta_info:
    column_name = '@' + class_obj['@id']

    id_to_name_dict = {}
    if isinstance(class_obj['CLASS'], list):
        for obj in class_obj['CLASS']:
            id_to_name_dict[obj['@code']] = obj['@name']
    else:
        id_to_name_dict[class_obj['CLASS']['@code']] = class_obj['CLASS']['@name']

    df[column_name] = df[column_name].replace(id_to_name_dict)

# 列名の日本語化
col_replace_dict = {'@unit': '単位', '$': '値'}
for class_obj in meta_info:
    org_col = '@' + class_obj['@id']
    new_col = class_obj['@name']
    col_replace_dict[org_col] = new_col

df.columns = [col_replace_dict.get(col, col) for col in df.columns]

# 表示（上位20件だけ表示）
print(df.head(20))
