import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="UFC Stance Analyzer - Brian's Project",
    page_icon="🥊",
    layout="wide",
    initial_sidebar_state="expanded"
)

UFC_RED = "#D20A0A"
UFC_GOLD = "#C9A84C"
UFC_DARK = "#1A1A1A"
UFC_GREY = "#2D2D2D"
UFC_WHITE = "#F5F5F5"

# CSS trang trí cao cấp - CÓ CHỮ TRẮNG
st.markdown(f"""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Oswald:wght@400;500;600;700&display=swap');
    
    .stApp {{
        background: linear-gradient(135deg, {UFC_DARK}, #0A0A0A);
        font-family: 'Oswald', sans-serif;
        color: white;
    }}
    
    /* CHỮ TRẮNG HẾT */
    .stMarkdown, .stSelectbox label, .stNumberInput label, .stMetric label {{
        color: white !important;
    }}
    
    div, p, span, label {{
        color: #F5F5F5 !important;
    }}
    
    h1, h2, h3, h4, h5, h6 {{
        color: white !important;
    }}
    
    .stAlert {{
        color: #1A1A1A !important;
    }}
    
    .stSelectbox div, .stNumberInput div {{
        color: white !important;
    }}
    
    /* Header chính */
    .main-header {{
        background: linear-gradient(90deg, {UFC_RED}, #8B0000, {UFC_GOLD});
        padding: 30px;
        border-radius: 20px;
        text-align: center;
        margin-bottom: 30px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.5);
        border: 1px solid rgba(255,255,255,0.1);
    }}
    .main-header h1 {{
        color: white;
        font-size: 56px;
        margin: 0;
        text-shadow: 3px 3px 6px rgba(0,0,0,0.5);
        letter-spacing: 2px;
    }}
    .main-header p {{
        color: #f0f0f0;
        font-size: 20px;
        margin: 10px 0 0 0;
        opacity: 0.9;
    }}
    
    /* Card cho group */
    .group-card {{
        background: linear-gradient(135deg, {UFC_GREY}, #3A3A3A);
        padding: 30px;
        border-radius: 20px;
        text-align: center;
        border-left: 8px solid var(--group-color);
        margin: 20px 0;
        box-shadow: 0 5px 20px rgba(0,0,0,0.3);
        transition: transform 0.3s;
    }}
    .group-card:hover {{
        transform: translateY(-5px);
    }}
    .group-card h3 {{
        font-size: 28px;
        margin: 0;
        color: white;
    }}
    .group-percent {{
        font-size: 64px;
        font-weight: bold;
        margin: 10px 0;
        color: var(--group-color);
    }}
    
    /* Badge võ sĩ */
    .fighter-badge {{
        background: linear-gradient(135deg, {UFC_GREY}, #383838);
        padding: 8px 16px;
        border-radius: 30px;
        margin: 6px;
        display: inline-block;
        font-size: 14px;
        font-weight: 500;
        border: 1px solid rgba(210,10,10,0.3);
        transition: all 0.2s;
        color: white;
    }}
    .fighter-badge:hover {{
        border-color: {UFC_GOLD};
        transform: scale(1.02);
        color: {UFC_GOLD};
    }}
    
    /* Metric card */
    .metric-card {{
        background: linear-gradient(135deg, #2A2A2A, #222);
        padding: 20px;
        border-radius: 15px;
        text-align: center;
        border-bottom: 3px solid {UFC_GOLD};
    }}
    .metric-value {{
        font-size: 42px;
        font-weight: bold;
        color: {UFC_GOLD};
    }}
    
    /* Profile card cho Brian */
    .profile-card {{
        background: linear-gradient(135deg, #2A2A2A, #1A1A1A);
        padding: 25px;
        border-radius: 20px;
        text-align: center;
        border: 1px solid {UFC_GOLD};
        margin-bottom: 20px;
    }}
    .profile-name {{
        font-size: 28px;
        font-weight: bold;
        color: {UFC_GOLD};
    }}
    .profile-stat {{
        font-size: 18px;
        margin: 8px 0;
        color: white;
    }}
    
    /* Comparison bar */
    .compare-bar {{
        background-color: #333;
        border-radius: 10px;
        height: 30px;
        overflow: hidden;
        margin: 10px 0;
    }}
    .compare-fill {{
        background: linear-gradient(90deg, {UFC_RED}, {UFC_GOLD});
        height: 100%;
        display: flex;
        align-items: center;
        justify-content: flex-end;
        padding-right: 10px;
        color: white;
        font-weight: bold;
        border-radius: 10px;
    }}
    
    .footer {{
        text-align: center;
        padding: 30px;
        color: #888;
        margin-top: 50px;
        border-top: 1px solid #333;
    }}
    
    hr {{
        border-color: {UFC_RED};
        margin: 30px 0;
    }}
    
    /* Sidebar style */
    [data-testid="stSidebar"] {{
        background: linear-gradient(180deg, #1A1A1A, #0D0D0D);
        border-right: 1px solid {UFC_RED};
    }}
    
    [data-testid="stSidebar"] * {{
        color: white !important;
    }}
</style>
""", unsafe_allow_html=True)

# ============================================
# HEADER
# ============================================
st.markdown("""
<div class="main-header">
    <h1>🥊 UFC STANCE ANALYZER</h1>
    <p>Discover how rare your fighting style is in the UFC</p>
</div>
""", unsafe_allow_html=True)

# ============================================
# LOAD DATA
# ============================================
@st.cache_data
def load_data():
    df = pd.read_excel('UFC_Real_Fighters_update.xlsx', sheet_name=0)
    return df

def get_group(stance, handedness):
    if stance == "Orthodox" and handedness == "Right":
        return 1
    elif stance == "Orthodox" and handedness == "Left":
        return 2
    elif stance == "Southpaw" and handedness == "Left":
        return 3
    else:
        return 4

group_labels = {
    1: "ORTHODOX + RIGHT",
    2: "ORTHODOX + LEFT",
    3: "SOUTHPAW + LEFT",
    4: "🔥 SOUTHPAW + RIGHT 🔥"
}

group_colors = {
    1: "#2E86AB",
    2: "#A23B72",
    3: "#F18F01",
    4: UFC_GOLD
}

group_percent = {
    1: "49.0%",
    2: "5.9%",
    3: "25.5%",
    4: "19.6%"
}

group_size = {
    1: "25 fighters",
    2: "3 fighters",
    3: "13 fighters",
    4: "10 fighters"
}

try:
    df = load_data()
except:
    st.error("❌ Cannot load data. Please check file.")
    st.stop()

# ============================================
# THÔNG TIN BRIAN (BẠN)
# ============================================
BRIAN = {
    'name': '🥊 BRIAN PHU',
    'stance': 'Southpaw',
    'handedness': 'Right',
    'height_cm': 179,
    'weight_kg': 69,
    'reach_cm': 181,
    'group': 4
}

# ============================================
# SIDEBAR - THÔNG TIN
# ============================================
with st.sidebar:
    st.markdown("## 🏆 UFC DATABASE")
    st.markdown(f"**Total fighters:** {len(df)}")
    st.markdown(f"**Weight classes:** {df['Weight_Class'].nunique()}")
    st.markdown(f"**Countries:** {df['Country'].nunique()}")
    st.markdown("---")
    
    # Profile của Brian
    st.markdown("### 👤 CREATOR")
    st.markdown(f"""
    <div class="profile-card">
        <div class="profile-name">{BRIAN['name']}</div>
        <div class="profile-stat">🔥 {BRIAN['stance']} | {BRIAN['handedness']}-handed</div>
        <div class="profile-stat">📏 {BRIAN['height_cm']}cm | 📏 {BRIAN['reach_cm']}cm reach</div>
        <div class="profile-stat">⚖️ {BRIAN['weight_kg']}kg</div>
        <div class="profile-stat" style="color: {UFC_GOLD}">✨ Group 4 — Only 19.6%</div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 📊 GROUP 4 STATS")
    g4_stats = df[df['Group_ID'] == 4].agg({
        'Win_Rate': 'mean',
        'KO_Rate': 'mean',
        'Finish_Rate': 'mean'
    }).round(4)
    st.metric("🏆 Win Rate", f"{g4_stats['Win_Rate']*100:.0f}%")
    st.metric("💥 KO Rate", f"{g4_stats['KO_Rate']*100:.0f}%")
    st.metric("⚡ Finish Rate", f"{g4_stats['Finish_Rate']*100:.0f}%")

# ============================================
# MAIN CONTENT
# ============================================
st.markdown("### 🎯 ENTER YOUR FIGHTING STYLE")

col1, col2 = st.columns(2)

with col1:
    stance = st.selectbox(
        "**🥋 STANCE**",
        ["Orthodox", "Southpaw"],
        help="Orthodox = left foot forward, Southpaw = right foot forward",
        key="stance"
    )

with col2:
    handedness = st.selectbox(
        "**✋ HANDEDNESS**",
        ["Right", "Left"],
        help="Which hand is your dominant punching hand?",
        key="handedness"
    )

# ============================================
# NHẬP THÔNG SỐ CÁ NHÂN
# ============================================
st.markdown("---")
st.markdown("### 📏 YOUR PHYSICAL STATS")

col_h1, col_h2, col_h3 = st.columns(3)

with col_h1:
    user_height = st.number_input("**Height (cm)**", min_value=150, max_value=220, value=179, step=1)

with col_h2:
    user_weight = st.number_input("**Weight (kg)**", min_value=50, max_value=150, value=69, step=1)

with col_h3:
    user_reach = st.number_input("**Reach (cm)**", min_value=150, max_value=230, value=181, step=1)

# ============================================
# TÍNH TOÁN KẾT QUẢ
# ============================================
your_group = get_group(stance, handedness)
group_color = group_colors[your_group]

st.markdown("---")
st.markdown("## 📊 YOUR RESULT")

# Card hiển thị nhóm của bạn
st.markdown(f"""
<div class="group-card" style="--group-color: {group_color};">
    <h3 style="color: {group_color};">{group_labels[your_group]}</h3>
    <div class="group-percent" style="color: {group_color};">{group_percent[your_group]}</div>
    <p>of UFC fighters share your stance + handedness</p>
    <p><strong>{group_size[your_group]}</strong> elite fighters in this database</p>
</div>
""", unsafe_allow_html=True)

# So sánh với Brian
if your_group == 4:
    st.success("🔥🔥🔥 **YOU'RE IN THE SAME GROUP AS BRIAN!** 🔥🔥🔥\n\nRight-handed southpaw — the rarest combination! Only 19.6% of fighters.")
else:
    st.info(f"📌 **Brian's group:** Group 4 (Southpaw + Right-handed) — only 19.6% of fighters")

# ============================================
# SO SÁNH THÔNG SỐ VỚI VÕ SĨ CÙNG NHÓM
# ============================================
st.markdown("---")
st.markdown("### 📊 HOW DO YOU COMPARE WITH UFC FIGHTERS?")

# Tìm võ sĩ gần nhất trong cùng group
same_group_fighters = df[df['Group_ID'] == your_group].copy()

if len(same_group_fighters) > 0:
    same_group_fighters['height_diff'] = abs(same_group_fighters['Height_cm'] - user_height)
    same_group_fighters['reach_diff'] = abs(same_group_fighters['Reach_cm'] - user_reach)
    same_group_fighters['total_diff'] = same_group_fighters['height_diff'] + same_group_fighters['reach_diff']
    closest = same_group_fighters.loc[same_group_fighters['total_diff'].idxmin()]
    
    col_c1, col_c2, col_c3 = st.columns(3)
    
    with col_c1:
        st.markdown(f"""
        <div class="metric-card">
            <div style="font-size: 14px; color: #aaa;">CLOSEST MATCH</div>
            <div style="font-size: 24px; font-weight: bold; color: white;">{closest['Fighter_Name']}</div>
            <div style="color: white;">{closest['Weight_Class']}</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col_c2:
        st.markdown(f"""
        <div class="metric-card">
            <div style="font-size: 14px; color: #aaa;">HEIGHT</div>
            <div style="font-size: 28px; font-weight: bold; color: white;">{user_height}cm vs {closest['Height_cm']}cm</div>
            <div style="color: {UFC_GOLD};">{abs(user_height - closest['Height_cm'])}cm difference</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col_c3:
        st.markdown(f"""
        <div class="metric-card">
            <div style="font-size: 14px; color: #aaa;">REACH</div>
            <div style="font-size: 28px; font-weight: bold; color: white;">{user_reach}cm vs {closest['Reach_cm']}cm</div>
            <div style="color: {UFC_GOLD};">{abs(user_reach - closest['Reach_cm'])}cm difference</div>
        </div>
        """, unsafe_allow_html=True)
    
    # Thanh so sánh win rate
    st.markdown("---")
    st.markdown("#### 🏆 WIN RATE COMPARISON")
    
    your_win_rate_projection = closest['Win_Rate'] * (1 - (closest['total_diff'] / 300))
    your_win_rate_projection = max(0.4, min(0.95, your_win_rate_projection))
    
    col_w1, col_w2 = st.columns(2)
    
    with col_w1:
        fighter_percent = closest['Win_Rate'] * 100
        st.markdown(f"""
        <div class="compare-bar">
            <div class="compare-fill" style="width: {fighter_percent:.0f}%;">
                {closest['Fighter_Name']} - {fighter_percent:.0f}%
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col_w2:
        your_percent = your_win_rate_projection * 100
        st.markdown(f"""
        <div class="compare-bar">
            <div class="compare-fill" style="width: {your_percent:.0f}%; background: linear-gradient(90deg, {UFC_GOLD}, #FFD700);">
                YOU - {your_percent:.0f}%
            </div>
        </div>
        """, unsafe_allow_html=True)

# ============================================
# HIỂN THỊ VÕ SĨ CÙNG GROUP
# ============================================
st.markdown("---")
st.markdown(f"### 👊 FIGHTERS IN YOUR GROUP ({len(same_group_fighters)} fighters)")

fighters_html = ""
for _, fighter in same_group_fighters.head(12).iterrows():
    fighters_html += f'<span class="fighter-badge">{fighter["Fighter_Name"]}</span>'

st.markdown(fighters_html, unsafe_allow_html=True)

# ============================================
# GROUP 4 STATS CHI TIẾT
# ============================================
if your_group == 4:
    st.markdown("---")
    st.markdown("### 🌟 FAMOUS RIGHT-HANDED SOUTHPAWS")
    
    famous = df[df['Group_ID'] == 4][['Fighter_Name', 'Win_Rate', 'KO_Rate', 'Weight_Class']].head(8)
    
    cols = st.columns(4)
    for i, (_, row) in enumerate(famous.iterrows()):
        with cols[i % 4]:
            st.markdown(f"""
            <div style="background: linear-gradient(135deg, #2D2D2D, #222); padding: 15px; border-radius: 15px; margin: 8px; text-align: center;">
                <b style="font-size: 16px; color: white;">{row['Fighter_Name']}</b><br>
                <span style="font-size: 12px; color: #aaa;">{row['Weight_Class']}</span><br>
                <span style="color: {UFC_GOLD};">🏆 {row['Win_Rate']*100:.0f}%</span>
            </div>
            """, unsafe_allow_html=True)

# ============================================
# FOOTER
# ============================================
st.markdown(f"""
<div class="footer">
    🥊 Data from UFC Real Fighters Database | Built with Streamlit by Brian Phu 🥊<br>
    <span style="font-size: 12px; color: #888;">Right-handed Southpaw — {BRIAN['height_cm']}cm | {BRIAN['weight_kg']}kg | {BRIAN['reach_cm']}cm reach</span>
</div>
""", unsafe_allow_html=True)
