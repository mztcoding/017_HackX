import streamlit as st

def show_home():
    # --- CSS for Home Only (Shows Header) ---
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
    
/* ================= FIXED HEADER ================= */
    .fixed-header {
        position: fixed;
        top: 0; left: 0; width: 100%; height: 90px; /* Slightly taller to accommodate larger text */
        background: rgba(255, 255, 255, 0.9);
        backdrop-filter: blur(10px);
        z-index: 99999;
        display: flex; justify-content: space-between; align-items: center;
        padding: 0 50px;
        box-shadow: 0 2px 20px rgba(0, 0, 0, 0.05);
        border-bottom: 1px solid rgba(0, 0, 0, 0.05);
    }
    
    .header-logo {
        font-size: 1.5rem; font-weight: 800; color: #000000;
        letter-spacing: -1px; cursor: pointer;
    }

    .nav-links {
        display: flex; gap: 40px; 
    }

    /* UPDATED NAV ITEM FOR LINKS */
    .nav-item {
        font-size: 1.2rem; 
        font-weight: 600; 
        color: #333 !important; /* Force color */
        cursor: pointer; 
        transition: color 0.3s ease;
        text-decoration: none !important; /* Remove underline */
    }
    .nav-item:hover { color: #006400 !important; }

/* "Get Started" Button Styling */
    .header-btn {
        background: #157556 !important; /* Flat Emerald Green Base */
        color: white !important;
        font-weight: 700; 
        font-size: 1.15rem; 
        padding: 12px 35px; 
        border-radius: 12px; /* Rounded Rectangle */
        border: none;
        cursor: pointer;
        box-shadow: 0 4px 10px rgba(21, 117, 86, 0.3);
        transition: all 0.3s ease;
    }

    /* RESTORED RED HOVER EFFECT */
    .header-btn:hover { 
        transform: translateY(-2px);
        background: linear-gradient(90deg, #ff6b6b 0%, #ff8787 100%) !important; /* Red Gradient */
        box-shadow: 0 15px 30px -10px rgba(255, 107, 107, 0.6); /* Red Shadow */
        color: white;
    }

    /* 1. HUGE LOGO TITLE */
    .hero-logo {
        font-size: 5rem; font-weight: 800; color: #004d00; text-align: center;
        letter-spacing: -2px; line-height: 1.1; margin-top: -20px; margin-bottom: 20px;
    }

    /* 2. THE BADGE (SEAMLESS TRAFFIC LIGHT LOOP) */
        
        @keyframes trafficLightCycle {
            /* START: RED */
            0% {
                background-color: #fee2e2; color: #991b1b; border-color: #fecaca;
                box-shadow: 0 4px 15px rgba(153, 27, 27, 0.15);
            }
            /* TRANSITION TO YELLOW */
            25% {
                background-color: #fef3c7; color: #92400e; border-color: #fde68a;
                box-shadow: 0 4px 15px rgba(146, 64, 14, 0.15);
            }
            /* MIDDLE: GREEN */
            50% {
                background-color: #eef9f2; color: #006400; border-color: #d0e8d9;
                box-shadow: 0 4px 15px rgba(0, 100, 0, 0.15);
            }
            /* TRANSITION BACK TO YELLOW */
            75% {
                background-color: #fef3c7; color: #92400e; border-color: #fde68a;
                box-shadow: 0 4px 15px rgba(146, 64, 14, 0.15);
            }
            /* END: BACK TO RED (Matches 0%) */
            100% {
                background-color: #fee2e2; color: #991b1b; border-color: #fecaca;
                box-shadow: 0 4px 15px rgba(153, 27, 27, 0.15);
            }
        }

        .ai-badge-container { display: flex; justify-content: center; margin-bottom: 20px; }
        
        .ai-badge {
                padding: 10px 25px; /* Slightly more padding for larger text */
                border-radius: 50px; 
                font-weight: 700; 
                font-size: 1.2rem; /* Increased from 1rem */
                color: #000000 !important; /* Force Black (overrides the animation colors) */
                display: flex; align-items: center; gap: 10px;
                border: 1px solid transparent;
                /* The animation will still cycle the background color, but text stays black */
                animation: trafficLightCycle 8s infinite; 
            }

    /* 3. MAIN HERO TITLE */
        .hero-title-main {
            font-size: 3rem; 
            font-weight: 800; 
            color: #000000; /* Pure Black */
            text-align: center;
            line-height: 1.2; 
            margin-bottom: 15px;
            /* No text-shadow here anymore */
        }

    /* 4. SUBTITLE */
        .hero-subtitle {
            /* UPDATED: Increased font-size from 1.1rem to 1.35rem */
            font-size: 1.35rem; 
            color: #546e7a; 
            text-align: center;
            max-width: 900px; /* Increased width slightly so text doesn't cramp */
            margin: 0 auto 40px auto; 
            font-weight: 400; 
            line-height: 1.6;
        }

    /* 5. STATS SECTION */
    .stats-container {
        display: flex; justify-content: center; gap: 30px; margin-top: 10px;
        padding-bottom: 30px; flex-wrap: wrap;
    }
    .stat-item { text-align: center; min-width: 120px; }
    .stat-number { font-size: 2.5rem; font-weight: 700; color: #006400; display: block; }
    .stat-label { font-size: 0.9rem; color: #546e7a; font-weight: 500; }

    /* 6. LANDING BUTTON STYLING */
    div.stButton { text-align: center; }
    
    div.stButton > button:first-child {
        background: #157556 !important; /* Flat Emerald Green Base */
        color: white !important;
        font-size: 1.15rem !important; 
        font-weight: 700 !important;
        padding: 16px 50px !important; 
        border-radius: 12px !important; /* Rounded Rectangle */
        border: none;
        box-shadow: 0 4px 10px rgba(21, 117, 86, 0.3);
        transition: all 0.3s ease; display: block; margin: 0 auto;
    }

    /* RESTORED RED HOVER EFFECT */
    div.stButton > button:first-child:hover {
        transform: translateY(-2px);
        background: linear-gradient(90deg, #ff6b6b 0%, #ff8787 100%) !important; /* Red Gradient */
        box-shadow: 0 15px 30px -10px rgba(255, 107, 107, 0.6) !important; /* Red Shadow */
        color: white !important;
    }
    
    /* EXTRA FIX: Target the paragraph inside the button just in case */
    div.stButton > button:first-child p {
        font-size: 1.15rem !important;
        font-weight: 700 !important;
    }

    /* 7. FEATURES SECTION - UPDATED FOR CLICKABLE CARDS */
    .section-title { font-size: 4rem; font-weight: 800; color: #004d00; text-align: center; margin-top: 60px; margin-bottom: 10px; }
    .section-subtitle { font-size: 1.5rem; color: #000000; text-align: center; font-weight: 500; margin-bottom: 40px; }
    .features-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 20px; max-width: 1200px; margin: 0 auto; padding: 0 20px; }
    
    /* STYLE THE ANCHOR TAG AS A CARD */
    a.feature-card {
            display: block; /* Makes the link act like a box, not text */
            height: 100%;   /* Ensures cards in same row are same height */
            text-decoration: none !important; /* Removes the blue underline */
            
            background: #ffffff; 
            padding: 25px 20px; 
            border-radius: 15px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.05); 
            border: 1px solid #f0f4f8; 
            text-align: left; 
            transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1); 
            cursor: pointer;
        }

    /* HOVER EFFECT */
    a.feature-card:hover {
        transform: translateY(-10px) scale(1.02); 
        background-color: #ffffe0; 
        border-color: #fff9c4; 
        box-shadow: 0 20px 40px rgba(0,0,0,0.1); 
        text-decoration: none !important; /* Ensure underline doesn't appear on hover */
    }

    .feature-icon { font-size: 2.5rem; margin-bottom: 15px; display: block; }
    
    /* FORCE TEXT COLORS INSIDE THE LINK (So they don't turn blue) */
    a.feature-card .feature-title { 
        font-size: 1.2rem; 
        font-weight: 700; 
        color: #000000 !important; 
        margin-bottom: 8px; 
        text-decoration: none !important;
    }
    
    a.feature-card .feature-desc { 
        font-size: 1rem; 
        color: #546e7a !important; 
        font-weight: 400; 
        text-decoration: none !important;
    }

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
    
    /* ================= HELPLINE BOX ================= */
    .helpline-container {
        background-color: #fff9e6; /* Light Beige/Yellow */
        border: 1px solid #ffeeba;
        border-radius: 12px;
        padding: 20px 30px;
        display: flex;
        align-items: center;
        gap: 25px;
        max-width: 900px;
        margin: 40px auto; /* Centered spacing */
        box-shadow: 0 4px 15px rgba(0,0,0,0.02);
    }

    .helpline-icon-box {
        width: 55px;
        height: 55px;
        background-color: #ffe0b2; /* Darker yellow circle */
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        flex-shrink: 0;
        color: #f57f17; /* Dark Orange Icon */
    }

    .helpline-text h3 {
        margin: 0 0 8px 0;
        font-size: 1.25rem;
        font-weight: 700;
        color: #000000 !important;
    }

    .helpline-text p {
        margin: 0;
        font-size: 1rem;
        color: #4a5568 !important;
        font-weight: 400;
    }
    
    .hl-number {
        font-weight: 700;
        color: #000;
    }
    
    
    
</style>
""", unsafe_allow_html=True)

    # st.markdown("""
    # <style>
    #     .fixed-header {
    #         position: fixed;
    #         top: 0; left: 0; width: 100%; height: 70px;
    #         background: white; z-index: 999;
    #         display: flex; justify-content: space-between; align-items: center;
    #         padding: 0 5%; border-bottom: 1px solid #eee;
    #     }
    #     .nav-item { margin: 0 15px; text-decoration: none; color: black; font-weight: 500; }
    # </style>
    
    # <div class="fixed-header">
    #     <div style="font-weight:800; font-size:1.2rem;">Mera Challan 🇵🇰</div>
    #     <div class="nav-links">
    #         <a href="?page=main&nav=0" target="_self" class="nav-item">Rules</a>
    #         <a href="?page=main&nav=1" target="_self" class="nav-item">AI Lawyer</a>
    #     </div>
    #     <a href="?page=main&nav=0" target="_self">
    #         <button style="background:#157556; color:white; border:none; padding:8px 20px; border-radius:8px; cursor:pointer;">
    #             Get Started
    #         </button>
    #     </a>
    # </div>
    # <div style="margin-top:100px;"></div>
    # """, unsafe_allow_html=True)

    # # --- Hero Section ---
    # st.markdown("<h1 style='text-align: center;'>Traffic Awareness & Legal Assistance</h1>", unsafe_allow_html=True)
    
    # Corrected "Launch" Button Link logic
    

    # --- ADD FIXED HEADER ---
    st.markdown("""
        <div class="fixed-header">
            <div class="header-logo">Mera Challan 🇵🇰</div>
            <div class="nav-links">
                <a href="?page=main&nav=0" target="_self" class="nav-item">Traffic Rules</a>
                <a href="?page=main&nav=1" target="_self" class="nav-item">AI Lawyer</a>
                <a href="?page=main&nav=2" target="_self" class="nav-item">Validate Challan</a>
                <a href="?page=main&nav=3" target="_self" class="nav-item">Know Your Route</a>
            </div>
            <a href="?page=main&nav=0" target="_self" style="text-decoration: none;">
                <button class="header-btn">Get Started</button>
            </a>
        </div>
    """, unsafe_allow_html=True)
    
    st.write("") 
    st.markdown('<div class="hero-logo">Mera Challan</div>', unsafe_allow_html=True)
    st.markdown("""
        <div class="ai-badge-container">
            <div class="ai-badge">
                <span>🚦</span> AI-powered Traffic Assistant
            </div>
        </div>
    """, unsafe_allow_html=True)
    # 3. MAIN HERO TITLE (UPDATED COLORS & WIDTH)
    # Removing <br> makes it wider. 
    # Using <span> tags to color specific words.
    # 3. MAIN HERO TITLE (UPDATED DARKER COLORS)
    # Updated Hero Title - Clean Black with Shadow
    st.markdown("""
        <div class="hero-title-main">
            Traffic Awareness, Clarity & Legal Assistance
        </div>
    """, unsafe_allow_html=True)
    st.markdown('<div class="hero-subtitle">Empowering Pakistani citizens with instant knowledge of traffic laws, real-time legal guidance against unlawful stops, and digital challan validation.</div>', unsafe_allow_html=True)

    c1, c2, c3 = st.columns([1, 0.5, 1]) 
    with c2:
        if st.button("🚀 Launch AI Assistant", use_container_width=True):
            st.session_state['current_view'] = 'main_app'
            st.rerun()

    st.markdown("""
        <div class="stats-container">
            <div class="stat-item"><span class="stat-number">10K+</span><span class="stat-label">Citizens Helped</span></div>
            <div class="stat-item"><span class="stat-number">5M+</span><span class="stat-label">PKR Saved in Fines</span></div>
            <div class="stat-item"><span class="stat-number">24/7</span><span class="stat-label">Available AI</span></div>
            <div class="stat-item"><span class="stat-number">Free</span><span class="stat-label">To Use</span></div>
        </div>
    """, unsafe_allow_html=True)

# ... previous code (Stats Section) ...

    st.markdown("---")
    
    # REPLACEMENT FOR "Features" SECTION
    st.markdown("""
        <div style="text-align: center; margin-top: 60px; margin-bottom: 10px;">
            <span style="font-size: 3rem; font-weight: 800; color: #000000; letter-spacing: -1px; line-height: 1.2;">
                Everything You Need to 
            </span>
            <span style="font-size: 3rem; font-weight: 800; color: #006400; letter-spacing: -1px; line-height: 1.2;">
                Stay Protected
            </span>
        </div>
        
        <div style="text-align: center; font-size: 1.35rem; color: #546e7a; margin-bottom: 50px; font-weight: 400; max-width: 750px; margin-left: auto; margin-right: auto;">
            From understanding traffic laws to fighting unlawful fines, Mera Challan has you covered at every step.
        </div>
    """, unsafe_allow_html=True)


    # --- FEATURES SECTION (Clean Version) ---
    st.markdown("""
        <div class="features-grid">
            <a href="?page=main&nav=0" target="_self" class="feature-card">
                <span class="feature-icon">📚</span>
                <h3 class="feature-title">Traffic Rules Library</h3>
                <p class="feature-desc">Comprehensive database of Pakistani traffic laws explained in simple English.</p>
            </a>
            <a href="?page=main&nav=1" target="_self" class="feature-card">
                <span class="feature-icon">⚖️</span>
                <h3 class="feature-title">AI Lawyer</h3>
                <p class="feature-desc">Get instant legal guidance when facing corrupt officers or unlawful stops.</p>
            </a>
            <a href="?page=main&nav=2" target="_self" class="feature-card">
                <span class="feature-icon">✅</span>
                <h3 class="feature-title">Challan Validator</h3>
                <p class="feature-desc">Instantly verify if your traffic challan is legitimate and issued correctly.</p>
            </a>
            <a href="?page=main&nav=3" target="_self" class="feature-card">
                <span class="feature-icon">🗺️</span>
                <h3 class="feature-title">Route Guide</h3>
                <p class="feature-desc">Tell us your route and we'll explain all traffic rules you need to follow.</p>
            </a>
        </div>
    """, unsafe_allow_html=True)
    
    # ... (After your Features Grid st.markdown block) ...

# --- EMERGENCY HELPLINE SECTION ---
    st.markdown("""
        <div class="helpline-container">
            <div class="helpline-icon-box">
                <svg xmlns="http://www.w3.org/2000/svg" width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"></path>
                    <line x1="12" y1="9" x2="12" y2="13"></line>
                    <line x1="12" y1="17" x2="12.01" y2="17"></line>
                </svg>
            </div>
            <div class="helpline-text">
                <h3>Emergency Helpline Numbers</h3>
                <p>
                    Traffic Police: <span class="hl-number">15</span> &nbsp;|&nbsp; 
                    Rescue (Ambulance): <span class="hl-number">1122</span> &nbsp;|&nbsp; 
                    NHMP (Motorway) <span class="hl-number">130</span>
                </p>
            </div>
        </div>
        """, unsafe_allow_html=True)

    # ... (Your existing Disclaimer block follows here) ...

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
    
# --- PRO FOOTER SECTION ---
    st.markdown("""
    <style>
        /* Footer Specific Styles */
        .main-footer {
            background-color: #0a1f18; /* Dark Green */
            color: #ffffff;
            padding: 100px 40px 60px 40px;
            font-family: 'Poppins', sans-serif;
            margin-top: 50px;
            margin-left: -6rem; /* Break out of Streamlit container margins */
            margin-right: -5rem;
            margin-bottom: -15rem;
        }
        
        .footer-content {
            display: flex;
            flex-wrap: wrap;
            justify-content: space-between;
            max-width: 1200px;
            margin: 0 auto;
            gap: 40px;
            border-bottom: 1px solid #1c3d32;
            padding-bottom: 40px;
        }
        
        .footer-col {
            flex: 1;
            min-width: 200px;
        }
        
        .footer-brand h3 {
            color: #ffffff !important;
            font-size: 1.5rem;
            font-weight: 700;
            margin-bottom: 15px;
            display: flex; align-items: center; gap: 10px;
        }
        
        .footer-brand p {
            color: #8fa69d !important;
            font-size: 0.95rem;
            line-height: 1.6;
            margin-bottom: 15px;
        }
        
        .contact-info div {
            display: flex;
            align-items: center;
            gap: 10px;
            color: #d1e0db;
            margin-bottom: 10px;
            font-size: 0.9rem;
        }
        
        .footer-col h4 {
            color: #ffffff !important;
            font-size: 1.1rem;
            font-weight: 600;
            margin-bottom: 25px;
        }
        
        .footer-links ul {
            list-style: none;
            padding: 0;
            margin: 0;
        }
        
        .footer-links li {
            color: #8fa69d;
            font-size: 0.95rem;
            margin-bottom: 15px;
            cursor: pointer;
            transition: color 0.3s ease;
        }
        
        .footer-links li:hover {
            color: #ffffff;
            transform: translateX(5px);
        }
        
        .footer-bottom {
            max-width: 1200px;
            margin: 0 auto;
            padding-top: 25px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            flex-wrap: wrap;
            color: #5c7c70;
            font-size: 0.85rem;
        }
        
        .footer-bottom span { color: #5c7c70; }
        
    </style>

    <div class="main-footer">
        <div class="footer-content">
            <div class="footer-col footer-brand">
                <h3>Mera Challan</h3>
                <p>Empowering Pakistani citizens with traffic law knowledge and protection against unlawful fines.</p>
                <div class="contact-info">
                    <div>✉️ support@merachallan.pk</div>
                    <div>📞 +92 300 1234567</div>
                </div>
            </div>
    </div>
    """, unsafe_allow_html=True)


    
    # _, col2, _ = st.columns([1, 1, 1])
    # with col2:
    #     if st.button("🚀 Launch AI Assistant", use_container_width=True):
    #         st.session_state['current_view'] = 'main_app'
    #         st.rerun()