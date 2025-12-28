import streamlit as st

# 1. 網頁配置
st.set_page_config(
    page_title="2026年1月沖繩家族旅遊",
    page_icon="🚗",
    layout="wide"
)

# 2. UI 風格設計 (手機優先，大按鈕導航)
st.markdown("""
    <style>
    .stApp { background-color: #F8F9FC; }
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
        border: 1px solid #E0E0E0;
        margin-bottom: 5px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
        color: #333;
    }
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

st.title("🚗 2026年1月沖繩家族旅遊")

# 3. 完整五天行程數據 (對應 PDF 所有點位)
plan = {
    "📅 Day 1: 1/1 (週四)": [
        ("16:50 臺灣桃園國際機場", "https://www.google.com/maps/search/?api=1&query=桃園國際機場"),
        ("19:10 那霸機場", "https://www.google.com/maps/search/?api=1&query=那霸機場"),
        ("20:38 美榮橋", "https://www.google.com/maps/search/?api=1&query=美榮橋"),
        ("20:56 住宿: 沖繩那霸 La'gent 飯店", "https://www.google.com/maps/search/?api=1&query=沖繩那霸La'gent飯店"),
        ("21:58 晚餐: Steak House 88 Jr. Matsuyama", "https://www.google.com/maps/search/?api=1&query=Steak+House+88+Jr.+Matsuyama")
    ],
    "📅 Day 2: 1/2 (週五)": [
        ("09:07 Relax car rental (取車)", "https://www.google.com/maps/search/?api=1&query=relax+car+rental+沖繩"),
        ("09:41 波上宮", "https://www.google.com/maps/search/?api=1&query=波上宮"),
        ("11:02 午餐: Posillipo 海景餐廳", "https://www.google.com/maps/search/?api=1&query=Posillipo海景餐廳"),
        ("12:36 瀨長島", "https://www.google.com/maps/search/?api=1&query=瀨長島"),
        ("15:04 玉泉洞", "https://www.google.com/maps/search/?api=1&query=玉泉洞"),
        ("16:39 國際通屋台村 (夜市)", "https://www.google.com/maps/search/?api=1&query=國際通屋台村"),
        ("17:46 國際通 (逛街)", "https://www.google.com/maps/search/?api=1&query=國際通")
    ],
    "📅 Day 3: 1/3 (週六)": [
        ("09:16 首里城", "https://www.google.com/maps/search/?api=1&query=首里城"),
        ("10:39 SAN-A 浦添西海岸 PARCO CITY", "https://www.google.com/maps/search/?api=1&query=SAN-A+浦添西海岸+PARCO+CITY"),
        ("11:43 午餐: 敘敘苑 (PARCO CITY店)", "https://www.google.com/maps/search/?api=1&query=敘敘苑+沖繩浦添+PARCO+CITY店"),
        ("13:43 AEON MALL Okinawa Rycom", "https://www.google.com/maps/search/?api=1&query=AEON+MALL+Okinawa+Rycom"),
        ("14:44 沖繩寶可夢中心", "https://www.google.com/maps/search/?api=1&query=沖繩寶可夢中心"),
        ("15:59 美國村", "https://www.google.com/maps/search/?api=1&query=美國村"),
        ("19:02 晚餐: 迴轉壽司市場美浜店", "https://www.google.com/maps/search/?api=1&query=迴轉壽司市場美浜店")
    ],
    "📅 Day 4: 1/4 (週日)": [
        ("09:57 Hoshino Resorts BANTA CAFE", "https://www.google.com/maps/search/?api=1&query=Hoshino+Resorts+BANTA+CAFE"),
        ("11:28 萬座毛", "https://www.google.com/maps/search/?api=1&query=萬座毛"),
        ("12:54 古宇利海洋塔", "https://www.google.com/maps/search/?api=1&query=古宇利海洋塔"),
        ("13:58 午餐: 古宇利蝦蝦飯", "https://www.google.com/maps/search/?api=1&query=古宇利蝦蝦飯"),
        ("15:28 沖繩美麗海水族館", "https://www.google.com/maps/search/?api=1&query=沖繩美麗海水族館"),
        ("17:59 晚餐: 百年古家 大家 (阿古豬)", "https://www.google.com/maps/search/?api=1&query=百年古家+大家")
    ],
    "📅 Day 5: 1/5 (週一)": [
        ("09:22 DMM Kariyushi 水族館", "https://www.google.com/maps/search/?api=1&query=DMM+Kariyushi+水族館"),
        ("11:29 午餐: 暖暮拉麵 (系滿店)", "https://www.google.com/maps/search/?api=1&query=暖暮系滿店"),
        ("12:35 購物: 沖繩 ASHIBINAA Outlet", "https://www.google.com/maps/search/?api=1&query=沖繩ASHIBINAA+Outlet"),
        ("15:52 還車: Relax car rental", "https://www.google.com/maps/search/?api=1&query=relax+car+rental+沖繩"),
        ("16:33 點心: 珀塔瑪 那霸機場店", "https://www.google.com/maps/search/?api=1&query=珀塔瑪+那霸機場"),
        ("18:10 那霸機場 (搭機)", "https://www.google.com/maps/search/?api=1&query=那霸機場"),
        ("20:10 臺灣桃園國際機場 (返抵)", "https://www.google.com/maps/search/?api=1&query=桃園國際機場")
    ]
}

# 4. 渲染行程
for day, items in plan.items():
    st.markdown(f'<div class="day-header">{day}</div>', unsafe_allow_html=True)
    for title, url in items:
        st.markdown(f'<div class="trip-card">{title}</div>', unsafe_allow_html=True)
        st.link_button("📍 Google 地圖導航", url)
