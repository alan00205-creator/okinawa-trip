import streamlit as st
import pandas as pd
import streamlit.components.v1 as components

# 1. 網頁配置：手機優先設計
st.set_page_config(page_title="2026 沖繩家族行 App", page_icon="🐢", layout="wide")

# 2. 自定義 CSS：打造可愛、專業的 App 感
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+TC:wght@400;700&display=swap');
    html, body, [class*="css"] { font-family: 'Noto Sans TC', sans-serif; }
    
    .stApp { background: #F7F9FC; }
    
    /* 卡片設計 */
    .trip-card {
        background-color: white;
        padding: 1.2rem;
        border-radius: 18px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.05);
        margin-bottom: 0.8rem;
        border-left: 8px solid #FF8C94; /* 預設景點紅色 */
    }
    .restaurant-card { border-left-color: #FFD54F; } /* 餐廳黃色 */
    .transport-card { border-left-color: #4FC3F7; }  /* 交通藍色 */
    
    /* 標籤樣式 */
    .tag {
        display: inline-block;
        padding: 3px 10px;
        border-radius: 8px;
        font-size: 0.75rem;
        font-weight: bold;
        margin: 4px 4px 4px 0;
        color: white;
    }
    .tag-must-eat { background-color: #FF5252; }
    .tag-must-buy { background-color: #7E57C2; }
    .tag-tips { background-color: #26A69A; }

    /* 手機導航按鈕 */
    .stButton>button {
        width: 100%;
        border-radius: 25px;
        height: 3rem;
        background-color: #007AFF !important;
        color: white !important;
        font-weight: bold;
        border: none;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. 實時天氣函數 (那霸 ID: 1856057, 名護 ID: 1856068)
def render_weather(city_id):
    weather_html = f"""
    <div style="margin-bottom: 20px;">
        <iframe src="https://openweathermap.org/themes/openweathermap/assets/vendor/owm/js/weather-widget-generator.php?id={city_id}&days=3&units=metric&lang=zh_tw" 
        width="100%" height="240" frameborder="0" scrolling="no"></iframe>
    </div>
    """
    components.html(weather_html, height=250)

# 4. 頂部導覽分頁
tab1, tab2, tab3 = st.tabs(["🗓 每日行程", "🏨 住宿/航班", "💰 預算/備忘"])

# --- Tab 1: 每日行程 ---
with tab1:
    st.title("🌊 2026 沖繩自駕趣")
    
    # --- Day 1 ---
    st.subheader("📅 Day 1: 1/1 (週四)")
    render_weather("1856057") # 那霸天氣
    
    d1_items = [
        {"type": "transport", "time": "16:50", "name": "桃園機場 (IT232)", "url": "https://www.google.com/maps/search/桃園機場"},
        {"type": "spot", "time": "20:56", "name": "La'gent 飯店入住", "url": "https://www.google.com/maps/search/La'gent+Hotel+Okinawa+Naha"},
        {"type": "restaurant", "time": "21:58", "name": "Steak House 88 Jr.", "url": "https://www.google.com/maps/search/Steak+House+88+Jr.+Matsuyama", "tags": [("必吃", "美式牛排"), ("攻略", "附自助吧")]}
    ]
    for item in d1_items:
        card_class = "transport-card" if item['type'] == 'transport' else ("restaurant-card" if item['type'] == 'restaurant' else "")
        st.markdown(f'<div class="trip-card {card_class}"><small>⏰ {item["time"]}</small><br><b>{item["name"]}</b></div>', unsafe_allow_html=True)
        if "tags" in item:
            tag_html = "".join([f'<span class="tag {"tag-must-eat" if t[0]=="必吃" else "tag-tips"}">{t[0]}: {t[1]}</span>' for t in item["tags"]])
            st.markdown(tag_html, unsafe_allow_html=True)
        st.link_button(f"🚀 導航", item['url'])

    st.divider()

    # --- Day 2 ---
    st.subheader("📅 Day 2: 1/2 (週五)")
    d2_items = [
        {"type": "transport", "time": "09:07", "name": "Relax Car Rental 取車", "url": "https://www.google.com/maps/search/Relax+Car+Rental+Okinawa"},
        {"type": "spot", "time": "11:02", "name": "Posillipo 海景餐廳", "url": "https://www.google.com/maps/search/Posillipo+Okinawa"},
        {"type": "spot", "time": "12:36", "name": "瀬長島 Umikaji Terrace", "url": "https://www.google.com/maps/search/Umikaji+Terrace", "tags": [("必吃", "幸福鬆餅")]},
        {"type": "spot", "time": "15:04", "name": "玉泉洞 (沖繩世界)", "url": "https://www.google.com/maps/search/玉泉洞"}
    ]
    for item in d2_items:
        card_class = "transport-card" if item['type'] == 'transport' else ("restaurant-card" if item['type'] == 'restaurant' else "")
        st.markdown(f'<div class="trip-card {card_class}"><b>{item["name"]}</b></div>', unsafe_allow_html=True)
        st.link_button(f"🚀 導航", item['url'])

    st.divider()

    # --- Day 3-4 (切換到北部天氣) ---
    st.subheader("📅 Day 3 & 4: 中北部行程")
    render_weather("1856068") # 名護天氣
    
    d4_items = [
        {"type": "restaurant", "time": "13:58", "name": "古宇利蝦蝦飯", "url": "https://www.google.com/maps/search/Kouri+Shrimp", "tags": [("必點", "蒜味奶油蝦")]},
        {"type": "spot", "time": "15:28", "name": "美麗海水族館", "url": "https://www.google.com/maps/search/Okinawa+Churaumi+Aquarium", "tags": [("攻略", "黑潮之海餵食秀")]},
        {"type": "restaurant", "time": "17:59", "name": "百年古家 大家 阿古豬", "url": "https://www.google.com/maps/search/百年古家+大家", "tags": [("必吃", "阿古豬涮涮鍋")]}
    ]
    for item in d4_items:
        card_class = "restaurant-card" if item['type'] == 'restaurant' else ""
        st.markdown(f'<div class="trip-card {card_class}"><b>{item["name"]}</b></div>', unsafe_allow_html=True)
        if "tags" in item:
            tag_html = "".join([f'<span class="tag tag-must-eat">{t[0]}: {t[1]}</span>' for t in item["tags"]])
            st.markdown(tag_html, unsafe_allow_html=True)
        st.link_button(f"🚀 導航", item['url'])

    st.divider()

    # --- Day 5 ---
    st.subheader("📅 Day 5: 1/5 (週一)")
    d5_items = [
        {"type": "spot", "time": "09:22", "name": "DMM Kariyushi 水族館", "url": "https://www.google.com/maps/search/DMM+Kariyushi+Aquarium"},
        {"type": "restaurant", "time": "11:29", "name": "暖暮拉麵 (系滿店)", "url": "https://www.google.com/maps/search/暖暮拉麵+系滿店"},
        {"type": "spot", "time": "12:35", "name": "ASHIBINAA Outlet", "url": "https://www.google.com/maps/search/ASHIBINAA+Outlet"},
        {"type": "transport", "time": "16:33", "name": "珀塔瑪 機場飯糰", "url": "https://www.google.com/maps/search/Potama+Naha+Airport", "tags": [("必買", "炸蝦飯糰")]}
    ]
    for item in d5_items:
        card_class = "transport-card" if item['type'] == 'transport' else ""
        st.markdown(f'<div class="trip-card {card_class}"><b>{item["name"]}</b></div>', unsafe_allow_html=True)
        st.link_button(f"🚀 導航", item['url'])

# --- Tab 2: 住宿/航班 ---
with tab2:
    st.header("✈️ 航班資訊")
    st.info("去程：1/1 IT232 16:50-19:10\n回程：1/5 IT233 20:10-21:10")
    st.header("🏨 飯店資訊")
    st.success("沖繩那霸 La'gent 飯店\n地址：〒900-0014 沖縄県那覇市松尾２丁目１−１\n電話：098-860-0300")

# --- Tab 3: 預算 ---
with tab3:
    st.header("💰 行程預算表")
    budget_df = pd.DataFrame([
        {"項目": "機票費用", "預算": "45,000", "狀態": "✅ 已付"},
        {"項目": "住宿費用", "預算": "30,000", "狀態": "✅ 已付"},
        {"項目": "租車費用", "預算": "15,000", "狀態": "⏳ 預約中"}
    ])
    st.table(budget_df)
