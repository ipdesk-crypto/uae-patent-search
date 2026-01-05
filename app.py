import streamlit as st
import pandas as pd

# --- 1. SETTINGS & AUTHENTICATION ---
# Change this to your desired password
SECRET_PASSWORD = "Archistratego2026" 

st.set_page_config(page_title="Archistratego | UAE Patent Search", layout="wide")

def check_password():
    """Returns True if the user had the correct password."""
    if "password_correct" not in st.session_state:
        st.session_state["password_correct"] = False

    if st.session_state["password_correct"]:
        return True

    # Show login screen
    st.markdown("<br><br>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.image("logo.jpeg", width=200)
        st.title("Secure Access")
        password = st.text_input("Please enter the platform password", type="password")
        if st.button("Unlock Platform"):
            if password == SECRET_PASSWORD:
                st.session_state["password_correct"] = True
                st.rerun()
            else:
                st.error("❌ Incorrect password. Please try again.")
    return False

# --- 2. DATA LEGEND & UI STYLING ---
APP_TYPE_LEGEND = {
    "1": "PCT National Entry",
    "2": "Divisional Application",
    "3": "Conversion Application",
    "4": "Normal Application with Priority Data",
    "5": "Normal Application without Priority Data"
}

def apply_branding():
    st.markdown("""
    <style>
    :root { --uae-gold: #FFB800; }
    .stApp { background-color: white; }
    .header-box { display: flex; align-items: center; gap: 20px; border-bottom: 3px solid var(--uae-gold); padding-bottom: 15px; margin-bottom: 30px; }
    .stTextInput > div > div > input { border-radius: 24px !important; }
    div.stButton > button { background-color: var(--uae-gold) !important; color: black !important; border-radius: 20px; font-weight: bold; }
    .result-card { padding: 20px; border-bottom: 1px solid #eee; }
    .patent-title { color: #1a0dab; font-size: 20px; font-weight: 500; cursor: pointer; text-decoration: none; }
    .type-badge { background-color: var(--uae-gold); padding: 2px 8px; border-radius: 4px; font-size: 11px; font-weight: bold; }
    .data-label { font-weight: bold; color: #555; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. THE SEARCH APP ---
def run_main_app():
    apply_branding()
    
    # Header
    st.markdown(f"""
        <div class='header-box'>
            <h2 style='margin:0;'>🇦🇪 UAE Patent Search Platform</h2>
        </div>
    """, unsafe_allow_html=True)

    # Search Bar
    query = st.text_input("", placeholder="Search anything (Application #, Title, Owner, Agent...)", label_visibility="collapsed")

    # Filters
    with st.expander("Advanced Search Filters"):
        c1, c2, c3 = st.columns(3)
        with c1:
            st.text_input("Application Number")
            st.text_input("Owner Name")
        with c2:
            st.selectbox("Application Type", ["All"] + list(APP_TYPE_LEGEND.values()))
            st.text_input("Agent/Firm")
        with c3:
            st.date_input("Date Range", [])
            st.text_input("Priority Country")

    if query:
        # Placeholder Data for Demo
        results = pd.DataFrame([{
            "app_no": "P555/2026",
            "title": "SMART LOGISTICS DRONE FOR DUBAI URBAN AREAS",
            "abstract": "An autonomous drone delivery system equipped with heat-resistant battery cooling for continuous operation in UAE summer climates...",
            "owner": "TechLogistics UAE",
            "agent": "Legal Partners Ltd",
            "date": "2026-01-02",
            "p_country": "UAE",
            "p_no": "UAE-998",
            "p_date": "2025-12-01",
            "e_priority": "2025-12-01",
            "type_id": "4"
        }])

        st.markdown(f"**Found {len(results)} results**")
        
        for _, row in results.iterrows():
            st.markdown(f"""
            <div class="result-card">
                <div class="patent-title">{row['title']}</div>
                <div style="color: #006621; font-size: 14px;">{row['app_no']} • {row['date']} <span class="type-badge">Type {row['type_id']}</span></div>
                <div style="margin-top:10px; font-size: 14px;">{row['abstract']}</div>
                <div style="margin-top:10px; font-size: 13px;">
                    <span class="data-label">Owner:</span> {row['owner']} | <span class="data-label">Agent:</span> {row['agent']}<br>
                    <span class="data-label">Priority:</span> {row['p_country']} ({row['p_no']}) | <span class="data-label">Priority Date:</span> {row['p_date']} | <span class="data-label">Earliest:</span> {row['e_priority']}
                </div>
            </div>
            """, unsafe_allow_html=True)

# --- 4. EXECUTION FLOW ---
if check_password():
    run_main_app()
