

import streamlit as st
import pandas as pd
import json

names_list=['admin', 'tanaka', 'satou', 'mitani', 'suzuki', 'yamada', 'takahashi', 'watanabe', 'ito', 'nakamura', 'kobayashi', 'kato', 'yoshida', 'ishikawa', 'sasaki', 'kawamoto', 'kimura', 'fujiwara', 'hayashi', 'matsumoto', 'inoue', 'okamoto', 'saito', 'nishimura', 'endo', 'morita', 'yamaguchi', 'shimizu', 'kondo', 'takeda', 'ueda', 'noguchi', 'mori', 'taniguchi', 'abe', 'sakamoto', 'nagai', 'miyamoto', 'fujita', 'okada']
days_of_week = ["月曜日", "火曜日", "水曜日", "木曜日", "金曜日", "土曜日", "日曜日"]

st.title("管理者用")

st.write("提出された予定")

JSONファイルからデータを読み込む
with open('schedule.json', 'r', encoding='utf-8') as file:
data = json.load(file)

ステータスと時間を抜き出してDataFrameに変換
status_data = {}
for name, schedule in data.items():
status_data[name] = {day: (details["status"], details["start_time"], details["end_time"]) for day, details in schedule.items()}
status_df = pd.DataFrame(status_data).T #.Tで行列入れ替え

△の時だけ時間を表示
filtered_status_df = status_df.applymap(lambda x: f"{x[1]} - {x[2]}" if x[0] == "△" else x[0])

背景色を設定
def highlight_status(val):
if val == "NG":
return ""
elif val == "OK":
return "background-color: lightblue"
else:
return "background-color: yellow"

表形式で表示
st.dataframe(filtered_status_df.style.applymap(highlight_status))

#未提出者をボタンで表示させる
if 'missing' not in st.session_state:
st.session_state.missing = False

missing_names = list(set(names_list )- set(status_df.index) )

if st.button("未提出者の表示"):
st.session_state.missing=not st.session_state.missing
if st.session_state.missing:
if len(missing_names)==0:
st.write("未提出者はいません")
else:
st.write(missing_names)

col = st.columns(len(days_of_week))
needlist={}
#"OK" の数をカウントする
ok_count = filtered_status_df.apply(lambda x: x.value_counts().get('OK', 0), axis=0)

必要な人員数と比較する
for i, day in enumerate(days_of_week):
with col[i]:
need = st.selectbox(day, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], key=f"{day}_selectbox")
st.write( f"OK数: {ok_count[i]}")
st.write(ok_count[2])
