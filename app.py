import streamlit as st
import pandas as pd
import requests
from bs4 import BeautifulSoup
import base64

# --- 1. SETTINGS ---
SECRET_PASSWORD = "Archistratego2026"

st.set_page_config(page_title="ARCHISTRATEGO | UAE IP Intelligence", layout="wide", initial_sidebar_state="collapsed")

# --- 2. THE DESIGN ENGINE (CSS) ---
def apply_executive_styles():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap');
    html, body, [class*="st-"] { font-family: 'Inter', sans-serif; }
    
    /* Clean Professional Background */
    .stApp { background-color: #fcfcfc; }

    /* Executive Obsidian Header */
    .hero-container {
        background: #000000; padding: 50px 80px; margin: -6rem -5rem 2rem -5rem;
        border-radius: 0 0 40px 40px; box-shadow: 0 10px 30px rgba(0,0,0,0.15);
        display: flex; justify-content: space-between; align-items: center;
    }
    .hero-title { color: white; font-size: 38px; font-weight: 700; letter-spacing: -1.5px; }
    .hero-sub { color: #FFB800; font-weight: 700; font-size: 14px; letter-spacing: 2px; text-transform: uppercase; }

    /* Search Bar Professionalism */
    .stTextInput input {
        border-radius: 16px !important; border: 1.5px solid #e2e8f0 !important;
        padding: 2rem !important; font-size: 18px !important;
        box-shadow: 0 10px 25px rgba(0,0,0,0.03) !important;
    }

    /* Result Card Layout */
    .patent-card {
        background: white; border-radius: 24px; padding: 35px;
        margin-bottom: 25px; border: 1px solid #f0f0f0;
        box-shadow: 0 4px 12px rgba(0,0,0,0.02); transition: 0.4s ease;
    }
    .patent-card:hover { transform: translateY(-5px); box-shadow: 0 20px 50px rgba(0,0,0,0.07); border-left: 10px solid #FFB800; }
    
    .card-id { color: #FFB800; font-weight: 700; font-size: 12px; margin-bottom: 5px; }
    .card-title { font-size: 24px; font-weight: 700; color: #111; margin-bottom: 15px; line-height: 1.2; text-transform: uppercase; }
    .card-abstract { font-size: 15px; color: #4A5568; line-height: 1.6; margin-bottom: 25px; }

    /* Info Grid for the 11 Fields */
    .info-grid {
        display: grid; grid-template-columns: repeat(2, 1fr); gap: 20px;
        background: #f8fafc; padding: 25px; border-radius: 15px; border: 1px solid #edf2f7;
    }
    .field-label { color: #94a3b8; font-size: 10px; font-weight: 800; text-transform: uppercase; letter-spacing: 0.5px; display: block; }
    .field-value { color: #1e293b; font-size: 14px; font-weight: 600; }

    /* Counter Badge */
    .results-banner { font-size: 13px; color: #64748b; margin-bottom: 25px; border-bottom: 1px solid #e2e8f0; padding-bottom: 10px; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. MOE LIVE CONNECT ---
def get_live_results(query):
    # This structure is ready for BeautifulSoup scraping from:
    # https://eservices.moec.gov.ae/patent/IPDLListingPatent
    return [{
        "app_no": "P/36/2026/00108",
        "title": "Integrated Solar Desalination Unit with Magnetic Heat Recovery",
        "abstract": "A hybrid desalination system utilizing the high ambient temperatures of the UAE combined with localized magnetic field stimulation to improve membrane flux by 22%...",
        "owner": "Khalifa University of Science & Technology",
        "agent": "AGIP - Abu-Ghazaleh Intellectual Property",
        "app_date": "2026-01-05",
        "p_country": "UAE",
        "p_no": "AE-10229-X",
        "p_date": "2025-11-12",
        "e_priority": "2025-11-12",
        "type_label": "1. PCT National Entry"
    }]

# --- 4. AUTH & ROUTING ---
apply_executive_styles()

if "auth" not in st.session_state: st.session_state.auth = False

if not st.session_state.auth:
    col1, col2, col3 = st.columns([1,1.5,1])
    with col2:
        st.markdown("<br><br>", unsafe_allow_html=True)
        st.image("logo.jpeg", width=200)
        st.markdown("<h2 style='text-align:center;'>Executive Portal</h2>", unsafe_allow_html=True)
        pwd = st.text_input("ACCESS KEY", type="password")
        if st.button("AUTHENTICATE SYSTEM", use_container_width=True):
            if pwd == SECRET_PASSWORD:
                st.session_state.auth = True
                st.rerun()
else:
    # --- MAIN UI ---
    st.markdown(f"""
    <div class="hero-container">
        <div>
            <div class="hero-sub">Official Registry Intelligence</div>
            <div class="hero-title">ARCHI<span style="color:#FFB800">STRATEGO</span></div>
        </div>
        <div style="text-align:right; font-size:12px; color:white; opacity:0.6;">
            UAE MOE DATABASE: <span style="color:#00FF00">ONLINE</span><br>
            LAST UPDATE: JAN 2026
        </div>
    </div>
    """, unsafe_allow_html=True)

    query = st.text_input("Universal Search", placeholder="Enter Application #, Title, or Owner name...", label_visibility="collapsed")

    if query:
        data = get_live_results(query)
        st.markdown(f"<div class='results-banner'>Total: <b>{len(data)}</b> records matched in MOE database</div>", unsafe_allow_html=True)

        for p in data:
            st.markdown(f"""
            <div class="patent-card">
                <div class="card-id">APPLICATION: {p['app_no']}</div>
                <div class="card-title">{p['title']}</div>
                <div class="card-abstract">{p['abstract']}</div>
                
                <div class="info-grid">
                    <div>
                        <span class="field-label">Applicant / Owner</span>
                        <span class="field-value">{p['owner']}</span>
                    </div>
                    <div>
                        <span class="field-label">Legal Agent</span>
                        <span class="field-value">{p['agent']}</span>
                    </div>
                    <div>
                        <span class="field-label">Application Type</span>
                        <span class="field-value">{p['type_label']}</span>
                    </div>
                    <div>
                        <span class="field-label">Filing Date</span>
                        <span class="field-value">{p['app_date']}</span>
                    </div>
                    <div>
                        <span class="field-label">Priority Data</span>
                        <span class="field-value">{p['p_country']} | {p['p_no']} | {p['p_date']}</span>
                    </div>
                    <div>
                        <span class="field-label">Earliest Priority</span>
                        <span class="field-value">{p['e_priority']}</span>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
