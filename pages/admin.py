import streamlit as st
import pandas as pd
import json

st.title("管理者用")


st.write("提出された予定")
# JSONファイルからデータを読み込む
with open('schedule.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# ステータスと時間を抜き出してDataFrameに変換
status_data = {}
for name, schedule in data.items():
    status_data[name] = {day: (details["status"], details["start_time"], details["end_time"]) for day, details in schedule.items()}
status_df = pd.DataFrame(status_data).T

# △の時だけ時間を表示
filtered_status_df = status_df.applymap(lambda x: f"{x[1]} - {x[2]}" if x[0] == "△" else x[0])

# 背景色を設定
def highlight_status(val):
    if val == "NG":
        return ""
    elif val == "OK":
        return "background-color: lightblue"
    else:
        return "background-color: yellow"

# 表形式で表示
st.dataframe(filtered_status_df.style.applymap(highlight_status))