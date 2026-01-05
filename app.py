import streamlit as st
import pandas as pd
import base64

# --- SYSTEM CONFIG ---
st.set_page_config(page_title="ARCHISTRATEGOS", layout="wide", initial_sidebar_state="collapsed")

def apply_styles():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap');
    html, body, [class*="st-"] { font-family: 'Plus Jakarta Sans', sans-serif; background-color: #ffffff; }

    /* Blue Glow Search Bar */
    div[data-baseweb="input"] {
        border-radius: 50px !important;
        border: 2px solid #3b82f6 !important;
        box-shadow: 0 4px 20px rgba(59, 130, 246, 0.15) !important;
    }

    /* Result Card with Yellow Accent */
    .result-card {
        border: 1px solid #f0f0f0; border-radius: 12px; padding: 25px;
        margin-bottom: 20px; border-left: 6px solid #fbbf24;
        background: white;
    }
    .patent-title-link { color: #fbbf24; font-size: 20px; font-weight: 700; text-decoration: none; display: block; }
    
    /* Obsidian Detail Header */
    .obsidian-header { background: #000; color: white; padding: 40px; border-radius: 12px 12px 0 0; }
    .detail-body { border: 1px solid #eee; border-top: none; padding: 40px; border-radius: 0 0 12px 12px; }
    
    /* The 11-Field Info Grid */
    .info-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 15px; margin-top: 25px; }
    .info-box { background: #fdfdfd; padding: 15px; border-radius: 10px; border: 1px solid #f1f1f1; }
    .label { font-size: 10px; color: #9ca3af; text-transform: uppercase; font-weight: 800; }
    .value { font-size: 14px; color: #111; font-weight: 600; margin-top: 4px; }
    </style>
    """, unsafe_allow_html=True)

apply_styles()

# --- HERO ---
st.markdown("<div style='text-align:center; padding-top:40px;'><h1 style='font-size:54px; font-weight:800;'>ARCHISTRATEGOS</h1></div>", unsafe_allow_html=True)

# --- ADVANCED SEARCH (THE 11 FILTERS) ---
with st.container():
    _, mid, _ = st.columns([1, 6, 1])
    with mid:
        main_q = st.text_input("", placeholder="Quick Search...", label_visibility="collapsed")
        
        with st.expander("⚙️ ADVANCED MOE FILTERS (ALL 11 SPECIFICATIONS)"):
            c1, c2, c3 = st.columns(3)
            f_app_no = c1.text_input("Application Number")
            f_title = c1.text_input("Title")
            f_type = c1.selectbox("Application Type", ["All", "1. PCT National Entry", "2. Divisional", "3. Conversion", "4. Normal w/ Priority", "5. Normal w/o Priority"])
            
            f_owner = c2.text_input("Owner / Applicant")
            f_agent = c2.text_input("Agent Details")
            f_p_country = c2.text_input("Priority Country")
            
            f_p_no = c3.text_input("Priority Number")
            f_p_date = c3.date_input("Priority Date", value=None)
            f_app_date = c3.date_input("Application Date", value=None)
            
            # Earliest Priority & Abstract keywords
            f_e_priority = st.date_input("Earliest Priority Date", value=None)
            f_abstract_key = st.text_input("Keywords in Abstract")

        # SORTING
        sort_choice = st.selectbox("Sort Results By:", ["Application Date", "Earliest Priority Date", "Title (A-Z)"])

# --- DATA & SORTING ENGINE ---
raw_data = [{
    "app_no": "AE20223145",
    "title": "MAGNETICALLY DRIVEN ENGINE UTILIZING MEGNATICAL TECHNOLOGIES",
    "abstract": "An engine-based system employing advanced magnetic interactions for high-efficiency output. This invention seeks to reduce energy consumption by in-channeling magnetic force.",
    "owner": "Innovative Power Systems LTD",
    "agent": "Emily Smith (Future Patents Consultancy)",
    "app_date": "2023-06-15",
    "p_country": "United Kingdom",
    "p_no": "UK-9912-B",
    "p_date": "2023-01-10",
    "e_priority": "2023-01-10",
    "app_type": "4. Normal Application with Priority"
}]

df = pd.DataFrame(raw_data)

# Sort logic
if sort_choice == "Application Date": df = df.sort_values("app_date", ascending=False)
elif sort_choice == "Earliest Priority Date": df = df.sort_values("e_priority")
else: df = df.sort_values("title")

# --- RESULTS ---
if main_q or f_app_no:
    st.markdown(f"Found {len(df)} results", unsafe_allow_html=True)
    for _, r in df.iterrows():
        # Result Card
        st.markdown(f"""
        <div class="result-card">
            <span style="background:#fef3c7; color:#92400e; padding:4px 10px; border-radius:6px; font-size:11px; font-weight:700;">{r['app_type']}</span>
            <span style="float:right; color:#9ca3af; font-size:13px;">{r['app_no']}</span>
            <div class="patent-title-link">{r['title']}</div>
            <div style="font-size:14px; color:#666; margin-top:10px;">
                👤 <b>Owner:</b> {r['owner']} &nbsp;&nbsp;&nbsp; 📅 <b>Filed:</b> {r['app_date']}
            </div>
        </div>
        """, unsafe_allow_html=True)

        # The 11-Field Result Grid
        with st.expander("VIEW FULL 11-FIELD SPECIFICATIONS"):
            st.markdown(f"""
            <div class="obsidian-header">
                <span style="background:#fbbf24; color:black; padding:4px 10px; border-radius:4px; font-size:10px; font-weight:800;">OFFICIAL DATA</span>
                <h1 style="margin-top:10px; font-size:28px;">{r['title']}</h1>
            </div>
            <div class="detail-body">
                <h4>Abstract</h4>
                <p style="color:#4b5563;">{r['abstract']}</p>
                <div class="info-grid">
                    <div class="info-box"><div class="label">1. Application Number</div><div class="value">{r['app_no']}</div></div>
                    <div class="info-box"><div class="label">2. Patent Title</div><div class="value">{r['title']}</div></div>
                    <div class="info-box"><div class="label">3. Abstract</div><div class="value">See Above</div></div>
                    <div class="info-box"><div class="label">4. Owner / Applicant</div><div class="value">{r['owner']}</div></div>
                    <div class="info-box"><div class="label">5. Agent Details</div><div class="value">{r['agent']}</div></div>
                    <div class="info-box"><div class="label">6. Application Date</div><div class="value">{r['app_date']}</div></div>
                    <div class="info-box"><div class="label">7. Priority Country</div><div class="value">{r['p_country']}</div></div>
                    <div class="info-box"><div class="label">8. Priority Number</div><div class="value">{r['p_no']}</div></div>
                    <div class="info-box"><div class="label">9. Priority Date</div><div class="value">{r['p_date']}</div></div>
                    <div class="info-box"><div class="label">10. Earliest Priority Date</div><div class="value">{r['e_priority']}</div></div>
                    <div class="info-box"><div class="label">11. Application Type</div><div class="value">{r['app_type']}</div></div>
                </div>
            </div>
            """, unsafe_allow_html=True)
