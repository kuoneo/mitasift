

import streamlit as st
from datetime import time
import json  # JSONを扱うためにインポートします

# JSONファイルからスケジュールを読み込む関数
def load_schedule_from_json(username, filename="schedule.json"):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)
        return data.get(username, {})
    except FileNotFoundError:
        return {}

# スケジュールを表形式で表示する関数
def display_schedule(schedule):
    if schedule:
        st.write("この予定で保存されています")
        st.table(schedule)
    else:
        st.write("保存された予定はありません。")

# ユーザー認証情報
keylist = {"admin": "admin", "tanaka": "tana", "satou": "sato", "mitani": "mita","suzuki":"suzu","yamada":"yama","takahashi":"taka","watanabe":"wata","ito":"ito","nakamura":"naka","kobayashi":"koba","kato":"kato","yoshida":"yoshi","ishikawa":"ishi","sasaki":"sasa","kawamoto":"kawa","kimura":"kimu","fujiwara":"fuji","hayashi":"haya","matsumoto":"matsu","inoue":"inou","okamoto":"oka","saito":"sait","nishimura":"nishi","endo":"endo","morita":"mori","yamaguchi":"yama","shimizu":"shim","kondo":"kond","takeda":"take","ueda":"ueda","noguchi":"nogu","mori":"mori","taniguchi":"tani","abe":"abe","sakamoto":"saka","nagai":"naga","miyamoto":"miya","fujita":"fuji","okada":"oka"}

# タイトル
st.title("シフト作成")

# セッションステートの初期化
if 'log' not in st.session_state:
    st.session_state.log = False
if 'name' not in st.session_state:
    st.session_state.name = None

# ログインフォーム
with st.form(key="login"):
    name = st.text_input("名前")
    pas = st.text_input("パスワード", type="password")
    submit = st.form_submit_button("認証")

    if submit:
        if name not in keylist:
            st.text("error:その名前は存在しません")
        elif keylist[name] != pas:
            st.text("認証に失敗しました")
        else:
            st.session_state.name = name
            st.session_state.log = True
            st.text(f"{name}さんでログインしました")
            
                
                

# ログイン成功後の予定入力フォーム
if st.session_state.log:
    if name=="admin":
        if st.button("管理画面に移動"):
            st.switch_page("pages/admin.py")
    schedule = load_schedule_from_json(name)
    display_schedule(schedule)
    st.text(f"{st.session_state.name}さん、来週の予定を入力してください")

    days_of_week = ["月曜日", "火曜日", "水曜日", "木曜日", "金曜日", "土曜日", "日曜日"]
    responses = {}
    
    for day in days_of_week:
        st.markdown(f"### {day}")
        status = st.selectbox(f"{day}の状態を選択", ["OK", "NG", "△"], key=f"status_{day}")
        if status == "△":
            start_time = st.time_input(f"{day}の開始時間",time(17,0), key=f"start_{day}")
            end_time = st.time_input(f"{day}の終了時間",time(23,0), key=f"end_{day}")
            responses[day] = {"status": status, "start_time": start_time.strftime("%H:%M"), "end_time": end_time.strftime("%H:%M")}
        elif status=="OK":
            responses[day] = {"status": status, "start_time": "17:00", "end_time": "23:00"}
        else:
            responses[day] = {"status": status, "start_time": "x", "end_time": "x"}

    st.write("選択されたステータスと時間:")
    for day, details in responses.items():
        if details["status"] == "△":
            st.write(f"{day}: {details['status']}, {details['start_time']}から{details['end_time']}まで許可")
        
        else:
            st.write(f"{day}: {details['status']}")

    # スケジュールをJSONファイルに保存する関数
    def save_schedule_to_json(username, responses, filename="schedule.json"):
        data = {}
        try:
            with open(filename, "r", encoding="utf-8") as f:
                data = json.load(f)
        except FileNotFoundError:
            pass
        data[username] = responses
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    # 保存ボタン
    st.write("↓二回押してね")
    if st.button("保存"):
        save_schedule_to_json(st.session_state.name, responses)
        st.success("スケジュールを保存しました")
