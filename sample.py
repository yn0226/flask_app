#必要なモジュールのインポート
from flask import Flask

#Flask　インスタンス化
app = Flask(__name__)

#ルートディレクトリにアクセスがあったときの処理
@app.route('/')
def hello():
    return 'Hello World!'

#エントリーポイントの設定
if __name__ == '__main__':
    app.run()

