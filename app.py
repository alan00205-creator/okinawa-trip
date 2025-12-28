import streamlit as st

# 1. 網頁配置：定義標題與圖示
st.set_page_config(
    page_title="2026年1月沖繩家族旅遊", 
    page_icon="🚗", 
    layout="wide"
)

# 2. 手機版 App 優化 UI
st.markdown("""
    <style>
    .stApp { background-color: #F8F9FA; }
    .day-header {
        background-color: #007AFF;
        color: white;
        padding: 12px 15px;
        border-radius: 12px;
        margin: 20px 0 10px 0;
        font-weight: bold;
        font-size: 1.2rem;
    }
    .trip-card {
        background-color: white;
        padding: 15px;
        border-radius: 12px;
        border: 1px solid #EEE;
        margin-bottom: 5px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
        color: #333;
    }
    /* 讓按鈕寬度 100% 方便點擊 */
    .stButton>button {
        width: 100%;
        border-radius: 25px;
        background-color: #007AFF !important;
        color: white !important;
        height: 50px;
        font-weight: bold;
        border: none;
        margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🚗 2026 沖繩家族行")

# 3. 更新後的行程數據：使用正確的 Google Maps 搜尋連結
# 格式為 https://www.google.com/maps/search/?api=1&query=關鍵字
plan = {
    "📅 Day 1: 1/1 (週四)": [
        ("16:50 桃園國際機場", "https://www.google.com/maps/search/?api=1&query=Taiwan+Taoyuan+International+Airport"),
        ("19:10 那霸機場", "https://www.google.com/maps/search/?api=1&query=Naha+Airport"),
        ("20:56 住宿: La'gent 飯店", "https://www.google.com/maps/search/?api=1&query=La'gent+Hotel+Okinawa+Naha+Kokusai+Street"),
        ("21:58 晚餐: Steak House 88 Jr.", "https://www.google.com/maps/search/?api=1&query=Steak+House+88+Jr.+Matsuyama")
    ],
    "📅 Day 2: 1/2 (週五)": [
        ("09:07 取車: Relax Car Rental", "https://www.google.com/maps/search/?api=1&query=relax+car+rental+okinawa"),
        ("09:41 波上宮", "https://www.google.com/maps/search/?api=1&query=Naminoue+Gu"),
        ("11:02 午餐: Posillipo 海景餐廳", "https://www.google.com/maps/search/?api=1&query=POSILLIPO+cucina+meridionale"),
        ("12:36 瀨長島 Umikaji Terrace", "https://www.google.com/maps/search/?api=1&query=Umikaji+Terrace+Senagajima"),
        ("15:04 玉泉洞", "https://www.google.com/maps/search/?api=1&query=Gyokusendo+Cave")
    ],
    "📅 Day 3: 1/3 (週六)": [
        ("09:16 首里城", "https://www.google.com/maps/search/?api=1&query=Shurijo+Castle"),
        ("11:43 敘敘苑 燒肉 (PARCO CITY)", "https://www.google.com/maps/search/?api=1&query=Jojoen+Okinawa+Urasoe+PARCO+CITY"),
        ("14:44 寶可夢中心 (永旺夢樂城)", "https://www.google.com/maps/search/?api=1&query=Pokemon+Center+Okinawa"),
        ("15:59 美國村", "https://www.google.com/maps/search/?api=1&query=American+Village+Okinawa"),
        ("19:02 晚餐: 迴轉壽司市場", "https://www.google.com/maps/search/?api=1&query=Gourmet+Kaiten-Sushi+Ichiba")
    ],
    "📅 Day 4: 1/4 (週日)": [
        ("09:57 BANTA CAFE", "https://www.google.com/maps/search/?api=1&query=Hoshino+Resorts+BANTA+CAFE"),
        ("11:28 萬座毛", "https://www.google.com/maps/search/?api=1&query=Manzamo"),
        ("13:58 古宇利蝦蝦飯", "https://www.google.com/maps/search/?api=1&query=Kouri+Shrimp+Panari"),
        ("15:28 沖繩美麗海水族館", "https://www.google.com/maps/search/?api=1&query=Okinawa+Churaumi+Aquarium"),
        ("17:59 晚餐: 百年古家 大家", "https://www.google.com/maps/search/?api=1&query=Ufuya")
    ],
    "📅 Day 5: 1/5 (週一)": [
        ("09:22 DMM Kariyushi 水族館", "https://www.google.com/maps/search/?api=1&query=DMM+Kariyushi+Aquarium"),
        ("11:29 暖暮拉麵 (系滿店)", "https://www.google.com/maps/search/?api=1&query=Danbo+Ramen+Itoman"),
        ("12:35 ASHIBINAA Outlet", "https://www.google.com/maps/search/?api=1&query=Okinawa+Outlet+Mall+Ashibinaa"),
        ("15:52 還車: Relax Car Rental", "https://www.google.com/maps/search/?api=1&query=relax+car+rental+okinawa"),
        ("16:33 機場飯糰 珀塔瑪", "https://www.google.com/maps/search/?api=1&query=Potama+Naha+Airport")
    ]
}

# 4. 渲染行程
for day, items in plan.items():
    st.markdown(f'<div class="day-header">{day}</div>', unsafe_allow_html=True)
    for title, url in items:
        st.markdown(f'<div class="trip-card">{title}</div>', unsafe_allow_html=True)
        st.link_button("📍 Google 地圖導航", url)
