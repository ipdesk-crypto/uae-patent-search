import streamlit as st
import pandas as pd
import base64

# --- 1. SETTINGS & AUTH ---
SECRET_PASSWORD = "Archistratego2026"

st.set_page_config(page_title="ARCHISTRATEGO", layout="wide", initial_sidebar_state="collapsed")

def apply_executive_ui():
    # Convert logo to base64 for cleaner HTML injection
    with open("logo.jpeg", "rb") as f:
        img_b64 = base64.b64encode(f.read()).decode()

    st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    html, body, [class*="st-"] {{
        font-family: 'Inter', sans-serif;
        background-color: #ffffff;
    }}

    /* Landing Hero Section */
    .hero-box {{
        text-align: center;
        padding: 60px 0 20px 0;
    }}
    .brand-title {{
        font-size: 52px;
        font-weight: 800;
        letter-spacing: -2px;
        color: #111;
        margin-bottom: 0;
    }}
    .brand-sub {{
        color: #888;
        font-size: 14px;
        margin-bottom: 40px;
    }}

    /* The Floating Search Bar (Google Style) */
    div[data-baseweb="input"] {{
        border-radius: 50px !important;
        border: 1px solid #dfe1e5 !important;
        padding: 8px 25px !important;
        box-shadow: 0 2px 10px rgba(0,0,0,0.05) !important;
        transition: 0.3s;
    }}
    div[data-baseweb="input"]:focus-within {{
        box-shadow: 0 4px 20px rgba(0,0,0,0.12) !important;
    }}

    /* Gold Status Pills */
    .pill-container {{
        display: flex;
        justify-content: center;
        gap: 15px;
        margin-top: 25px;
    }}
    .status-pill {{
        background: #f8f9fa;
        border: 1px solid #eee;
        padding: 6px 18px;
        border-radius: 50px;
        font-size: 12px;
        color: #666;
        display: flex;
        align-items: center;
        gap: 8px;
    }}
    .gold-dot {{ color: #FFB800; font-weight: bold; }}

    /* Result Card - MOE Professional Style */
    .patent-header-box {{
        background: #000;
        color: white;
        padding: 25px 35px;
        border-radius: 12px 12px 0 0;
        margin-top: 40px;
    }}
    .patent-type-badge {{
        background: #FFB800;
        color: black;
        padding: 3px 12px;
        border-radius: 4px;
        font-size: 11px;
        font-weight: 700;
        margin-bottom: 10px;
        display: inline-block;
    }}
    .patent-body-box {{
        border: 1px solid #eee;
        border-top: none;
        padding: 35px;
        border-radius: 0 0 12px 12px;
        background: white;
        box-shadow: 0 10px 30px rgba(0,0,0,0.03);
    }}

    /* Info Grid Layout */
    .info-grid {{
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 30px;
        margin-top: 30px;
    }}
    .info-item {{
        background: #fcfcfc;
        border: 1px solid #f1f1f1;
        padding: 15px 20px;
        border-radius: 10px;
    }}
    .info-label {{
        font-size: 10px;
        color: #aaa;
        text-transform: uppercase;
        font-weight: 700;
        letter-spacing: 1px;
    }}
    .info-val {{
        font-size: 14px;
        color: #222;
        font-weight: 600;
        margin-top: 4px;
    }}

    /* Hide Streamlit default branding */
    #MainMenu {{visibility: hidden;}}
    footer {{visibility: hidden;}}
    </style>
    """, unsafe_allow_html=True)

# --- 2. APP LOGIC ---
if "auth" not in st.session_state: st.session_state.auth = False

if not st.session_state.auth:
    # --- LOGIN PAGE ---
    _, col, _ = st.columns([1,1,1])
    with col:
        st.markdown("<br><br><br>", unsafe_allow_html=True)
        st.image("logo.jpeg", width=180)
        st.markdown("<h3 style='text-align:center;'>Executive Access</h3>", unsafe_allow_html=True)
        pwd = st.text_input("PASSWORD", type="password", label_visibility="collapsed")
        if st.button("UNLOCK SYSTEM", use_container_width=True):
            if pwd == SECRET_PASSWORD:
                st.session_state.auth = True
                st.rerun()
else:
    # --- SEARCH INTERFACE ---
    apply_executive_ui()
    
    st.markdown(f"""
    <div class="hero-box">
        <img src="data:image/jpeg;base64,{base64.b64encode(open("logo.jpeg", "rb").read()).decode()}" width="80" style="margin-bottom:20px;">
        <div class="brand-title">ARCHISTRATEGOS</div>
        <div class="brand-sub">UAE Patent Search Platform. Precision intelligence for intellectual property.</div>
    </div>
    """, unsafe_allow_html=True)

    # Universal Search Bar
    _, mid, _ = st.columns([1, 4, 1])
    with mid:
        q = st.text_input("", placeholder="Search by patent number, title, or keyword...", label_visibility="collapsed")
        
        # Pills
        st.markdown("""
        <div class="pill-container">
            <div class="status-pill"><span class="gold-dot">●</span> 50,000+ Records</div>
            <div class="status-pill"><span class="gold-dot">●</span> UAE Registry</div>
            <div class="status-pill"><span class="gold-dot">●</span> Official Data</div>
        </div>
        """, unsafe_allow_html=True)

    # MOE Style Advanced Filters
    with st.expander("Advanced MOE Registry Search Fields"):
        c1, c2, c3 = st.columns(3)
        app_no = c1.text_input("Application Number (e.g. P/36/2026/...)")
        owner = c1.text_input("Owner / Applicant Name")
        agent = c2.text_input("Agent Firm / Name")
        app_type = c2.selectbox("Application Type", ["All", "1. PCT National Entry", "2. Divisional", "3. Conversion", "4. Normal w/ Priority", "5. Normal w/o Priority"])
        date_from = c3.date_input("Filed From", value=None)
        priority_country = c3.text_input("Priority Country")

    if q or app_no:
        # Results Header
        st.markdown("<br><br><p style='color:#888; font-size:14px;'>About 1 results found in MOEC database</p>", unsafe_allow_html=True)
        
        # --- PATENT RESULT CARD ---
        st.markdown("""
        <div class="patent-header-box">
            <div class="patent-type-badge">UTILITY PATENT</div>
            <div style="font-size:12px; opacity:0.7; margin-bottom:5px;">AE20251687</div>
            <div style="font-size:28px; font-weight:700;">Magnetically Driven Engine Utilizing MEGNATICAL Technologies</div>
            <div style="font-size:13px; opacity:0.7; margin-top:10px;">📅 Filed: January 5, 2026</div>
        </div>
        <div class="patent-body-box">
            <p style="color:#444; line-height:1.7; font-size:15px;">
                An engine-based system employing advanced magnetic interactions for high-efficiency output. This invention seeks to incorporate machinery to in-channeling magnetic force to reduce energy consumption.
            </p>
            
            <div style="font-weight:700; margin-top:40px; font-size:18px;">Application Details</div>
            
            <div class="info-grid">
                <div class="info-item">
                    <div class="info-label">Application Number</div>
                    <div class="info-val">P/36/2026/00108</div>
                </div>
                <div class="info-item">
                    <div class="info-label">Ownership</div>
                    <div class="info-val"><b>Tech Dynamics LLC</b><br><span style="color:#888; font-weight:400; font-size:12px;">Future Patents Consultancy</span></div>
                </div>
                <div class="info-item">
                    <div class="info-label">Application Type</div>
                    <div class="info-val">4. Normal Application with Priority</div>
                </div>
                <div class="info-item">
                    <div class="info-label">Agent / Firm</div>
                    <div class="info-val"><b>Emily Smith</b><br><span style="color:#888; font-weight:400; font-size:12px;">Global IP Partners</span></div>
                </div>
                <div class="info-item">
                    <div class="info-label">Priority Data</div>
                    <div class="info-val">United Kingdom | #UK-99201 | 2025-05-12</div>
                </div>
                <div class="info-item">
                    <div class="info-label">Earliest Priority Date</div>
                    <div class="info-val">2025-05-12</div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
