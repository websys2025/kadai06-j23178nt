import requests

# ---------------------------------------------------------
# オープンデータ名: Frankfurter.app API
# 概要: 無料で使える為替レートAPI。ヨーロッパ中央銀行のデータ使用。
# エンドポイント: https://api.frankfurter.app/latest
# 機能: 指定した通貨の最新為替レートを取得（JSON形式）
# 使い方:
#   - "from": 基準通貨（例: JPY）
#   - "to": 対象通貨（例: USD,EUR）
#   - APIキー不要で誰でも使用可能。
# ---------------------------------------------------------

url = "https://api.frankfurter.app/latest"
params = {
    "from": "JPY",
    "to": "USD,EUR"
}

response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()

    print("=== 日本円(JPY)に対する為替レート ===")
    for currency, rate in data["rates"].items():
        print(f"1 JPY = {rate:.4f} {currency}")
else:
    print("為替レートの取得に失敗しました。ステータスコード:", response.status_code)
