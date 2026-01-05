import streamlit as st
import pandas as pd
import base64

# --- 1. SYSTEM CONFIG & AUTH ---
st.set_page_config(page_title="ARCHISTRATEGOS", layout="wide", initial_sidebar_state="collapsed")

if "auth" not in st.session_state:
    st.session_state.auth = False

# --- 2. PIXEL-PERFECT CSS (VISIBLE BRANDING) ---
def apply_styles():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;700;800&display=swap');
    
    /* Force high-contrast visibility for all text */
    html, body, [class*="st-"] {
        font-family: 'Plus Jakarta Sans', sans-serif;
        background-color: white !important;
        color: #000000 !important;
    }

    /* Landing Search Bar (Screenshot 2) */
    div[data-baseweb="input"] {
        border-radius: 50px !important;
        border: 2px solid #3b82f6 !important;
        background-color: white !important;
        box-shadow: 0 4px 20px rgba(59, 130, 246, 0.15) !important;
    }

    /* Result Card (Screenshot 3) */
    .result-card {
        border: 1px solid #e0e0e0; border-radius: 12px; padding: 25px;
        margin-bottom: 20px; border-left: 8px solid #fbbf24;
        background: white; color: #000000 !important;
    }
    .patent-link { color: #fbbf24 !important; font-size: 22px; font-weight: 700; text-decoration: none; }
    
    /* Obsidian Detail Header (Screenshot 4) */
    .obsidian-header {
        background: #000000 !important; color: #ffffff !important;
        padding: 40px; border-radius: 12px 12px 0 0;
    }
    .obsidian-header h1 { color: #ffffff !important; margin: 0; }

    /* The 11-Field Grid (Screenshot 5) */
    .info-grid {
        display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
        gap: 1px; background: #eee; border: 1px solid #eee;
    }
    .info-item {
        background: white; padding: 20px;
    }
    .field-label { color: #888888 !important; font-size: 11px; font-weight: 700; text-transform: uppercase; }
    .field-value { color: #000000 !important; font-size: 15px; font-weight: 600; margin-top: 5px; display: block; }
    
    /* Filter Visibility */
    label { color: #000000 !important; font-weight: 600 !important; }
    </style>
    """, unsafe_allow_html=True)

# Helper to load logo
def get_logo():
    try:
        with open("logo.jpeg", "rb") as f:
            return base64.b64encode(f.read()).decode()
    except: return ""

# --- 3. PAGE LOGIC ---
apply_styles()
logo_b64 = get_logo()

if not st.session_state.auth:
    # --- LOGIN PAGE ---
    _, col, _ = st.columns([1,1,1])
    with col:
        st.markdown(f'<div style="text-align:center; margin-top:100px;"><img src="data:image/jpeg;base64,{logo_b64}" width="150"></div>', unsafe_allow_html=True)
        pwd = st.text_input("ACCESS KEY", type="password")
        if st.button("UNLOCK PLATFORM", use_container_width=True):
            if pwd == "Archistratego2026":
                st.session_state.auth = True
                st.rerun()
else:
    # --- LANDING PAGE ---
    st.markdown(f"""
    <div style="text-align:center; padding-top:40px;">
        <img src="data:image/jpeg;base64,{logo_b64}" width="120">
        <h1 style="font-size:50px; font-weight:800; margin:10px 0;">ARCHISTRATEGOS</h1>
        <p style="color:#555; font-size:18px;">UAE Ministry of Economy Official IP Portal</p>
    </div>
    """, unsafe_allow_html=True)

    # --- ADVANCED SEARCH (THE 11 FIELDS) ---
    _, mid, _ = st.columns([1, 6, 1])
    with mid:
        main_q = st.text_input("", placeholder="Quick Search...", label_visibility="collapsed")
        
        with st.expander("⚙️ ADVANCED MOE SEARCH FILTERS (11 SPECIFICATIONS)"):
            c1, c2, c3 = st.columns(3)
            f_app_no = c1.text_input("1. Application Number")
            f_title = c1.text_input("2. Patent Title")
            f_abstract = c1.text_input("3. Abstract Keywords")
            
            f_owner = c2.text_input("4. Owner / Applicant")
            f_agent = c2.text_input("5. Agent Details")
            f_app_date = c2.text_input("6. Application Date (YYYY-MM-DD)")
            
            f_p_country = c3.text_input("7. Priority Country")
            f_p_no = c3.text_input("8. Priority Number")
            f_p_date = c3.text_input("9. Priority Date (YYYY-MM-DD)")
            
            f_e_priority = st.text_input("10. Earliest Priority Date")
            f_app_type = st.selectbox("11. Application Type", ["All", "1. PCT National Entry", "2. Divisional", "3. Conversion", "4. Normal w/ Priority", "5. Normal w/o Priority"])

        sort_by = st.selectbox("Sort Results By:", ["Application Date", "Earliest Priority Date", "Title (A-Z)"])

    # --- RESULTS (ACCURATE DATA MAPPING) ---
    if main_q or f_app_no or f_owner:
        # Results display logic
        st.markdown(f"### Found 1 Result")
        
        # Result Card
        st.markdown(f"""
        <div class="result-card">
            <span style="background:#fef3c7; color:#92400e; padding:4px 10px; border-radius:6px; font-size:11px; font-weight:700;">Utility Patent</span>
            <span style="float:right; color:#888;">AE20223145</span>
            <div class="patent-link">The MEGNATICAL Engine</div>
            <div style="margin-top:10px; color:#333;">👤 <b>Owner:</b> Innovative Power Systems LTD &nbsp;&nbsp; 📅 <b>Filed:</b> 2023-06-15</div>
        </div>
        """, unsafe_allow_html=True)

        # Full 11-Field Grid (Screenshot 5)
        with st.expander("VIEW OFFICIAL 11-FIELD SPECIFICATIONS"):
            st.markdown(f"""
            <div class="obsidian-header">
                <span style="background:#fbbf24; color:black; padding:4px 10px; border-radius:4px; font-size:10px; font-weight:800;">OFFICIAL DATA</span>
                <h1>The MEGNATICAL Engine</h1>
            </div>
            <div class="info-grid">
                <div class="info-item"><span class="field-label">1. Application Number</span><span class="field-value">AE20223145</span></div>
                <div class="info-item"><span class="field-label">2. Patent Title</span><span class="field-value">The MEGNATICAL Engine</span></div>
                <div class="info-item"><span class="field-label">3. Abstract</span><span class="field-value">A magnetic-driven propulsion system...</span></div>
                <div class="info-item"><span class="field-label">4. Owner / Applicant</span><span class="field-value">Innovative Power Systems LTD</span></div>
                <div class="info-item"><span class="field-label">5. Agent Details</span><span class="field-value">Emily Smith (Future Patents)</span></div>
                <div class="info-item"><span class="field-label">6. Application Date</span><span class="field-value">2023-06-15</span></div>
                <div class="info-item"><span class="field-label">7. Priority Country</span><span class="field-value">United Kingdom</span></div>
                <div class="info-item"><span class="field-label">8. Priority Number</span><span class="field-value">UK-9912-B</span></div>
                <div class="info-item"><span class="field-label">9. Priority Date</span><span class="field-value">2023-01-10</span></div>
                <div class="info-item"><span class="field-label">10. Earliest Priority Date</span><span class="field-value">2023-01-10</span></div>
                <div class="info-item"><span class="field-label">11. Application Type</span><span class="field-value">4. Normal Application with Priority</span></div>
            </div>
            """, unsafe_allow_html=True)
