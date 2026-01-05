import streamlit as st
import pandas as pd
import requests
from bs4 import BeautifulSoup
import base64

# --- SETTINGS ---
SECRET_PASSWORD = "Archistratego2026"
MOE_URL = "https://eservices.moec.gov.ae/patent/IPDLListingPatent"

st.set_page_config(page_title="ARCHISTRATEGOS", layout="wide", initial_sidebar_state="collapsed")

# --- UI ENGINE: PIXEL PERFECT RECONSTRUCTION ---
def apply_theme():
    with open("logo.jpeg", "rb") as f:
        img_b64 = base64.b64encode(f.read()).decode()

    st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    html, body, [class*="st-"] {{ font-family: 'Inter', sans-serif; background-color: #ffffff; }}

    /* 1. Landing Page (Screenshot 1) */
    .hero {{ text-align: center; padding: 80px 0 30px 0; }}
    .brand-title {{ font-size: 58px; font-weight: 800; letter-spacing: -2px; color: #1a1a1a; margin: 10px 0; }}
    .brand-sub {{ color: #777; font-size: 16px; margin-bottom: 40px; max-width: 600px; margin-left: auto; margin-right: auto; }}
    
    /* Glowing Rounded Search Bar */
    div[data-baseweb="input"] {{
        border-radius: 50px !important;
        border: 2px solid #3b82f6 !important; /* Blue glow from screenshot */
        padding: 10px 30px !important;
        box-shadow: 0 4px 20px rgba(59, 130, 246, 0.15) !important;
    }}

    /* 2. Result Cards (Screenshot 2) */
    .result-card {{
        border: 1px solid #e5e7eb; border-radius: 12px; padding: 30px;
        margin-bottom: 25px; border-left: 6px solid #fbbf24; /* Yellow accent line */
        background: white; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);
    }}
    .type-badge {{
        background: #fef3c7; color: #92400e; padding: 4px 12px;
        border-radius: 50px; font-size: 11px; font-weight: 700; margin-bottom: 15px; display: inline-block;
    }}
    .patent-title-link {{ color: #fbbf24; font-size: 22px; font-weight: 700; text-decoration: none; }}
    .meta-item {{ font-size: 14px; color: #4b5563; display: flex; align-items: center; gap: 8px; margin-top: 10px; }}

    /* 3. Detail View (Screenshot 3) */
    .detail-header {{
        background: #000; color: white; padding: 40px;
        border-radius: 12px 12px 0 0; margin-top: 20px;
    }}
    .detail-body {{
        border: 1px solid #eee; border-top: none; padding: 40px;
        border-radius: 0 0 12px 12px; background: white;
    }}
    .info-grid {{
        display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin-top: 30px;
    }}
    .label {{ font-size: 11px; color: #9ca3af; text-transform: uppercase; font-weight: 700; }}
    .value {{ font-size: 15px; color: #1f2937; font-weight: 600; }}

    /* Result Counter */
    .counter-pill {{
        background: #f3f4f6; padding: 5px 15px; border-radius: 50px;
        font-size: 13px; color: #6b7280; float: right;
    }}
    </style>
    """, unsafe_allow_html=True)

# --- SCRAPER ENGINE: LIVE MOE CONNECTION ---
def fetch_moe_data(query):
    # This simulates the live POST request to the MOE portal
    # In production, use: requests.post(MOE_URL, data={'ApplicationNumber': query})
    return [{
        "id": "AE20223145",
        "title": "The MEGNATICAL Engine",
        "owner": "Innovative Power Systems LTD",
        "date": "Jun 15, 2023",
        "type": "Utility Patent",
        "abstract": "A novel engine system that utilizes magnetic properties to generate mechanical motion for energy-efficient applications...",
        "agent": "Emily Smith (Future Patents Consultancy)",
        "priority": "UK | #UK-9912 | 2023-01-10"
    }]

# --- ROUTING & UI ---
apply_theme()

if "auth" not in st.session_state: st.session_state.auth = False

if not st.session_state.auth:
    # Minimalist Login
    _, col, _ = st.columns([1,1.2,1])
    with col:
        st.markdown("<div style='height:100px'></div>", unsafe_allow_html=True)
        st.image("logo.jpeg", use_container_width=True)
        pwd = st.text_input("ACCESS KEY", type="password")
        if st.button("UNLOCK PLATFORM", use_container_width=True):
            if pwd == SECRET_PASSWORD:
                st.session_state.auth = True
                st.rerun()
else:
    # 1. LANDING (SCREENSHOT 1)
    st.markdown("""
    <div class="hero">
        <div class="brand-title">ARCHISTRATEGOS</div>
        <div class="brand-sub">UAE Patent Search Platform. Precision intelligence for intellectual property.</div>
    </div>
    """, unsafe_allow_html=True)

    _, mid, _ = st.columns([1, 4, 1])
    with mid:
        search_query = st.text_input("", placeholder="Search anything (Application #, Title, Owner, Agent...)", label_visibility="collapsed")
        
    if search_query:
        results = fetch_moe_data(search_query)
        
        # 2. SEARCH RESULTS (SCREENSHOT 2)
        st.markdown(f"### Results for \"{search_query}\" <span class='counter-pill'>{len(results)} patents found</span>", unsafe_allow_html=True)
        
        for r in results:
            st.markdown(f"""
            <div class="result-card">
                <div class="type-badge">Type {r['type']}: Unknown</div>
                <div style="float:right; color:#9ca3af; font-size:14px;">{r['id']}</div>
                <div class="patent-title-link">{r['title']}</div>
                <div class="meta-item">👤 <b>Owner:</b> {r['owner']} &nbsp;&nbsp;&nbsp; 📅 <b>Filed:</b> {r['date']}</div>
                <p style="margin-top:20px; color:#4b5563; font-size:15px; background:#f9fafb; padding:15px; border-radius:8px;">{r['abstract']}</p>
                <div style="text-align:right; color:#fbbf24; font-weight:700; font-size:14px; cursor:pointer;">Full Patent Details →</div>
            </div>
            """, unsafe_allow_html=True)

            # 3. DETAIL VIEW (SCREENSHOT 3)
            with st.expander("Expand Official MOE Detail View"):
                st.markdown(f"""
                <div class="detail-header">
                    <span class="type-badge" style="background:#fbbf24; color:black;">UTILITY PATENT</span>
                    <span style="margin-left:15px; opacity:0.7;">{r['id']}</span>
                    <h1 style="margin-top:10px;">{r['title']}</h1>
                    <p>📅 Filed: {r['date']}</p>
                </div>
                <div class="detail-body">
                    <h3>Abstract</h3>
                    <p style="color:#4b5563;">{r['abstract']}</p>
                    <hr>
                    <div class="info-grid">
                        <div><div class="label">Application Number</div><div class="value">{r['id']}</div></div>
                        <div><div class="label">Ownership</div><div class="value">{r['owner']}</div></div>
                        <div><div class="label">Legal Agent</div><div class="value">{r['agent']}</div></div>
                        <div><div class="label">Priority Data</div><div class="value">{r['priority']}</div></div>
                    </div>
                </div>
                """, unsafe_allow_html=True)
