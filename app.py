import streamlit as st
import pandas as pd
import base64

# --- 1. SESSION STATE FOR NAVIGATION ---
if "page" not in st.session_state:
    st.session_state.page = "login"

# --- 2. THEME & CSS (Pixel Perfect to Screenshots) ---
def apply_custom_styles():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap');
    
    /* Ensure all text is visible and follows branding */
    html, body, [class*="st-"] {
        font-family: 'Plus Jakarta Sans', sans-serif;
        background-color: #ffffff !important;
        color: #111111 !important;
    }

    /* Landing Page Search Bar (Blue Glow - Screenshot 2) */
    div[data-baseweb="input"] {
        border-radius: 50px !important;
        border: 2px solid #3b82f6 !important;
        background-color: white !important;
        box-shadow: 0 4px 20px rgba(59, 130, 246, 0.15) !important;
    }
    input { color: #111111 !important; }

    /* Result Card (Yellow Accent - Screenshot 3) */
    .result-card {
        border: 1px solid #f0f0f0;
        border-radius: 12px;
        padding: 25px;
        margin-bottom: 20px;
        border-left: 6px solid #fbbf24;
        background: white;
    }
    .patent-title { color: #fbbf24 !important; font-size: 22px; font-weight: 700; text-decoration: none; }
    
    /* Obsidian Header (Screenshot 4) */
    .obsidian-header {
        background: #000000 !important;
        color: #ffffff !important;
        padding: 40px;
        border-radius: 12px 12px 0 0;
    }
    .obsidian-header h1 { color: #ffffff !important; }

    /* Info Grid (Screenshot 5) */
    .info-grid {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 15px;
        padding: 20px;
        background: #f9fafb;
        border-radius: 0 0 12px 12px;
        border: 1px solid #eee;
    }
    .field-label { color: #9ca3af !important; font-size: 11px; font-weight: 700; text-transform: uppercase; }
    .field-value { color: #111111 !important; font-size: 14px; font-weight: 600; }
    
    /* Login Box */
    .login-container {
        max-width: 400px;
        margin: 100px auto;
        padding: 40px;
        text-align: center;
        border: 1px solid #eee;
        border-radius: 15px;
    }
    </style>
    """, unsafe_allow_html=True)

# Helper to load logo
def get_base64_logo():
    try:
        with open("logo.jpeg", "rb") as f:
            return base64.b64encode(f.read()).decode()
    except: return ""

# --- 3. PAGE: LOGIN ---
def show_login():
    logo_b64 = get_base64_logo()
    st.markdown(f'<div class="login-container"><img src="data:image/jpeg;base64,{logo_b64}" width="120"><h2>Access Portal</h2></div>', unsafe_allow_html=True)
    
    # Custom CSS to fix invisible input text in login
    pwd = st.text_input("Enter Key", type="password", placeholder="Password", label_visibility="collapsed")
    if st.button("Unlock System", use_container_width=True):
        if pwd == "Archistratego2026":
            st.session_state.page = "landing"
            st.rerun()

# --- 4. PAGE: LANDING & SEARCH ---
def show_portal():
    logo_b64 = get_base64_logo()
    
    # Hero Branding (Matches Screenshot 2)
    st.markdown(f"""
    <div style="text-align:center; padding-top:60px;">
        <img src="data:image/jpeg;base64,{logo_b64}" width="150">
        <h1 style="font-size:54px; font-weight:800; margin-top:10px;">ARCHISTRATEGOS</h1>
        <p style="color:#888;">UAE Ministry of Economy Official IP Portal</p>
    </div>
    """, unsafe_allow_html=True)

    _, mid, _ = st.columns([1, 5, 1])
    with mid:
        query = st.text_input("", placeholder="Search by patent number, title, or keyword...", label_visibility="collapsed")
        
        # 11 Filters (As requested for the search section)
        with st.expander("⚙️ ADVANCED MOE SEARCH FILTERS (11 SPECIFICATIONS)"):
            c1, c2, c3 = st.columns(3)
            f_app_no = c1.text_input("Application Number")
            f_title = c1.text_input("Patent Title")
            f_type = c1.selectbox("Application Type", ["All", "1. PCT National Entry", "2. Divisional", "3. Conversion", "4. Normal w/ Priority", "5. Normal w/o Priority"])
            f_owner = c2.text_input("Applicant / Owner")
            f_agent = c2.text_input("Legal Agent")
            f_date = c2.date_input("Filing Date", value=None)
            f_p_country = c3.text_input("Priority Country")
            f_p_no = c3.text_input("Priority Number")
            f_p_date = c3.date_input("Priority Date", value=None)
            f_e_priority = st.date_input("Earliest Priority Date", value=None)
            f_abstract = st.text_input("Keywords in Abstract")

        # Sorting Options
        sort_by = st.selectbox("Sort Results By:", ["Application Date", "Earliest Priority Date", "Title (A-Z)"])

    if query or f_app_no:
        # Result Card (Matches Screenshot 3)
        st.markdown(f"""
        <div class="result-card">
            <span style="background:#fef3c7; color:#92400e; padding:4px 10px; border-radius:6px; font-size:11px; font-weight:700;">Utility Patent</span>
            <span style="float:right; color:#9ca3af; font-size:13px;">AE20223145</span>
            <div class="patent-title">The MEGNATICAL Engine</div>
            <div style="margin-top:10px; font-size:14px;">👤 <b>Owner:</b> Innovative Power Systems LTD &nbsp;&nbsp; 📅 <b>Filed:</b> Jun 15, 2023</div>
        </div>
        """, unsafe_allow_html=True)

        # Detailed Grid (Matches Screenshot 5/Code)
        with st.expander("Full Patent Specifications"):
            st.markdown("""
            <div class="obsidian-header">
                <span style="background:#fbbf24; color:black; padding:4px 10px; border-radius:4px; font-size:10px; font-weight:800;">OFFICIAL RECORD</span>
                <h1>The MEGNATICAL Engine</h1>
            </div>
            <div class="info-grid">
                <div><span class="field-label">Applicant / Owner</span><br><span class="field-value">Innovative Power Systems LTD</span></div>
                <div><span class="field-label">Legal Agent</span><br><span class="field-value">Emily Smith (Future Patents)</span></div>
                <div><span class="field-label">Application Type</span><br><span class="field-value">4. Normal Application with Priority</span></div>
                <div><span class="field-label">Filing Date</span><br><span class="field-value">2023-06-15</span></div>
                <div><span class="field-label">Priority Data</span><br><span class="field-value">UK | #UK-9912 | 2023-01-10</span></div>
                <div><span class="field-label">Earliest Priority</span><br><span class="field-value">2023-01-10</span></div>
            </div>
            """, unsafe_allow_html=True)

# --- 5. EXECUTION ---
apply_custom_styles()
if st.session_state.page == "login":
    show_login()
else:
    show_portal()
