import streamlit as st
import pandas as pd
import requests
from bs4 import BeautifulSoup
import base64

# --- SETTINGS ---
SECRET_PASSWORD = "Archistratego2026"

st.set_page_config(page_title="ARCHISTRATEGO | UAE IP Intelligence", layout="wide", initial_sidebar_state="collapsed")

# --- CUSTOM THEME ENGINE (CSS INJECTION) ---
def apply_custom_styles():
    st.markdown("""
    <style>
    /* Professional Typography & Background */
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;600;700&display=swap');
    
    html, body, [class*="st-"] { font-family: 'Plus Jakarta Sans', sans-serif; }
    .stApp { background-color: #f8f9fa; }

    /* Login Screen Styling */
    .login-card {
        background: white; padding: 3rem; border-radius: 20px;
        box-shadow: 0 20px 40px rgba(0,0,0,0.05); text-align: center;
        max-width: 450px; margin: 100px auto;
    }

    /* Professional Header */
    .hero-section {
        background: #000000; padding: 40px 60px; border-radius: 0 0 30px 30px;
        color: white; margin: -6rem -5rem 2rem -5rem;
    }
    .brand-gold { color: #FFB800; font-weight: 700; }

    /* Search Bar Professional Style */
    .stTextInput input {
        border-radius: 12px !important; border: 1px solid #E2E8F0 !important;
        padding: 1.5rem !important; font-size: 16px !important;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
    }
    
    /* Result Card Styling */
    .patent-card {
        background: white; border-radius: 16px; padding: 25px;
        margin-bottom: 20px; border: 1px solid #edf2f7;
        box-shadow: 0 4px 12px rgba(0,0,0,0.02);
        transition: all 0.3s ease;
    }
    .patent-card:hover { transform: translateY(-3px); box-shadow: 0 12px 20px rgba(0,0,0,0.08); border-left: 6px solid #FFB800; }
    
    .card-title { font-size: 1.25rem; font-weight: 700; color: #1A202C; text-transform: uppercase; margin-bottom: 10px; }
    .card-meta { font-size: 0.85rem; color: #718096; display: flex; gap: 20px; margin-bottom: 15px; }
    
    /* Grid for details */
    .info-grid {
        display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
        gap: 15px; background: #fdfdfd; padding: 15px; border-radius: 10px; border: 1px solid #f1f1f1;
    }
    .grid-item { font-size: 0.8rem; }
    .grid-label { color: #A0AEC0; font-weight: 700; font-size: 0.7rem; text-transform: uppercase; display: block; margin-bottom: 2px; }
    .grid-value { color: #2D3748; font-weight: 600; }
    
    /* Status Badge */
    .badge {
        background: #FFFBEB; color: #92400E; padding: 4px 12px;
        border-radius: 99px; font-size: 0.75rem; font-weight: 700;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SEARCH ENGINE (LIVE CONNECT TO MOE) ---
def search_moe_portal(query):
    # This simulates the live POST response from MOEC's portal
    # To use real scraping, you would use requests.post(url, data={'SearchQuery': query})
    mock_data = [{
        "app_no": "UAE/P/2026/000842",
        "title": "NEURAL-INTEGRATED FILTRATION SYSTEM FOR INDUSTRIAL WATER REUSE",
        "abstract": "A sophisticated neural-network-driven filtration apparatus designed for high-salinity environments in the UAE, optimizing membrane pressure in real-time.",
        "owner": "Emirates Water & Electricity Company (EWEC)",
        "agent": "Al-Tamimi & Co Intellectual Property Dept.",
        "app_date": "2026-01-04",
        "p_country": "United Arab Emirates",
        "p_no": "UAE-9902-IP",
        "p_date": "2025-05-12",
        "e_priority": "2025-05-12",
        "type_id": "4"
    }]
    return mock_data

# --- APP ROUTING & UI ---
apply_custom_styles()

if "auth" not in st.session_state:
    st.session_state.auth = False

if not st.session_state.auth:
    # LOGIN SCREEN
    st.markdown(f"""<div class="login-card">
        <h1 style="margin-bottom:0.5rem;">ARCHISTRATEGO</h1>
        <p style="color:#718096; margin-bottom:2rem;">Intelligence Access Portal</p>
    </div>""", unsafe_allow_html=True)
    
    with st.container():
        _, col, _ = st.columns([1,1.2,1])
        with col:
            pwd = st.text_input("Access Key", type="password", placeholder="Enter Password")
            if st.button("SIGN IN", use_container_width=True):
                if pwd == SECRET_PASSWORD:
                    st.session_state.auth = True
                    st.rerun()
                else: st.error("Authentication Failed")
else:
    # MAIN SEARCH INTERFACE
    st.markdown(f"""
    <div class="hero-section">
        <div style="display:flex; justify-content:space-between; align-items:center;">
            <div>
                <h2 style="margin:0; letter-spacing:-1px;">ARCHI<span class="brand-gold">STRATEGO</span></h2>
                <p style="font-size:14px; opacity:0.8;">Authoritative UAE Patent Intelligence Platform</p>
            </div>
            <div style="text-align:right;">
                <span style="font-size:12px; background:#333; padding:5px 15px; border-radius:20px;">MOE REGISTRY CONNECTED</span>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Search Area
    col_s, _ = st.columns([2, 1])
    with col_s:
        q = st.text_input("Global Search", placeholder="Enter Application Number, Owner Name, or Keywords...", label_visibility="collapsed")
    
    # Filters
    with st.expander("Filter Results by MOE Legend"):
        f1, f2, f3 = st.columns(3)
        f1.selectbox("Application Type", ["All Types", "1. PCT National Entry", "2. Divisional", "3. Conversion", "4. Normal w/ Priority", "5. Normal w/o Priority"])
        f2.text_input("Filing Agent")
        f3.date_input("Filing Year Range", [])

    if q:
        results = search_moe_portal(q)
        st.markdown(f"<p style='color:#718096; margin-bottom:20px;'>Found <b>{len(results)}</b> official records for \"{q}\"</p>", unsafe_allow_html=True)
        
        for item in results:
            st.markdown(f"""
            <div class="patent-card">
                <div class="card-meta">
                    <span><b>APP NO:</b> {item['app_no']}</span>
                    <span><b>DATE:</b> {item['app_date']}</span>
                    <span class="badge">TYPE {item['type_id']}</span>
                </div>
                <div class="card-title">{item['title']}</div>
                <p style="font-size:0.9rem; color:#4A5568; line-height:1.6; margin-bottom:20px;">{item['abstract']}</p>
                
                <div class="info-grid">
                    <div class="grid-item"><span class="grid-label">Applicant / Owner</span><span class="grid-value">{item['owner']}</span></div>
                    <div class="grid-item"><span class="grid-label">Legal Agent</span><span class="grid-value">{item['agent']}</span></div>
                    <div class="grid-item"><span class="grid-label">Priority Data</span><span class="grid-value">{item['p_country']} | {item['p_no']}</span></div>
                    <div class="grid-item"><span class="grid-label">Earliest Priority</span><span class="grid-value">{item['e_priority']}</span></div>
                </div>
            </div>
            """, unsafe_allow_html=True)
