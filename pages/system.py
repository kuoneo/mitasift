import streamlit as st
import pandas as pd

st.title("システム仕様書ver1.1")
st.header("1. システム概要")
st.write("本システムは、PythonのStreamlitを使用して開発されたウェブアプリケーションであり、アルバイトのシフト作成を容易にすることを目的としています。主な機能として、ログインと予定入力が一緒になったページと、管理者画面の2つのページから構成されています。")
st.write("ログイン名とパスワードは以下の通りである")
# データを辞書型で定義
data = {
    "admin": "admin", "tanaka": "tana", "satou": "sato", "mitani": "mita",
    "suzuki": "suzu", "yamada": "yama", "takahashi": "taka", "watanabe": "wata",
    "ito": "ito", "nakamura": "naka", "kobayashi": "koba", "kato": "kato",
    "yoshida": "yoshi", "ishikawa": "ishi", "sasaki": "sasa", "kawamoto": "kawa",
    "kimura": "kimu", "fujiwara": "fuji", "hayashi": "haya", "matsumoto": "matsu",
    "inoue": "inou", "okamoto": "oka", "saito": "sait", "nishimura": "nishi",
    "endo": "endo", "morita": "mori", "yamaguchi": "yama", "shimizu": "shim",
    "kondo": "kond", "takeda": "take", "ueda": "ueda", "noguchi": "nogu",
    "mori": "mori", "taniguchi": "tani", "abe": "abe", "sakamoto": "saka",
    "nagai": "naga", "miyamoto": "miya", "fujita": "fuji", "okada": "oka"
}

# データをPandasのDataFrameに変換
df = pd.DataFrame(list(data.items()), columns=['name', 'pass'])

# Streamlitで表を表示
st.write(df)

st.header("2. 機能要件")
st.subheader("2.1 ログインと予定入力ページ")
st.write("・ログインフォームを備え、ログインしたユーザーの名前を表示する機能が存在します。")
st.write("・ユーザーが入力した予定が表形式で確認できるようになっています。")
st.write("・一週間分の予定をそれぞれ入力できるようになっており、予定はOK、NG、△の三種類で表現されます。")
st.write("・△の場合、開始時刻と終了時刻を選択できるセレクトボックスが用意されています。")
st.write("・全ての選択肢を選択した後、選択したステータスと時間が表示される機能が備わっています。")
st.write("・保存ボタンを押すと、入力された予定がJSONファイルに保存される仕組みがあります")
st.write("・管理者権限でログインした場合、管理者ページへ移動できるボタンが表示されます。")
st.subheader("2.2 管理者画面")
st.write("・管理者画面には各人の入力した予定が表形式で表示されます。")
st.write("・OKとNGの場合はそのまま表示され、△の場合には開始時刻から終了時刻が表示されます")
st.write("・OKの場合、背景色が青色に、△の場合、背景色が黄色になるような視覚的な表現がされています。")
st.write("・シフトの未提出者を一覧で表示させるボタンがあり、２回押すと消せます"
st.write("・各曜日の必要な人員を選択できるようになってます"
st.subheader("2.3 実装予定")
st.write("・各人員ごとに優先度を設定できるようにする予定です。")
st.write("・選択した人員数を満たす配置を自動で制作できる機能が実装予定です。")
st.write("・決定したシフト表を印刷できる画像ファイル等にアウトプットできる機能が実装予定です。")
st.header("3. システム開発")
st.subheader(3.1 アップデート情報)
st.write("0619:ver1.1 シフトの未提出者と各曜日の必要人員を選択できる機能を追加)
st.subheader(3.2 開発環境)
st.write("システム開発期間：3日")
st.write("システム開発者：三谷光")
st.write("システムテスト協力：WEBプログラミング科のみなさま")
st.write("連絡先：hikarumitani3@gmail.com")








