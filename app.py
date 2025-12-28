import streamlit as st
import pandas as pd

# 1. 網頁配置：手機優先
st.set_page_config(page_title="2026年1月沖繩家族旅遊", page_icon="🐢", layout="wide")

# 2. 可愛旅遊風 CSS 樣式
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+TC:wght@400;700&display=swap');
    html, body, [class*="css"] { font-family: 'Noto Sans TC', sans-serif; }
    
    .stApp { background: #F0F7F9; }
    
    /* 卡片設計 */
    .trip-card {
        background-color: white;
        padding: 15px;
        border-radius: 15px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        margin-bottom: 12px;
        border-left: 5px solid #FF8C94;
    }
    .restaurant-card { border-left: 5px solid #FFD54F; }
    .transport-card { border-left: 5px solid #4FC3F7; }
    
    /* 標籤樣式 */
    .tag {
        display: inline-block;
        padding: 2px 8px;
        border-radius: 5px;
        font-size: 0.8rem;
        font-weight: bold;
        margin-right: 5px;
        color: white;
    }
    .tag-must-eat { background-color: #E57373; }
    .tag-must-buy { background-color: #BA68C8; }
    .tag-tips { background-color: #4DB6AC; }
    
    /* 手機優化按鈕 */
    .stButton>button {
        width: 100%;
        border-radius: 20px;
        border: none;
        background-color: #007AFF;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 側邊欄或頂部導覽 ---
tab1, tab2, tab3 = st.tabs(["🗓 每日行程", "🏠 住宿/航班", "💰 預算記帳"])

# --- Tab 1: 每日行程 ---
with tab1:
    st.title("☀️ 沖繩自駕趣")
    
    days = {
        "Day 1: 1/1 (週四)": {
            "weather": "☁️ 那霸 18°C - 21°C",
            "items": [
                {"type": "transport", "time": "16:50", "name": "桃園國際機場 (IT232)", "url": "https://www.google.com/maps/search/桃園機場"},
                {"type": "spot", "time": "19:10", "name": "抵達那霸機場", "url": "https://www.google.com/maps/search/那霸機場"},
                {"type": "restaurant", "time": "21:58", "name": "Steak House 88 Jr.", "url": "https://www.google.com/maps/search/Steak+House+88+Jr.+Matsuyama", "tags": [("必吃", "龍蝦牛排餐"), ("攻略", "CP值極高，附自助吧")]}
            ]
        },
        "Day 2: 1/2 (週五)": {
            "weather": "☀️ 南部 20°C",
            "items": [
                {"type": "transport", "time": "09:07", "name": "Relax Car Rental 取車", "url": "https://www.google.com/maps/search/Relax+Car+Rental+Okinawa"},
                {"type": "spot", "time": "11:02", "name": "瀬長島 Umikaji Terrace", "url": "https://www.google.com/maps/search/瀬長島", "tags": [("必吃", "幸福鬆餅"), ("必買", "手作皮革")]},
                {"type": "restaurant", "time": "15:04", "name": "玉泉洞 (沖繩世界)", "url": "https://www.google.com/maps/search/玉泉洞", "tags": [("攻略", "全長5公里鐘乳石洞")]}
            ]
        },
        "Day 3: 1/3 (週六)": {
            "weather": "☁️ 中部 19°C",
            "items": [
                {"type": "spot", "time": "11:43", "name": "敘敘苑 燒肉 (PARCO CITY)", "url": "https://www.google.com/maps/search/敘敘苑+PARCO+CITY", "tags": [("必點", "牛舌、商業午餐")]},
                {"type": "spot", "time": "14:44", "name": "寶可夢中心 (永旺夢樂城)", "url": "https://www.google.com/maps/search/Pokemon+Center+Okinawa", "tags": [("必買", "沖繩限定皮卡丘")]}
            ]
        },
        "Day 4: 1/4 (週日)": {
            "weather": "🌊 北部 21°C",
            "items": [
                {"type": "spot", "time": "13:58", "name": "古宇利蝦蝦飯", "url": "https://www.google.com/maps/search/Kouri+Shrimp", "tags": [("必點", "蒜味奶油蝦")]},
                {"type": "spot", "time": "15:28", "name": "美麗海水族館", "url": "https://www.google.com/maps/search/Churaumi+Aquarium", "tags": [("攻略", "黑潮之海餵食秀")]}
            ]
        }
    }

    for day, content in days.items():
        with st.expander(f"📅 {day} | {content['weather']}", expanded=True):
            for item in content['items']:
                card_class = "transport-card" if item['type'] == 'transport' else ("restaurant-card" if item['type'] == 'restaurant' else "")
                
                st.markdown(f"""
                <div class="trip-card {card_class}">
                    <small>{item['time']}</small><br>
                    <strong>{item['name']}</strong>
                </div>
                """, unsafe_allow_html=True)
                
                if "tags" in item:
                    tag_html = ""
                    for t_type, t_text in item['tags']:
                        t_class = "tag-must-eat" if t_type in ["必吃", "必點"] else "tag-tips"
                        tag_html += f'<span class="tag {t_class}">{t_type}: {t_text}</span>'
                    st.markdown(tag_html, unsafe_allow_html=True)
                
                st.link_button(f"🚗 導航至 {item['name']}", item['url'])
                st.write("")

# --- Tab 2: 住宿/航班 ---
with tab2:
    st.header("✈️ 航班資訊")
    st.info("**去程**：1/1 IT232 16:50-19:10  \n**回程**：1/5 IT233 20:10-21:10")
    
    st.header("🏨 住宿資訊")
    st.success("**沖繩那霸 La'gent 飯店** \n地址：〒900-0014 沖縄県那覇市松尾２丁目１−１  \n電話：098-860-0300")
    
    st.header("☎️ 緊急聯絡")
    st.warning("警察局：110 | 急救/火警：119  \n租車公司 (Relax)：098-xxx-xxxx")

# --- Tab 3: 預算記帳 ---
with tab3:
    st.header("💰 行程預算表")
    df = pd.DataFrame([
        {"項目": "機票", "金額": 12000, "狀態": "已付"},
        {"項目": "住宿", "金額": 8500, "狀態": "預計"},
        {"項目": "租車", "金額": 3000, "狀態": "預計"},
    ])
    st.table(df)
    st.metric("預估總支出", f"NT$ {df['金額'].sum():,}")
