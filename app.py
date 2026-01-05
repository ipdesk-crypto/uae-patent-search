import streamlit as st
import pandas as pd

# --- SYSTEM CONFIG ---
st.set_page_config(page_title="ARCHISTRATEGOS", layout="wide", initial_sidebar_state="collapsed")

def apply_executive_styles():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap');
    html, body, [class*="st-"] { font-family: 'Plus Jakarta Sans', sans-serif; background-color: #ffffff; }

    /* Blue Glow Search Bar (Screenshot 5) */
    div[data-baseweb="input"] {
        border-radius: 50px !important;
        border: 2px solid #3b82f6 !important;
        box-shadow: 0 4px 20px rgba(59, 130, 246, 0.15) !important;
    }

    /* Result Card with Yellow Accent (Screenshot 9) */
    .result-card {
        border: 1px solid #f0f0f0; border-radius: 12px; padding: 25px;
        margin-bottom: 20px; border-left: 6px solid #fbbf24;
        background: white; transition: 0.3s ease;
    }
    .result-card:hover { transform: translateY(-3px); box-shadow: 0 10px 30px rgba(0,0,0,0.05); }
    .patent-title-link { color: #fbbf24; font-size: 20px; font-weight: 700; text-decoration: none; display: block; }
    
    /* Obsidian Detail View (Screenshot 2, 10, 11) */
    .obsidian-header { background: #000; color: white; padding: 40px; border-radius: 12px 12px 0 0; }
    .detail-body { border: 1px solid #eee; border-top: none; padding: 40px; border-radius: 0 0 12px 12px; }
    
    /* 11-Field Info Grid */
    .info-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 15px; margin-top: 25px; }
    .info-box { background: #fdfdfd; padding: 15px; border-radius: 10px; border: 1px solid #f1f1f1; }
    .label { font-size: 10px; color: #9ca3af; text-transform: uppercase; font-weight: 800; letter-spacing: 0.5px; }
    .value { font-size: 14px; color: #111; font-weight: 600; margin-top: 4px; line-height: 1.4; }
    </style>
    """, unsafe_allow_html=True)

apply_executive_styles()

# --- HERO SECTION ---
st.markdown("<div style='text-align:center; padding: 40px 0;'><h1 style='font-size:54px; font-weight:800; color:#111; margin:0;'>ARCHISTRATEGOS</h1><p style='color:#888; font-size:15px;'>UAE Ministry of Economy Official IP Portal</p></div>", unsafe_allow_html=True)

# --- ADVANCED SEARCH FILTERS (THE 11 FIELDS) ---
with st.container():
    _, mid, _ = st.columns([1, 6, 1])
    with mid:
        main_q = st.text_input("", placeholder="Quick Search (Keyword, Number, or Owner...)", label_visibility="collapsed")
        
        with st.expander("⚙️ ADVANCED MOE SEARCH FILTERS (11 SPECIFICATIONS)"):
            f1, f2, f3 = st.columns(3)
            f_app_no = f1.text_input("Application Number")
            f_title = f1.text_input("Title (A-Z Search)")
            f_type = f1.selectbox("Application Type", ["All", "1. PCT National Entry", "2. Divisional", "3. Conversion", "4. Normal w/ Priority", "5. Normal w/o Priority"])
            
            f_owner = f2.text_input("Owner / Applicant")
            f_agent = f2.text_input("Agent Details")
            f_abstract = f2.text_input("Abstract Keywords")
            
            f_p_country = f3.text_input("Priority Country")
            f_p_no = f3.text_input("Priority Number")
            f_p_date = f3.date_input("Priority Date", value=None)
            
            f_app_date = st.date_input("Application Filing Date", value=None)
            f_e_priority = st.date_input("Earliest Priority Date", value=None)

        col_sort, col_space = st.columns([2, 4])
        sort_choice = col_sort.selectbox("Sort Results By:", ["Application Date", "Earliest Priority Date", "Title (A-Z)"])

# --- DATA MAPPING & SORTING ---
# Every item contains exactly the 11 fields requested
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

# Sort Engine
if sort_choice == "Application Date":
    df = df.sort_values("app_date", ascending=False)
elif sort_choice == "Earliest Priority Date":
    df = df.sort_values("e_priority", ascending=True)
else:
    df = df.sort_values("title", ascending=True)

# --- RESULT DISPLAY ---
if main_q or f_app_no or f_owner:
    st.markdown(f"<p style='color:#888; margin-top:20px;'>Found {len(df)} official records</p>", unsafe_allow_html=True)
    
    for _, r in df.iterrows():
        # Clean Result Card
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

        # Full 11-Field Detail View
        with st.expander("VIEW COMPLETE 11-FIELD SPECIFICATIONS"):
            st.markdown(f"""
            <div class="obsidian-header">
                <span style="background:#fbbf24; color:black; padding:4px 10px; border-radius:4px; font-size:10px; font-weight:800;">OFFICIAL DATA</span>
                <h1 style="margin-top:10px; font-size:28px;">{r['title']}</h1>
                <p style="opacity:0.7;">Application Number: {r['app_no']} | Filed: {r['app_date']}</p>
            </div>
            <div class="detail-body">
                <h4 style="margin-top:0;">Abstract</h4>
                <p style="color:#4b5563; line-height:1.6;">{r['abstract']}</p>
                <hr style="border:0.5px solid #eee; margin:25px 0;">
                <div class="info-grid">
                    <div class="info-box"><div class="label">1. Application Number</div><div class="value">{r['app_no']}</div></div>
                    <div class="info-box"><div class="label">2. Patent Title</div><div class="value">{r['title']}</div></div>
                    <div class="info-box"><div class="label">3. Application Date</div><div class="value">{r['app_date']}</div></div>
                    <div class="info-box"><div class="label">4. Owner / Applicant</div><div class="value">{r['owner']}</div></div>
                    <div class="info-box"><div class="label">5. Agent Details</div><div class="value">{r['agent']}</div></div>
                    <div class="info-box"><div class="label">6. Priority Country</div><div class="value">{r['p_country']}</div></div>
                    <div class="info-box"><div class="label">7. Priority Number</div><div class="value">{r['p_no']}</div></div>
                    <div class="info-box"><div class="label">8. Priority Date</div><div class="value">{r['p_date']}</div></div>
                    <div class="info-box"><div class="label">9. Earliest Priority Date</div><div class="value">{r['e_priority']}</div></div>
                    <div class="info-box"><div class="label">10. Application Type</div><div class="value">{r['app_type']}</div></div>
                    <div class="info-box"><div class="label">11. Technical Abstract</div><div class="value">Field Loaded Successfully</div></div>
                </div>
            </div>
            """, unsafe_allow_html=True)
