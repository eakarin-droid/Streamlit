import streamlit as st
from datetime import datetime

# ==============================================================================
# PAGE CONFIGURATION
# ==============================================================================
st.set_page_config(
    page_title="NeoCalc • เครื่องคิดเลขดีไซน์ใหม่",
    page_icon="⚡",
    layout="centered"
)

# ==============================================================================
# CUSTOM STYLING (MODERN CYBER-GLASS DESIGN)
# ==============================================================================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Prompt:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500;700&display=swap');

html, body, [class*="css"], .stApp {
    font-family: 'Prompt', sans-serif !important;
}

/* Deep Space Violet Background */
.stApp {
    background: radial-gradient(circle at 10% 20%, #1e1b4b 0%, #0f172a 50%, #020617 100%) !important;
    color: #f1f5f9;
}

/* Header Styling */
.header-container {
    text-align: center;
    padding: 1.5rem 0 1rem 0;
}

.brand-badge {
    display: inline-block;
    padding: 0.3rem 0.9rem;
    background: linear-gradient(135deg, rgba(99, 102, 241, 0.25), rgba(168, 85, 247, 0.25));
    border: 1px solid rgba(168, 85, 247, 0.45);
    border-radius: 9999px;
    color: #c084fc;
    font-size: 0.78rem;
    font-weight: 600;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    margin-bottom: 0.6rem;
}

.gradient-title {
    font-size: 2.2rem;
    font-weight: 700;
    background: linear-gradient(135deg, #ffffff 25%, #c084fc 65%, #6366f1 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin: 0;
    line-height: 1.25;
}

.sub-title {
    color: #94a3b8;
    font-size: 0.95rem;
    margin-top: 0.4rem;
}

/* Digital LED Display Screen */
.digital-screen {
    background: linear-gradient(180deg, #070b13 0%, #0f172a 100%);
    border: 1px solid rgba(99, 102, 241, 0.35);
    border-radius: 18px;
    padding: 1.4rem 1.6rem;
    margin: 1.2rem 0;
    position: relative;
    box-shadow: inset 0 3px 12px rgba(0, 0, 0, 0.7), 0 10px 25px -8px rgba(99, 102, 241, 0.2);
}

.screen-badge {
    position: absolute;
    top: 14px;
    left: 18px;
    font-size: 0.72rem;
    color: #64748b;
    font-weight: 600;
    letter-spacing: 1.5px;
    text-transform: uppercase;
}

.formula-text {
    font-family: 'JetBrains Mono', monospace;
    font-size: 1rem;
    color: #94a3b8;
    text-align: right;
    min-height: 1.5rem;
    letter-spacing: 0.5px;
}

.result-number {
    font-family: 'JetBrains Mono', monospace;
    font-size: 2.4rem;
    font-weight: 700;
    color: #38bdf8;
    text-align: right;
    margin-top: 0.2rem;
    text-shadow: 0 0 25px rgba(56, 189, 248, 0.45);
    word-break: break-all;
    line-height: 1.15;
}

.result-number.error {
    color: #f87171 !important;
    font-size: 1.3rem !important;
    text-shadow: 0 0 20px rgba(248, 113, 113, 0.4) !important;
}

/* Input Fields Styling */
div[data-testid="stNumberInput"] label {
    font-weight: 500 !important;
    color: #cbd5e1 !important;
    font-size: 0.92rem !important;
}

div[data-testid="stNumberInput"] input {
    font-family: 'JetBrains Mono', monospace !important;
    font-size: 1.15rem !important;
    border-radius: 14px !important;
    background: rgba(15, 23, 42, 0.75) !important;
    border: 1px solid rgba(255, 255, 255, 0.12) !important;
    color: #f8fafc !important;
    padding: 0.65rem 0.85rem !important;
    box-shadow: inset 0 2px 4px rgba(0, 0, 0, 0.3) !important;
}

div[data-testid="stNumberInput"] input:focus {
    border-color: #818cf8 !important;
    box-shadow: 0 0 0 2px rgba(129, 140, 248, 0.3) !important;
}

/* Operation Radio Control */
div[data-testid="stRadio"] > label {
    font-weight: 600 !important;
    color: #cbd5e1 !important;
    font-size: 0.92rem !important;
    margin-bottom: 0.4rem !important;
}

div[data-testid="stRadio"] div[role="radiogroup"] {
    background: rgba(15, 23, 42, 0.65);
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 16px;
    padding: 8px 12px;
    gap: 10px;
}

/* Primary Button Styling */
div.stButton > button {
    background: linear-gradient(135deg, #6366f1 0%, #8b5cf6 50%, #d946ef 100%) !important;
    color: #ffffff !important;
    font-weight: 600 !important;
    font-size: 1.05rem !important;
    border-radius: 14px !important;
    border: none !important;
    padding: 0.7rem 1.6rem !important;
    box-shadow: 0 10px 25px -5px rgba(99, 102, 241, 0.45) !important;
    transition: all 0.25s ease !important;
    width: 100% !important;
    cursor: pointer !important;
}

div.stButton > button:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 15px 30px -4px rgba(168, 85, 247, 0.55) !important;
    filter: brightness(1.1) !important;
}

div.stButton > button:active {
    transform: translateY(0) !important;
}

/* Secondary Action Button */
div[data-testid="stButton"] button[kind="secondary"] {
    background: rgba(30, 41, 59, 0.6) !important;
    color: #cbd5e1 !important;
    border: 1px solid rgba(255, 255, 255, 0.12) !important;
    box-shadow: none !important;
}

div[data-testid="stButton"] button[kind="secondary"]:hover {
    background: rgba(51, 65, 85, 0.8) !important;
    color: #ffffff !important;
}

/* History Card */
.history-item {
    background: rgba(15, 23, 42, 0.6);
    border: 1px solid rgba(255, 255, 255, 0.06);
    border-radius: 10px;
    padding: 0.6rem 0.8rem;
    margin-bottom: 0.5rem;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.88rem;
    display: flex;
    justify-content: space-between;
    align-items: center;
}
.history-time {
    color: #64748b;
    font-size: 0.72rem;
}
</style>
""", unsafe_allow_html=True)

# ==============================================================================
# STATE MANAGEMENT
# ==============================================================================
if "history" not in st.session_state:
    st.session_state.history = []

if "num1_val" not in st.session_state:
    st.session_state.num1_val = 5.00

if "num2_val" not in st.session_state:
    st.session_state.num2_val = 5.00

# ==============================================================================
# HEADER SECTION
# ==============================================================================
st.markdown("""
<div class="header-container">
    <div class="brand-badge">⚡ Next-Gen Calculator</div>
    <div class="gradient-title">เครื่องคิดเลขจำลอง</div>
    <div class="sub-title">คำนวณแม่นยำ พร้อมอินเทอร์เฟซสไตล์โมเดิร์น</div>
</div>
""", unsafe_allow_html=True)

# ==============================================================================
# DIGITAL DISPLAY SCREEN
# ==============================================================================
# จอแสดงผลลัพธ์แบบดิจิทัล
screen_placeholder = st.empty()

# ==============================================================================
# INPUT CONTROLS
# ==============================================================================
# ช่องกรอกตัวเลข 2 ฝั่ง พร้อมปุ่มสลับค่า
col_input1, col_swap, col_input2 = st.columns([5, 1, 5])

with col_input1:
    num1 = st.number_input(
        "ตัวเลขที่ 1 (Number 1)",
        value=st.session_state.num1_val,
        step=1.00,
        format="%.2f",
        key="input_num1"
    )

with col_swap:
    st.write("") # ปรับ alignment
    st.write("")
    if st.button("⇄", help="สลับตัวเลข 1 กับ 2", key="swap_btn"):
        st.session_state.num1_val = num2
        st.session_state.num2_val = num1
        st.rerun()

with col_input2:
    num2 = st.number_input(
        "ตัวเลขที่ 2 (Number 2)",
        value=st.session_state.num2_val,
        step=1.00,
        format="%.2f",
        key="input_num2"
    )

# เลือกการดำเนินการ (Radio Buttons แนวนอน จัดหมวดหมู่สวยงาม)
operations = {
    "➕ บวก (+)": "+",
    "➖ ลบ (-)": "-",
    "✖️ คูณ (×)": "×",
    "➗ หาร (÷)": "÷",
    "⚡ ยกกำลัง (xʸ)": "^",
    "🔄 เศษเหลือ (%)": "%"
}

selected_op_label = st.radio(
    "เลือกการดำเนินการทางคณิตศาสตร์:",
    options=list(operations.keys()),
    horizontal=True
)

op_symbol = operations[selected_op_label]

# ==============================================================================
# CALCULATION LOGIC & ACTION
# ==============================================================================
col_btn1, col_btn2 = st.columns([3, 1])

with col_btn1:
    calculate_clicked = st.button("✨ คำนวณผลลัพธ์ (Calculate)")

with col_btn2:
    if st.button("🔄 ล้างค่า", key="reset_btn"):
        st.session_state.num1_val = 0.00
        st.session_state.num2_val = 0.00
        st.rerun()

# ประมวลผลคำนวณ
formula_display = f"{num1:g} {op_symbol} {num2:g}"
result_text = "READY"
is_error = False

if calculate_clicked:
    try:
        if op_symbol == "+":
            ans = num1 + num2
        elif op_symbol == "-":
            ans = num1 - num2
        elif op_symbol == "×":
            ans = num1 * num2
        elif op_symbol == "÷":
            if num2 == 0:
                raise ZeroDivisionError("ไม่สามารถหารด้วยศูนย์ได้")
            ans = num1 / num2
        elif op_symbol == "^":
            ans = num1 ** num2
        elif op_symbol == "%":
            if num2 == 0:
                raise ZeroDivisionError("ไม่สามารถหารเอาเศษด้วยศูนย์ได้")
            ans = num1 % num2

        result_text = f"{ans:,.4f}".rstrip('0').rstrip('.') if '.' in f"{ans:,.4f}" else f"{ans:,.0f}"
        
        # บันทึกลงประวัติ
        time_str = datetime.now().strftime("%H:%M:%S")
        st.session_state.history.insert(0, {
            "formula": formula_display,
            "result": result_text,
            "time": time_str
        })
        # จำกัดประวัติไม่เกิน 10 รายการ
        if len(st.session_state.history) > 10:
            st.session_state.history.pop()

    except ZeroDivisionError as e:
        is_error = True
        result_text = "Error: หารด้วยศูนย์ไม่ได้ ⚠️"
    except Exception as e:
        is_error = True
        result_text = "Error: คำนวณไม่สำเร็จ"

# เรนเดอร์หน้าจอ LED แสดงผล
screen_placeholder.markdown(f"""
<div class="digital-screen">
    <div class="screen-badge">Digital OLED Display</div>
    <div class="formula-text">{formula_display if calculate_clicked else "0.00"}</div>
    <div class="result-number {'error' if is_error else ''}">{result_text}</div>
</div>
""", unsafe_allow_html=True)

# ==============================================================================
# SIDEBAR - HISTORY & QUICK INFO
# ==============================================================================
with st.sidebar:
    st.markdown("### 📋 ประวัติการคำนวณ")
    st.caption("บันทึกการคำนวณล่าสุด 10 รายการ")

    if st.session_state.history:
        for item in st.session_state.history:
            st.markdown(f"""
            <div class="history-item">
                <span>{item['formula']} = <b>{item['result']}</b></span>
                <span class="history-time">{item['time']}</span>
            </div>
            """, unsafe_allow_html=True)
        
        if st.button("🗑️ ล้างประวัติทั้งหมด", key="clear_history"):
            st.session_state.history = []
            st.rerun()
    else:
        st.info("ยังไม่มีประวัติการคำนวณ")

    st.divider()
    st.markdown("#### 💡 ฟีเจอร์เพิ่มเติมที่เพิ่มให้:")
    st.markdown("""
    - ⚡ **ดีไซน์ Cyber-Glass**: โทน Deep Violet & Neon
    - 📺 **OLED Screen**: หน้าจอแสดงสูตรและผลลัพธ์แบบดิจิทัล
    - ⇄ **สลับค่าทันใจ**: สลับตัวเลขที่ 1 และ 2 ได้ในคลิกเดียว
    - 🚀 **ฟังก์ชันเสริม**: รองรับเลขยกกำลัง ($x^y$) และหารเอาเศษ (%)
    - 🕒 **ระบบประวัติ**: บันทึกรายการคำนวณใน Sidebar
    """)
