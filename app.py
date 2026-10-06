import streamlit as st
import numpy as np
import pandas as pd
import joblib
import os
# pyrefly: ignore [missing-import]
import plotly.graph_objects as go
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

# ==============================================================================
# 1. PAGE CONFIGURATION & THEME
# ==============================================================================
st.set_page_config(
    page_title="Iris Intelligence System",
    page_icon="🌼",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom High-Tech / Stealth Masculine UI Styling
custom_css = """
<style>
    /* Global Background & Font */
    @import url('https://fonts.googleapis.com/css2?family=Chakra+Petch:wght@400;500;600;700&family=Inter:wght@300;400;600;700&display=swap');

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    .stApp {
        background: radial-gradient(circle at 15% 15%, #111827 0%, #0b0f19 75%, #050811 100%);
        color: #e2e8f0;
    }

    /* Sidebar Dark Gunmetal Finish */
    section[data-testid="stSidebar"] {
        background-color: #0d121f !important;
        border-right: 1px solid rgba(255, 255, 255, 0.08);
    }
    
    section[data-testid="stSidebar"] h1, 
    section[data-testid="stSidebar"] h2, 
    section[data-testid="stSidebar"] h3 {
        color: #f8fafc;
        font-family: 'Chakra Petch', sans-serif;
        letter-spacing: 1px;
    }

    /* Primary Buttons - High-Performance Electric Cyan / Blue */
    div.stButton > button:first-child {
        background: linear-gradient(135deg, #0284c7 0%, #2563eb 50%, #1d4ed8 100%);
        color: #ffffff;
        font-family: 'Chakra Petch', sans-serif;
        font-size: 16px;
        font-weight: 700;
        letter-spacing: 1.5px;
        text-transform: uppercase;
        border: 1px solid #38bdf8;
        border-radius: 8px;
        padding: 0.65rem 1.2rem;
        box-shadow: 0 4px 14px rgba(2, 132, 199, 0.4);
        transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1);
    }
    div.stButton > button:first-child:hover {
        background: linear-gradient(135deg, #0ea5e9 0%, #3b82f6 100%);
        box-shadow: 0 6px 22px rgba(14, 165, 233, 0.65);
        border-color: #7dd3fc;
        transform: translateY(-2px);
    }

    /* Tactical HUD Metric Card */
    .hud-card {
        background: linear-gradient(145deg, rgba(17, 24, 39, 0.85) 0%, rgba(15, 23, 42, 0.75) 100%);
        border: 1px solid rgba(56, 189, 248, 0.2);
        box-shadow: 0 8px 24px rgba(0, 0, 0, 0.4), inset 0 1px 0 rgba(255, 255, 255, 0.05);
        border-radius: 12px;
        padding: 16px 20px;
        margin-bottom: 20px;
        position: relative;
        backdrop-filter: blur(8px);
    }
    
    .hud-card-accent {
        border-left: 4px solid #38bdf8;
    }

    /* Main Result Card - Carbon & Neon HUD */
    .prediction-card {
        background: linear-gradient(145deg, #111827 0%, #0f172a 60%, #1e1b4b 100%);
        border: 1px solid rgba(99, 102, 241, 0.35);
        border-radius: 16px;
        padding: 28px 24px;
        text-align: center;
        box-shadow: 0 12px 32px rgba(0, 0, 0, 0.5), 0 0 20px rgba(56, 189, 248, 0.15);
        position: relative;
        overflow: hidden;
    }

    .prediction-badge {
        display: inline-block;
        background: rgba(56, 189, 248, 0.12);
        color: #38bdf8;
        border: 1px solid rgba(56, 189, 248, 0.4);
        border-radius: 9999px;
        padding: 4px 14px;
        font-family: 'Chakra Petch', monospace;
        font-size: 13px;
        font-weight: 700;
        letter-spacing: 1.5px;
        text-transform: uppercase;
        margin-bottom: 12px;
    }

    .prediction-title {
        color: #ffffff;
        font-family: 'Chakra Petch', sans-serif;
        font-size: 40px;
        font-weight: 800;
        letter-spacing: 2px;
        margin: 6px 0 10px 0;
        text-transform: uppercase;
        text-shadow: 0 0 20px rgba(56, 189, 248, 0.4);
    }

    .confidence-tag {
        font-size: 16px;
        font-weight: 600;
        color: #94a3b8;
    }
    .confidence-value {
        color: #10b981;
        font-family: 'Chakra Petch', monospace;
        font-weight: 700;
        font-size: 18px;
    }

    /* Header Accent */
    .system-title {
        font-family: 'Chakra Petch', sans-serif;
        font-size: 34px;
        font-weight: 800;
        letter-spacing: 1px;
        color: #f8fafc;
        margin-bottom: 0px;
    }
    .system-subtitle {
        color: #64748b;
        font-size: 14px;
        font-family: 'Inter', sans-serif;
        font-weight: 500;
        letter-spacing: 0.5px;
    }

    /* Slider tweaks */
    div[data-testid="stSlider"] label {
        color: #cbd5e1 !important;
        font-weight: 600 !important;
        font-size: 13px !important;
    }
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# ==============================================================================
# 2. MODEL ENGINE (LOAD / AUTO-TRAIN)
# ==============================================================================
@st.cache_resource
def get_model():
    model_path = 'iris_model.pkl'
    if os.path.exists(model_path):
        return joblib.load(model_path)
    else:
        iris = load_iris()
        model = RandomForestClassifier(n_estimators=100, random_state=42)
        model.fit(iris.data, iris.target)
        joblib.dump(model, model_path)
        return model

model = get_model()

# Baseline benchmarks & metadata
feature_names = ['Sepal Length', 'Sepal Width', 'Petal Length', 'Petal Width']
dataset_averages = [5.84, 3.05, 3.76, 1.20]
class_names = ['Setosa', 'Versicolor', 'Virginica']

# ==============================================================================
# 3. SIDEBAR: TACTICAL CONTROL PANEL
# ==============================================================================
with st.sidebar:
    st.markdown("""
        <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 10px;">
            <span style="font-size: 28px;">🌼</span>
            <div>
                <div style="font-size: 18px; font-weight: 800; color: #f8fafc; font-family: 'Chakra Petch', sans-serif;">CONTROL MATRIX</div>
                <div style="font-size: 11px; color: #38bdf8; font-weight: 600; letter-spacing: 1px;">TELEMETRY INPUTS</div>
            </div>
        </div>
    """, unsafe_allow_html=True)
    st.caption("Adjust physical measurements to simulate botanical specimen parameters:")
    st.write("")

    sepal_length = st.slider("Sepal Length (cm)", min_value=4.0, max_value=8.0, value=5.8, step=0.1)
    sepal_width = st.slider("Sepal Width (cm)", min_value=2.0, max_value=4.5, value=3.0, step=0.1)
    petal_length = st.slider("Petal Length (cm)", min_value=1.0, max_value=7.0, value=3.8, step=0.1)
    petal_width = st.slider("Petal Width (cm)", min_value=0.1, max_value=2.5, value=1.2, step=0.1)

    st.write("")
    predict_btn = st.button("⚡ EXECUTE PREDICTION", type="primary", use_container_width=True)

    st.markdown("""
        <div style="margin-top: 30px; padding: 14px; background: rgba(15, 23, 42, 0.6); border: 1px solid rgba(255,255,255,0.06); border-radius: 8px;">
            <div style="font-size: 11px; color: #94a3b8; font-family: 'Chakra Petch', sans-serif; letter-spacing: 1px;">SYSTEM TELEMETRY</div>
            <div style="display: flex; justify-content: space-between; margin-top: 6px; font-size: 12px;">
                <span style="color: #64748b;">Engine:</span>
                <span style="color: #38bdf8; font-weight: 600;">Random Forest</span>
            </div>
            <div style="display: flex; justify-content: space-between; margin-top: 4px; font-size: 12px;">
                <span style="color: #64748b;">Estimators:</span>
                <span style="color: #f1f5f9; font-weight: 600;">100 Trees</span>
            </div>
            <div style="display: flex; justify-content: space-between; margin-top: 4px; font-size: 12px;">
                <span style="color: #64748b;">System Status:</span>
                <span style="color: #10b981; font-weight: 600;">● ONLINE</span>
            </div>
        </div>
    """, unsafe_allow_html=True)

# ==============================================================================
# 4. MAIN INTERFACE HEADER & HUD STATUS
# ==============================================================================
# Title Section
col_title, col_badge = st.columns([3, 1])
with col_title:
    st.markdown('<div class="system-title">🌼 IRIS INTELLIGENCE // ML CLASSIFIER</div>', unsafe_allow_html=True)
    st.markdown('<div class="system-subtitle">HIGH-PRECISION BOTANICAL TAXONOMY RECOGNITION SYSTEM</div>', unsafe_allow_html=True)

with col_badge:
    st.markdown("""
        <div style="text-align: right; margin-top: 8px;">
            <span style="background: rgba(16, 185, 129, 0.12); color: #10b981; border: 1px solid rgba(16, 185, 129, 0.4); border-radius: 6px; padding: 6px 12px; font-family: 'Chakra Petch', monospace; font-size: 12px; font-weight: 700; letter-spacing: 1px;">
                ● RADAR ACTIVE
            </span>
        </div>
    """, unsafe_allow_html=True)

st.write("")

# ML Calculation
input_values = [sepal_length, sepal_width, petal_length, petal_width]
input_array = np.array([input_values])

prediction = model.predict(input_array)[0]
predicted_species = class_names[prediction]

if hasattr(model, "predict_proba"):
    probabilities = model.predict_proba(input_array)[0]
else:
    probabilities = [0.0, 0.0, 0.0]
    probabilities[prediction] = 1.0

confidence = probabilities[prediction] * 100

# Top KPI Metric Strip
kpi1, kpi2, kpi3, kpi4 = st.columns(4)
with kpi1:
    st.markdown(f"""
        <div class="hud-card hud-card-accent">
            <div style="font-size: 11px; color: #64748b; font-family: 'Chakra Petch', sans-serif; letter-spacing: 1px;">TARGET LOCK</div>
            <div style="font-size: 20px; font-weight: 700; color: #f8fafc; font-family: 'Chakra Petch', sans-serif;">{predicted_species}</div>
        </div>
    """, unsafe_allow_html=True)
with kpi2:
    st.markdown(f"""
        <div class="hud-card hud-card-accent">
            <div style="font-size: 11px; color: #64748b; font-family: 'Chakra Petch', sans-serif; letter-spacing: 1px;">CONFIDENCE INDEX</div>
            <div style="font-size: 20px; font-weight: 700; color: #10b981; font-family: 'Chakra Petch', sans-serif;">{confidence:.1f}%</div>
        </div>
    """, unsafe_allow_html=True)
with kpi3:
    st.markdown(f"""
        <div class="hud-card hud-card-accent">
            <div style="font-size: 11px; color: #64748b; font-family: 'Chakra Petch', sans-serif; letter-spacing: 1px;">PETAL RATIO</div>
            <div style="font-size: 20px; font-weight: 700; color: #38bdf8; font-family: 'Chakra Petch', sans-serif;">{(petal_length/petal_width):.2f}x</div>
        </div>
    """, unsafe_allow_html=True)
with kpi4:
    st.markdown(f"""
        <div class="hud-card hud-card-accent">
            <div style="font-size: 11px; color: #64748b; font-family: 'Chakra Petch', sans-serif; letter-spacing: 1px;">MODEL ARCHITECTURE</div>
            <div style="font-size: 20px; font-weight: 700; color: #f59e0b; font-family: 'Chakra Petch', sans-serif;">RF-100 CORE</div>
        </div>
    """, unsafe_allow_html=True)

# ==============================================================================
# 5. CORE DUAL-PANEL DISPLAY (ตามดีไซน์ของอาจารย์: 2 คอลัมน์)
# ==============================================================================
col1, col2 = st.columns([1, 1], gap="large")

# ----------------- COLUMN 1: INPUT VISUALIZATION -----------------
with col1:
    st.markdown("""
        <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 8px;">
            <div style="font-family: 'Chakra Petch', sans-serif; font-size: 20px; font-weight: 700; color: #f8fafc;">
                📊 TELEMETRY ANALYSIS
            </div>
            <span style="font-size: 12px; color: #38bdf8; font-family: 'Chakra Petch', sans-serif;">SPECIMEN VS AVERAGE</span>
        </div>
    """, unsafe_allow_html=True)
    st.caption("Direct telemetry comparison between live specimen input and dataset baseline benchmarks.")

    fig_input = go.Figure()
    
    # Trace 1: Live Input (Electric Cyan)
    fig_input.add_trace(go.Bar(
        x=feature_names,
        y=input_values,
        name='Specimen Input',
        marker=dict(
            color='#00F2FE',
            line=dict(color='#38BDF8', width=1.5)
        ),
        text=[f"{v:.1f} cm" for v in input_values],
        textposition='outside',
        textfont=dict(color='#00F2FE', family='Chakra Petch', size=12)
    ))
    
    # Trace 2: Dataset Baseline Average (Titanium Silver / Slate)
    fig_input.add_trace(go.Bar(
        x=feature_names,
        y=dataset_averages,
        name='Baseline Mean',
        marker=dict(
            color='#334155',
            line=dict(color='#64748B', width=1.5)
        ),
        text=[f"{v:.2f} cm" for v in dataset_averages],
        textposition='outside',
        textfont=dict(color='#94A3B8', family='Chakra Petch', size=12)
    ))

    fig_input.update_layout(
        template='plotly_dark',
        paper_bgcolor='rgba(15, 23, 42, 0.4)',
        plot_bgcolor='rgba(15, 23, 42, 0.4)',
        barmode='group',
        height=390,
        margin=dict(l=20, r=20, t=30, b=20),
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.03,
            xanchor="right",
            x=1,
            font=dict(color='#cbd5e1', family='Inter', size=12)
        ),
        xaxis=dict(
            showgrid=False,
            tickfont=dict(color='#cbd5e1', family='Inter', size=12)
        ),
        yaxis=dict(
            showgrid=True,
            gridcolor='rgba(255, 255, 255, 0.06)',
            tickfont=dict(color='#64748b'),
            title=dict(text='Dimensions (cm)', font=dict(color='#94a3b8', size=12))
        )
    )
    st.plotly_chart(fig_input, use_container_width=True)

# ----------------- COLUMN 2: PREDICTION & PROBABILITY -----------------
with col2:
    st.markdown("""
        <div style="font-family: 'Chakra Petch', sans-serif; font-size: 20px; font-weight: 700; color: #f8fafc; margin-bottom: 8px;">
            🎯 PREDICTION RESULT
        </div>
    """, unsafe_allow_html=True)

    # Masculine Carbon/HUD Result Card
    card_html = f"""
    <div class="prediction-card">
        <div class="prediction-badge">🌼 TARGET IDENTIFIED</div>
        <div class="prediction-title">{predicted_species}</div>
        <div class="confidence-tag">
            MATCH PROBABILITY: <span class="confidence-value">{confidence:.1f}%</span>
        </div>
    </div>
    """
    st.markdown(card_html, unsafe_allow_html=True)

    # Probability Distribution Subheader
    st.markdown("""
        <div style="font-family: 'Chakra Petch', sans-serif; font-size: 16px; font-weight: 700; color: #cbd5e1; margin-top: 15px; margin-bottom: 6px;">
            ⚡ PROBABILITY SPECTRUM
        </div>
    """, unsafe_allow_html=True)

    # Dynamic styling for probabilities: Highlight winner in Tactical Emerald, others in sleek dark slate
    bar_colors = [
        '#10B981' if i == prediction else '#1e293b'
        for i in range(len(class_names))
    ]
    bar_border_colors = [
        '#34d399' if i == prediction else '#334155'
        for i in range(len(class_names))
    ]
    text_colors = [
        '#34d399' if i == prediction else '#64748b'
        for i in range(len(class_names))
    ]

    fig_prob = go.Figure()
    fig_prob.add_trace(go.Bar(
        x=class_names,
        y=probabilities * 100,
        marker=dict(
            color=bar_colors,
            line=dict(color=bar_border_colors, width=1.5)
        ),
        text=[f"{p*100:.1f}%" for p in probabilities],
        textposition='outside',
        textfont=dict(color=text_colors, family='Chakra Petch', size=13, weight='bold')
    ))

    fig_prob.update_layout(
        template='plotly_dark',
        paper_bgcolor='rgba(15, 23, 42, 0.4)',
        plot_bgcolor='rgba(15, 23, 42, 0.4)',
        yaxis=dict(
            title=dict(text='Confidence (%)', font=dict(color='#94a3b8', size=12)),
            range=[0, 115],
            showgrid=True,
            gridcolor='rgba(255, 255, 255, 0.06)',
            tickfont=dict(color='#64748b')
        ),
        xaxis=dict(
            showgrid=False,
            tickfont=dict(color='#cbd5e1', family='Inter', size=12)
        ),
        height=270,
        margin=dict(l=20, r=20, t=25, b=20)
    )
    st.plotly_chart(fig_prob, use_container_width=True)

# Footer tag
st.markdown("""
    <div style="text-align: center; margin-top: 40px; padding: 15px 0; border-top: 1px solid rgba(255,255,255,0.06); font-size: 12px; color: #475569; font-family: 'Chakra Petch', sans-serif; letter-spacing: 1px;">
        🌼 IRIS TACTICAL LABS // POWERED BY SCIKIT-LEARN & STREAMLIT
    </div>
""", unsafe_allow_html=True)
