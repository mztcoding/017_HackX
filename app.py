import streamlit as st
from streamlit_option_menu import option_menu

# --- Page Configuration ---
st.set_page_config(
    page_title="Mera Challan - Traffic AI Assistant",
    page_icon="🇵🇰",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- Session State for Navigation ---
if 'current_view' not in st.session_state:
    st.session_state['current_view'] = 'landing'

def enter_app():
    st.session_state['current_view'] = 'main_app'

# --- MODERN CSS INJECTION (GLOBAL & LANDING DEFAULTS) ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&display=swap');

    /* Global App Settings - Default is the Green Hue (Landing Page) */
    .stApp {
        background: linear-gradient(180deg, #f4fcf6 0%, #e8f5eb 100%);
        font-family: 'Poppins', sans-serif;
    }
    
    /* Hide Header/Footer */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    /* ================= LANDING PAGE STYLES ================= */

    /* 1. HUGE LOGO TITLE */
    .hero-logo {
        font-size: 5rem; font-weight: 800; color: #004d00; text-align: center;
        letter-spacing: -2px; line-height: 1.1; margin-top: -20px; margin-bottom: 20px;
    }

    /* 2. THE BADGE */
    .ai-badge-container { display: flex; justify-content: center; margin-bottom: 20px; }
    .ai-badge {
        background-color: #eef9f2; color: #006400; padding: 8px 20px;
        border-radius: 50px; font-weight: 600; font-size: 1rem;
        display: flex; align-items: center; gap: 10px;
        box-shadow: 0 4px 10px rgba(0,100,0,0.1); border: 1px solid #d0e8d9;
    }

    /* 3. MAIN HERO TITLE */
    .hero-title-main {
        font-size: 3rem; font-weight: 800; color: #1a2e3b; text-align: center;
        line-height: 1.2; margin-bottom: 15px;
    }

    /* 4. SUBTITLE */
    .hero-subtitle {
        font-size: 1.1rem; color: #546e7a; text-align: center;
        max-width: 800px; margin: 0 auto 40px auto; font-weight: 400; line-height: 1.6;
    }

    /* 5. STATS SECTION */
    .stats-container {
        display: flex; justify-content: center; gap: 30px; margin-top: 20px;
        padding-bottom: 30px; flex-wrap: wrap;
    }
    .stat-item { text-align: center; min-width: 120px; }
    .stat-number { font-size: 2.5rem; font-weight: 700; color: #006400; display: block; }
    .stat-label { font-size: 0.9rem; color: #546e7a; font-weight: 500; }

    /* 6. LANDING BUTTON STYLING */
    div.stButton { text-align: center; }
    div.stButton > button:first-child {
        background: linear-gradient(90deg, #006400 0%, #008f00 100%);
        color: white; font-size: 1.3rem; font-weight: 600;
        padding: 16px 50px; border-radius: 50px; border: none;
        box-shadow: 0 10px 20px -10px rgba(0,100,0,0.5);
        transition: all 0.3s ease; display: block; margin: 0 auto;
    }
    div.stButton > button:first-child:hover {
        transform: scale(1.05);
        background: linear-gradient(90deg, #ff6b6b 0%, #ff8787 100%);
        box-shadow: 0 15px 30px -10px rgba(255, 107, 107, 0.6);
        color: white;
    }

    /* 7. FEATURES SECTION */
    .section-title { font-size: 4rem; font-weight: 800; color: #004d00; text-align: center; margin-top: 60px; margin-bottom: 10px; }
    .section-subtitle { font-size: 1.5rem; color: #000000; text-align: center; font-weight: 500; margin-bottom: 40px; }
    .features-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 20px; max-width: 1200px; margin: 0 auto; padding: 0 20px; }
    .feature-card {
        background: #ffffff; padding: 25px 20px; border-radius: 15px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.05); border: 1px solid #f0f4f8; text-align: center;
        transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1); cursor: default;
    }
    .feature-card:hover {
        transform: translateY(-10px) scale(1.02); 
        background-color: #ffffe0; border-color: #fff9c4; 
        box-shadow: 0 20px 40px rgba(0,0,0,0.1); 
    }
    .feature-icon { font-size: 2.5rem; margin-bottom: 15px; display: block; }
    .feature-title { font-size: 1.2rem; font-weight: 700; color: #000000 !important; margin-bottom: 8px; }
    .feature-desc { font-size: 1rem; color: #000000 !important; font-weight: 400; }

    /* DISCLAIMER */
    .disclaimer-container { margin-top: 60px; padding: 20px; border-top: 1px solid #e0e0e0; background-color: #f9f9f9; display: flex; justify-content: center; }
    .disclaimer-text { font-size: 1rem; color: #777; max-width: 800px; line-height: 1.7; text-align: center; }

    /* ================= MAIN APP DASHBOARD STYLES ================= */
    .dashboard-card {
        background-color: #ffffff; padding: 25px; border-radius: 20px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.03); height: 100%;
        border: 1px solid #f0f0f0; transition: transform 0.2s;
    }
    .dashboard-card:hover { transform: translateY(-3px); box-shadow: 0 8px 25px rgba(0,0,0,0.06); }
    .card-icon-dash {
        background-color: #e8f5eb; color: #004d00; width: 45px; height: 45px;
        border-radius: 12px; display: flex; align-items: center; justify-content: center;
        font-size: 1.3rem; margin-bottom: 15px;
    }
    .card-title-dash { font-size: 1.1rem; font-weight: 700; color: #1a2e3b; margin-bottom: 5px; }
    .card-text-dash { font-size: 0.95rem; color: #6c757d; line-height: 1.5; }
    .welcome-header { font-size: 2.5rem; font-weight: 700; color: #1a2e3b; margin-top: -20px; }
    .welcome-sub { font-size: 1.1rem; color: #6c757d; margin-bottom: 30px; }
    
</style>
""", unsafe_allow_html=True)


# ================= VIEW CONTROLLER =================

if st.session_state['current_view'] == 'landing':
    
    # --- LANDING PAGE (EXACT PRESERVED) ---
    st.write("") 
    st.markdown('<div class="hero-logo">Mera Challan</div>', unsafe_allow_html=True)
    st.markdown("""
        <div class="ai-badge-container">
            <div class="ai-badge">
                <span>🚦</span> AI-powered Traffic Assistant
            </div>
        </div>
    """, unsafe_allow_html=True)
    st.markdown('<div class="hero-title-main">Traffic Awareness, Clarity<br>& Legal Assistance</div>', unsafe_allow_html=True)
    st.markdown('<div class="hero-subtitle">Empowering Pakistani citizens with instant knowledge of traffic laws, real-time legal guidance against unlawful stops, and digital challan validation.</div>', unsafe_allow_html=True)

    c1, c2, c3 = st.columns([1, 0.45, 1]) 
    with c2:
        st.button("Launch AI Assistant", on_click=enter_app)

    st.markdown("""
        <div class="stats-container">
            <div class="stat-item"><span class="stat-number">10K+</span><span class="stat-label">Citizens Helped</span></div>
            <div class="stat-item"><span class="stat-number">5M+</span><span class="stat-label">PKR Saved in Fines</span></div>
            <div class="stat-item"><span class="stat-number">24/7</span><span class="stat-label">Available AI</span></div>
            <div class="stat-item"><span class="stat-number">Free</span><span class="stat-label">To Use</span></div>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown('<div class="section-title">Features</div>', unsafe_allow_html=True)
    st.markdown('<p class="section-subtitle">Everything you need for traffic safety in one app.</p>', unsafe_allow_html=True)

    st.markdown("""
        <div class="features-grid">
            <div class="feature-card">
                <span class="feature-icon">📚</span><h3 class="feature-title">Traffic Rules</h3>
                <p class="feature-desc">Simplified traffic laws and Motor Vehicle Ordinances.</p>
            </div>
            <div class="feature-card">
                <span class="feature-icon">⚖️</span><h3 class="feature-title">AI Lawyer</h3>
                <p class="feature-desc">Instant legal citations for unlawful stops.</p>
            </div>
            <div class="feature-card">
                <span class="feature-icon">✅</span><h3 class="feature-title">Validator</h3>
                <p class="feature-desc">Check if a challan is authentic or fake.</p>
            </div>
             <div class="feature-card">
                <span class="feature-icon">🗺️</span><h3 class="feature-title">Route Guide</h3>
                <p class="feature-desc">Proactive legal alerts for your journey.</p>
            </div>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div class="disclaimer-container">
            <div class="disclaimer-text">
                <b>Disclaimer:</b> Mera Challan is an AI-powered assistant designed for educational and informational purposes only. 
                It does not constitute professional legal advice or official government documentation. 
                Please verify all citations with the official Motor Vehicle Ordinance (1965) or consult a qualified attorney for legal representation. 
                We are not responsible for any actions taken based on the information provided by this system.
            </div>
        </div>
    """, unsafe_allow_html=True)


elif st.session_state['current_view'] == 'main_app':
    
# 2. INJECT CSS FOR YELLOW DASHBOARD & VISIBLE HEADER
    st.markdown("""
    <style>
        /* Force Header Visible */
        header {visibility: visible !important;} 
        
        /* OVERRIDE BACKGROUND FOR DASHBOARD -> White with Yellow Hue */
        .stApp {
            background: linear-gradient(180deg, #ffffff 0%, #fffef0 100%) !important;
        }

        /* --- FORCE BLACK TEXT FOR ALL PAGES (AI Lawyer, Validator, Route) --- */
        h1, h2, h3, h4, h5, h6, p, .stMarkdown, .stText, label, div[data-testid="stMetricValue"] {
            color: #000000 !important;
        }
        
        /* Specific fix for Input/Chat/Uploader labels */
        .stTextInput label, .stFileUploader label, .stChatInput textarea {
            color: #000000 !important;
        }

        /* --- DASHBOARD CARD STYLES --- */
        .dashboard-card {
            background-color: #ffffff; padding: 25px; border-radius: 20px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.03); height: 100%;
            border: 1px solid #f0f0f0; transition: all 0.3s ease;
        }
        
        /* HOVER EFFECT (Green Hue + Shadow) */
        .dashboard-card:hover { 
            transform: translateY(-5px); 
            box-shadow: 0 12px 30px rgba(0, 100, 0, 0.15); 
            background-color: #f0fff4; 
            border-color: #c3e6cb; 
        }

        .card-icon-dash {
            background-color: #e8f5eb; color: #004d00; width: 45px; height: 45px;
            border-radius: 12px; display: flex; align-items: center; justify-content: center;
            font-size: 1.3rem; margin-bottom: 15px;
        }
        
        /* Card Text Specifics (Keep these slightly grey for style, or change to black if preferred) */
        .card-title-dash { font-size: 1.1rem; font-weight: 700; color: #1a2e3b !important; margin-bottom: 5px; }
        .card-text-dash { font-size: 0.95rem; color: #6c757d !important; line-height: 1.5; }
        
        .welcome-header { font-size: 2.5rem; font-weight: 700; color: #1a2e3b !important; margin-top: -20px; }
        .welcome-sub { font-size: 1.1rem; color: #6c757d !important; margin-bottom: 30px; }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR (WITH "DRIVER MENU") ---
    with st.sidebar:
        # Profile Section
        st.markdown("""
        <div style="background-color: #fdfdf5; padding: 15px; border-radius: 15px; display: flex; align-items: center; gap: 10px; margin-bottom: 20px; border: 1px solid #f0f0e0;">
            <div style="font-size: 2rem;">👮‍♂️</div>
            <div>
                <h4 style="margin:0; color:#004d00; font-size:1.1rem; font-weight:700;">Driver Menu</h4>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Navigation Menu
        selected_page = option_menu(
            menu_title="Main Menu",
            options=["Traffic Guide", "AI Lawyer", "Validator", "Route Guide"],
            icons=['grid', 'chat-dots', 'shield-check', 'map'], 
            menu_icon="cast", 
            default_index=0,
            styles={
                "container": {"padding": "0!important", "background-color": "transparent"},
                "icon": {"color": "#004d00", "font-size": "16px"}, 
                "nav-link": {"font-size": "15px", "text-align": "left", "margin":"5px", "--hover-color": "#fffde7"},
                "nav-link-selected": {"background-color": "#006400", "color": "white"},
            }
        )
        
        st.markdown("---")
        
        # --- CENTERED HOME BUTTON ---
        # We use 3 columns: Left spacer, Button (Middle), Right spacer
        c1, c2, c3 = st.columns([0.1, 1, 0.1]) 
        
        with c2:
            if st.button("⬅️ Home"):
                 st.session_state['current_view'] = 'landing'
                 st.rerun()

    # --- DASHBOARD CONTENT ---
    # CHANGED: Check for "Traffic Guide"
    if selected_page == "Traffic Guide":
        
        st.markdown('<div class="welcome-header">Welcome, Driver! 👋</div>', unsafe_allow_html=True)
        st.markdown('<div class="welcome-sub">How can I help you regarding traffic laws today?</div>', unsafe_allow_html=True)

        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            <div class="dashboard-card">
                <div class="card-icon-dash">🛑</div>
                <div class="card-title-dash">Exceeding Prescribed Speed Limit</div>
                <div class="card-text-dash">
                    <span style="font-size:1.2rem; color:#aaa;">2000 PKR fine for Motorcycles and 5000 for cars less than 2000cc</span>
                </div>
            </div>
            """, unsafe_allow_html=True)
            
        with col2:
            st.markdown("""
            <div class="dashboard-card">
                <div class="card-icon-dash">🚦</div>
                <div class="card-title-dash">Violation of Traffic Signals</div>
                <div class="card-text-dash">
                    <span style="font-size:1.2rem; color:#aaa;">2000 PKR fine for Motorcycles and 5000 for cars less than 2000cc</span>
                </div>
            </div>
            """, unsafe_allow_html=True)

        st.write("") 
        st.write("") 

        col3, col4 = st.columns(2)

        with col3:
            st.markdown("""
            <div class="dashboard-card">
                <div class="card-icon-dash">🪪</div>
                <div class="card-title-dash">Driving a Motor Vehicle Without a Driving License</div>
                <div class="card-text-dash">
                    <span style="font-size:1.2rem; color:#aaa;">2000 PKR fine for Motorcycles and 5000 for cars less than 2000cc</span>
                </div>
            </div>
            """, unsafe_allow_html=True)

        with col4:
            st.markdown("""
            <div class="dashboard-card">
                <div class="card-icon-dash">🔞</div>
                <div class="card-title-dash">Driving in Violation of Age Limit</div>
                <div class="card-text-dash">
                    <span style="font-size:1.2rem; color:#aaa;">2000 PKR fine for Motorcycles and 5000 for cars less than 2000cc</span>
                </div>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("---")
        user_input = st.chat_input("Search for a Rule...")
        if user_input:
            st.info(f"🤖 **AI Processing:** {user_input} ... (Go to 'AI Lawyer' tab for full conversation)")

        # --- OTHER PAGES ---
    elif selected_page == "AI Lawyer":
            st.title("⚖️ AI Lawyer")
            st.write("Consult the Motor Vehicle Ordinance (1965) for instant legal defense.")

            # --- LAWYER DASHBOARD GRID ---
            col1, col2 = st.columns(2)

            with col1:
                st.markdown("""
                <div class="dashboard-card">
                    <div class="card-icon-dash">📜</div>
                    <div class="card-title-dash">Section 3 - MVO 1965</div>
                    <div class="card-text-dash">
                        <span style="font-weight:600;">Necessity of Driving License</span><br>
                        "No person shall drive a motor vehicle in any public place unless he holds an effective driving license."
                    </div>
                </div>
                """, unsafe_allow_html=True)

            with col2:
                st.markdown("""
                <div class="dashboard-card">
                    <div class="card-icon-dash">🔞</div>
                    <div class="card-title-dash">Section 4 - MVO 1965</div>
                    <div class="card-text-dash">
                        <span style="font-weight:600;">Age Limit Restrictions</span><br>
                        "No person under the age of 18 years shall drive a motor vehicle in any public place."
                    </div>
                </div>
                """, unsafe_allow_html=True)

            st.write("") # Spacing
            
            col3, col4 = st.columns(2)

            with col3:
                st.markdown("""
                <div class="dashboard-card">
                    <div class="card-icon-dash">🛑</div>
                    <div class="card-title-dash">Section 112 - MVO 1965</div>
                    <div class="card-text-dash">
                        <span style="font-weight:600;">Disobedience of Orders</span><br>
                        "The driver of a motor vehicle shall cause the vehicle to stop and remain stationary when required."
                    </div>
                </div>
                """, unsafe_allow_html=True)

            with col4:
                st.markdown("""
                <div class="dashboard-card">
                    <div class="card-icon-dash">⚖️</div>
                    <div class="card-title-dash">Section 99 - MVO 1965</div>
                    <div class="card-text-dash">
                        <span style="font-weight:600;">Dangerous Driving</span><br>
                        "Driving at a speed or in a manner which is dangerous to the public having regard to traffic nature."
                    </div>
                </div>
                """, unsafe_allow_html=True)

            st.markdown("---")
            st.write("### 💬 Ask for Legal Defense")
            st.chat_input("Explain your situation (e.g. 'A warden stopped me without a reason')...")
        
    elif selected_page == "Validator":
        st.title("✅ Challan Validator")
        st.file_uploader("Upload Ticket Photo")
        
    elif selected_page == "Route Guide":
            st.title("🗺️ Route Guide")
            st.write("Enter your route details below. The AI will analyze the path for area specific legal laws.")
            st.chat_input("Explain your route (e.g. Liberty Market to DHA Phase 6)...")
