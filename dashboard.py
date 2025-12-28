import streamlit as st
from streamlit_option_menu import option_menu


def get_clear():
    clear_button=st.sidebar.button("Start new session", key="clear")
    # clear_button="dw"
    return clear_button

def reset_search():
    # 'search_bar' is the key we will give to our text_input
    st.session_state.search_bar = ""

# URDU_LEGAL_GUIDE = """
# <div style="
#     background-color: #f0f9ff; 
#     padding: 12px; 
#     border-radius: 10px; 
#     border: 1px solid #bae6fd; 
#     box-shadow: 0 2px 4px rgba(0,0,0,0.05);
#     color: #000000;
# ">
#     <h3 style="color: #f87171; text-align: right;">بدعنوانی سے بچاؤ</h3>
#     <p dir="rtl" style="text-align: right; font-size: 0.95rem; color: #ddd;">
#         ٹریفک پولیس کی بدعنوانی اور غیر قانونی ہراساں کرنے سے بچنے کے لیے درج ذیل قانونی نکات یاد رکھیں:
#     </p>
#     <hr style="border-color: #444;">
#     <ul dir="rtl" style="text-align: right; color: #aaa; font-size: 0.9rem; list-style-type: none; padding-right: 0;">
#         <li style="margin-bottom: 12px;">🛑 <b>نقدی نہ دیں:</b> کوئی بھی ٹریفک وارڈن موقع پر نقد جرمانہ لینے کا مجاز نہیں ہے۔ ہمیشہ بینک چالان طلب کریں۔</li>
#         <li style="margin-bottom: 12px;">🪪 <b>شناخت کا حق:</b> آپ کو پولیس افسر سے اس کا نام اور بیلٹ نمبر پوچھنے کا پورا قانونی حق حاصل ہے۔</li>
#         <li style="margin-bottom: 12px;">📱 <b>ویڈیو ریکارڈنگ:</b> قانونی طور پر آپ پبلک جگہ پر پولیس کی کارروائی کی ویڈیو بنا سکتے ہیں بشرطیکہ آپ ان کے کام میں رکاوٹ نہ ڈالیں۔</li>
#         <li style="margin-bottom: 12px;">📝 <b>چالان پر دستخط:</b> اگر آپ کو لگتا ہے کہ آپ نے غلطی نہیں کی، تو چالان پر 'متفق نہیں' (Disputed) لکھ کر دستخط کر سکتے ہیں۔</li>
#         <li style="margin-bottom: 12px;">📞 <b>شکایات:</b> اگر کوئی رشوت مانگے تو فوری طور پر 15 پر کال کریں یا 'سٹیزن پورٹل' پر شکایت درج کرائیں۔</li>
#     </ul>
#     <div style="background-color: #2d3748; padding: 10px; border-radius: 5px; margin-top: 15px;">
#         <p dir="rtl" style="text-align: right; font-size: 0.8rem; margin: 0; color: #90cdf4;">
#             <b>قانونی مشورہ:</b> ہمیشہ اپنی گاڑی کے اصل کاغذات اور ڈرائیونگ لائسنس ساتھ رکھیں تاکہ کسی کو بلاوجہ تنگ کرنے کا موقع نہ ملے۔
#         </p>
#     </div>
# </div>
# """

# URDU_LEGAL_GUIDE = """

#     <h4 style="color: #0369a1; text-align: right; margin: 0 0 8px 0; font-size: 1rem;">بدعنوانی سے بچاؤ 🛡️</h4>
#     <ul dir="rtl" style="text-align: right; font-size: 0.82rem; list-style-type: none; padding-right: 0; line-height: 1.4; margin: 0;">
#         <li style="margin-bottom: 5px;">🛑 <b>نقد جرمانہ نہ دیں:</b> ہمیشہ بینک چالان طلب کریں۔</li>
#         <li style="margin-bottom: 5px;">🪪 <b>شناخت:</b> افسر کا نام اور نمبر پوچھنا آپ کا حق ہے۔</li>
#         <li style="margin-bottom: 5px;">📱 <b>ریکارڈنگ:</b> آپ ویڈیو بنا سکتے ہیں۔</li>
#         <li style="margin-bottom: 0px;">📞 <b>شکایت:</b> کسی بھی بدتمیزی پر 15 پر کال کریں۔</li>
#     </ul>
# </div>
# """

traffic_rules = [
    {
        "id": 1, "title": "Speed Limit Violation", "icon": "🛑", "bike_fine": "2,000", "car_fine": "2,500",
        "desc": "Exceeding speed limits on city roads or highways.",
        "long_desc": "Under Section 112 of the MVO, exceeding the speed limit is a major cause of accidents. Modern ANPR cameras automatically detect speed. Repeat offenders may face license suspension."
    },
    {
        "id": 2, "title": "Signal Violation", "icon": "🚦", "bike_fine": "2,000", "car_fine": "5,000",
        "desc": "Jumping a red light or ignoring warden signals.",
        "long_desc": "Violation of traffic signals includes jumping a red light or failing to stop when a warden signals. In cities like Lahore/Islamabad, this is strictly monitored via Safe City cameras."
    },
    {
        "id": 3, "title": "No Driving License", "icon": "🪪", "bike_fine": "2,000", "car_fine": "5,000",
        "desc": "Driving without a valid, original license.",
        "long_desc": "Section 3 of the MVO prohibits driving without a license. If you have a learner's permit, you must have a licensed driver in the passenger seat and 'L' stickers on the vehicle."
    },
    {
        "id": 4, "title": "Underage Driving", "icon": "🔞", "bike_fine": "5,000", "car_fine": "10,000",
        "desc": "Driving while under the legal age of 18.",
        "long_desc": "Underage driving is now a non-compoundable offense in many districts, meaning the vehicle can be impounded and parents may be required to submit a legal undertaking in court."
    },
    {
        "id": 5, "title": "No Helmet (Rider)", "icon": "🪖", "bike_fine": "2,000", "car_fine": "N/A",
        "desc": "Riding a motorcycle without a safety helmet.",
        "long_desc": "High-quality, fastened helmets are mandatory. Simple caps or unfastened helmets are still considered a violation of safety protocols under Section 89-A."
    },
    {
        "id": 6, "title": "No Helmet (Pillion)", "icon": "👥", "bike_fine": "1,000", "car_fine": "N/A",
        "desc": "Second person on a bike not wearing a helmet.",
        "long_desc": "The 2025 enforcement requires both the rider and the pillion passenger to wear helmets. Failure results in a challan issued to the driver of the motorcycle."
    },
    {
        "id": 7, "title": "Mobile Phone Usage", "icon": "📱", "bike_fine": "2,000", "car_fine": "5,000",
        "desc": "Using a phone while driving or riding.",
        "long_desc": "This includes texting, calling, or even holding the device. Hands-free usage is discouraged but strictly handheld use is a fineable offense."
    },
    {
        "id": 8, "title": "Seat Belt Negligence", "icon": "💺", "bike_fine": "N/A", "car_fine": "1,500",
        "desc": "Driving without a fastened seat belt.",
        "long_desc": "Mandatory for all drivers and front-seat passengers. Modern e-challan systems use high-res sensors to detect unbuckled belts even at night."
    },
    {
        "id": 9, "title": "Wrong Way Driving", "icon": "↩️", "bike_fine": "1,000", "car_fine": "2,000",
        "desc": "Driving on the wrong side of a one-way road.",
        "long_desc": "One of the most dangerous violations. In addition to a fine, your vehicle may be impounded for 'Endangering Public Safety'."
    },
    {
        "id": 10, "title": "Fancy Number Plate", "icon": "🔢", "bike_fine": "2,000", "car_fine": "5,000",
        "desc": "Using non-standard or stylish plates.",
        "long_desc": "Only government-issued computerized plates are legal. Plates with fancy fonts, colors, or hidden numbers are illegal and easily detected by ANPR cameras."
    },
    {
        "id": 11, "title": "One-Wheeling", "icon": "🏍️", "bike_fine": "10,000", "car_fine": "N/A",
        "desc": "Performing dangerous stunts on public roads.",
        "long_desc": "This is a criminal offense. Violators are often arrested, and their motorcycles are permanently confiscated by the state."
    },
    {
        "id": 12, "title": "Smoke/Pollution", "icon": "💨", "bike_fine": "5,000", "car_fine": "10,000",
        "desc": "Vehicles emitting excessive visible smoke.",
        "long_desc": "Part of the Anti-Smog campaign. Vehicles must have a valid fitness certificate. Heavy fines are applied to commercial vehicles emitting black smoke."
    },
    {
        "id": 13, "title": "No-Parking Zone", "icon": "🅿️", "bike_fine": "500", "car_fine": "2,000",
        "desc": "Parking in restricted areas.",
        "long_desc": "If your vehicle is towed from a No-Parking zone, you must pay both the traffic challan and the lifter/towing charges at the police station."
    },
    {
        "id": 14, "title": "Overloading Goods", "icon": "📦", "bike_fine": "500", "car_fine": "3,000",
        "desc": "Carrying load exceeding vehicle capacity.",
        "long_desc": "Overloading affects vehicle braking and stability. For commercial trucks, fines are calculated per ton of excess weight."
    },
    {
        "id": 15, "title": "Illegal Overtaking", "icon": "🏎️", "bike_fine": "1,000", "car_fine": "2,500",
        "desc": "Overtaking from the wrong side.",
        "long_desc": "Always overtake from the right. Overtaking on bridges, narrow roads, or from the left is a violation of the Highway Code."
    },
    {
        "id": 16, "title": "Tinted Windows", "icon": "🕶️", "bike_fine": "N/A", "car_fine": "5,000",
        "desc": "Using dark/tinted glass without permission.",
        "long_desc": "Only factory-fitted glass within the legal transparency limit is allowed. Aftermarket black sheets result in immediate removal of the sheets and a fine."
    },
    {
        "id": 17, "title": "Triple Riding", "icon": "🏍️", "bike_fine": "5,000", "car_fine": "N/A",
        "desc": "More than two persons on one motorcycle.",
        "long_desc": "Section 101-A of MVO forbids carrying more than one passenger on a motorcycle. This is a high-priority violation in urban areas."
    },
    {
        "id": 18, "title": "Littering from Car", "icon": "🚮", "bike_fine": "5,000", "car_fine": "10,000",
        "desc": "Throwing trash out of a moving vehicle.",
        "long_desc": "A newly enforced fine under environmental protection laws. Dashcam footage or Safe City evidence can be used to issue e-challans."
    },
    {
        "id": 19, "title": "Fake Number Plate", "icon": "🚫", "bike_fine": "10,000", "car_fine": "15,000",
        "desc": "Using tampered or fake plates.",
        "long_desc": "This is treated as a forgery crime (PPC 468/471). In addition to fines, an FIR is usually registered against the vehicle owner."
    },
    {
        "id": 20, "title": "Dangerous Driving", "icon": "⚠️", "bike_fine": "5,000", "car_fine": "15,000",
        "desc": "Reckless maneuvers endangering lives.",
        "long_desc": "Includes zig-zagging, tailgating, or sudden lane changes without indicators. It carries some of the highest penalty points on your digital license."
    },
    {
        "id": 21, "title": "Unregistered Vehicle", "icon": "📑", "bike_fine": "1,000", "car_fine": "5,000",
        "desc": "Driving a vehicle not yet registered.",
        "long_desc": "New vehicles have a grace period (usually 60 days) to be registered. Driving 'Applied For' vehicles beyond this period is a violation."
    },
    {
        "id": 22, "title": "Blocking Footpath", "icon": "🚶", "bike_fine": "2,000", "car_fine": "5,000",
        "desc": "Parking or driving on pedestrian footpaths.",
        "long_desc": "Footpaths are strictly for pedestrians. Obstruction forces people onto the main road, increasing the risk of accidents."
    }
]

def show_dashboard(client, MODEL_ID):

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


    # 1. Initialize Chat Context (History)
    if "chat_history" not in st.session_state:
        # We start with a system instruction to set the AI's persona
        st.session_state.chat_history = [
            {"role": "user", "parts": [{"text": "Always give response in urdu. You are a specialized Pakistani Traffic Law expert. Answer only based on the Motor Vehicle Ordinance 1965."}]},
            {"role": "model", "parts": [{"text": "Understood. I am ready to provide legal guidance on Pakistani traffic laws."}]}
        ]

    # 2. Navigation
    default_idx = st.session_state.get('nav_target', 0)
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
                
        .streamlit-expanderHeader {
            background-color: #1e1e1e !important;
            border: 1px solid #333 !important;
            border-radius: 8px !important;
            padding: 12px !important;
            color: #ffffff !important;
            font-size: 1.1rem !important;
        }

        .streamlit-expanderContent {
            background-color: #121212 !important;
            border: 1px solid #333 !important;
            border-top: none !important;
            border-radius: 0 0 8px 8px !important;
        }
    </style>
    """, unsafe_allow_html=True)


# --- SIDEBAR (WITH "DRIVER MENU") ---
    with st.sidebar:
        # ... (Your Profile Section Code remains here) ...
        
        # DETERMINE DEFAULT INDEX
        # If we came from a header button, use that index. Otherwise default to 0.
        default_idx = st.session_state.get('nav_target', 0)

        # Navigation Menu
        selected_page = option_menu(
            menu_title="Main Menu",
            options=["Traffic Guide", "AI Lawyer", "Validator", "Route Guide"],
            icons=['grid', 'chat-dots', 'shield-check', 'map'], 
            menu_icon="cast", 
            default_index=default_idx,
            styles={
                "container": {"padding": "0!important", "background-color": "transparent"},
                "icon": {"color": "#004d00", "font-size": "16px"}, 
                "nav-link": {"font-size": "15px", "text-align": "left", "margin":"5px", "--hover-color": "#fffde7"},
                "nav-link-selected": {"background-color": "#006400", "color": "white"},
            }
        )
        
        # Clear the nav_target so if they refresh, it doesn't get stuck
        if 'nav_target' in st.session_state:
            del st.session_state['nav_target']
            
        # ... (Rest of sidebar code) ...
        
        st.markdown("---")
        
        # --- CENTERED HOME BUTTON ---
        # We use 3 columns: Left spacer, Button (Middle), Right spacer
        c1, c2, c3 = st.columns([0.08, 1, 0.08]) 
        
        with c2:
            if st.button("⬅ Home"):
                 st.session_state['current_view'] = 'landing'
                 st.rerun()

    # --- DASHBOARD CONTENT ---
    # CHANGED: Check for "Traffic Guide"
    if selected_page == "Traffic Guide":
        st.markdown('<div class="welcome-header">Rule Explorer 📚</div>', unsafe_allow_html=True)
        st.markdown('<div class="welcome-sub">Click on any rule card to reveal detailed legal info and fines.</div>', unsafe_allow_html=True)

        # 1. Search Logic
        if "search_bar" not in st.session_state: st.session_state.search_bar = ""
        
        col_search, col_reset = st.columns([4, 1])
        with col_search:
            query = st.text_input("Search rules...", key="search_bar").lower()
        with col_reset:
            st.write(" ") # Spacer
            st.button("Show All", on_click=lambda: st.session_state.update(search_bar=""), use_container_width=True)

        filtered = [r for r in traffic_rules if query in r['title'].lower() or query in r['desc'].lower()]

        # 2. Grid with Interactive Expanders
        for i in range(0, len(filtered), 2):
            cols = st.columns(2)
            for j in range(2):
                if i + j < len(filtered):
                    rule = filtered[i + j]
                    with cols[j]:
                        # The Expander acts as the 'Clickable Card'
                        with st.expander(f"{rule['icon']} {rule['title']}", expanded=False):
                            st.markdown(f"### {rule['title']}")
                            st.write(f"_{rule['desc']}_")
                            st.info(f"⚖️ **Legal Detail:** {rule['long_desc']}")
                            
                            # Fine Comparison Table
                            st.markdown(f"""
                            | Vehicle Type | Fine Amount |
                            | :--- | :--- |
                            | 🏍️ Motorcycle | {rule['bike_fine']} PKR |
                            | 🚗 Car / SUV | {rule['car_fine']} PKR |
                            """)
            
        # --- OTHER PAGES ---
    elif selected_page == "AI Lawyer":
        # Create columns for the top layout
        col_chat, col_guide = st.columns([0.7, 0.3])

        with col_chat:
            st.title("⚖️ Conversational AI Lawyer")
            
            # Message history display
            for message in st.session_state.chat_history[2:]:
                role = "user" if message["role"] == "user" else "assistant"
                with st.chat_message(role):
                    st.markdown(message["parts"][0]["text"])

        with col_guide:
            # 1. The Main Point (Visible)
            st.markdown("""
            <div style="background-color: #f0f9ff; padding: 12px; border-radius: 10px; border: 1px solid #bae6fd; color: #000000; margin-bottom: 5px;">
                <h4 style="color: #0369a1; text-align: right; margin: 0 0 5px 0;">بدعنوانی سے بچاؤ 🛡️</h4>
                <p dir="rtl" style="text-align: right; font-size: 0.85rem; margin: 0; line-height: 1.4;">
                    🛑 <b>نقدی نہ دیں:</b> کوئی بھی ٹریفک وارڈن موقع پر نقد جرمانہ لینے کا مجاز نہیں ہے۔ ہمیشہ بینک چالان طلب کریں۔
                </p>
            </div>
            """, unsafe_allow_html=True)

            # 2. Additional Points (Hidden in Expander)
            with st.expander("مزید قانونی معلومات"):
                st.markdown("""
                <div dir="rtl" style="text-align: right; color: #000000; font-size: 0.82rem; line-height: 1.6;">
                    <ul style="list-style-type: none; padding-right: 0;">
                        <li>🪪 <b>شناخت:</b> آپ کو افسر کا نام اور بیلٹ نمبر پوچھنے کا پورا حق ہے۔</li>
                        <hr style="margin: 8px 0; border-top: 1px solid #eee;">
                        <li>📱 <b>ویڈیو:</b> آپ پبلک جگہ پر کارروائی کی ویڈیو بنا سکتے ہیں۔</li>
                        <hr style="margin: 8px 0; border-top: 1px solid #eee;">
                        <li>📝 <b>دستخط:</b> اختلاف کی صورت میں چالان پر 'Disputed' لکھ سکتے ہیں۔</li>
                        <hr style="margin: 8px 0; border-top: 1px solid #eee;">
                        <li>📞 <b>شکایات:</b> رشوت مانگنے پر <b>15</b> پر کال کریں۔</li>
                    </ul>
                    <div style="background-color: #e0f2fe; padding: 8px; border-radius: 5px; margin-top: 5px; font-size: 0.75rem;">
                        <b>قانونی مشورہ:</b> ہمیشہ اصل کاغذات ساتھ رکھیں تاکہ تنگ کرنے کا موقع نہ ملے۔
                    </div>
                </div>
                """, unsafe_allow_html=True)

        # Chat Input - Placed globally at the bottom
        if prompt := st.chat_input("Ask a follow-up question..."):
            # 1. Update UI and State
            st.session_state.chat_history.append({"role": "user", "parts": [{"text": prompt}]})
            
            # 2. Logic for generating response
            try:
                response = client.models.generate_content(
                    model=MODEL_ID,
                    contents=st.session_state.chat_history
                )
                ai_response = response.text
                st.session_state.chat_history.append({"role": "model", "parts": [{"text": ai_response}]})
                
                # Rerun to display the new messages in the history loop above
                st.rerun()
            except Exception as e:
                st.error(f"Lawyer is busy: {e}")

    elif selected_page == "Validator":
        st.header("✅ Challan Validator")
        st.write("Upload a photo of your traffic ticket to verify its details and legitimacy.")

        # 1. File Uploader
        uploaded_file = st.file_uploader("Upload Ticket Photo", type=['png', 'jpg', 'jpeg'])

        if uploaded_file is not None:
            # Display a preview of the uploaded image
            st.image(uploaded_file, caption="Uploaded Challan", width=300)
            
            # 2. Analyze Button
            if st.button("Analyze Challan", type="primary"):
                with st.spinner("AI is analyzing your ticket details..."):
                    try:
                        # Convert file to bytes for the API
                        image_bytes = uploaded_file.getvalue()
                        
                        # 3. Call Gemini API
                        # We send the image and a prompt to extract specific Pakistani traffic law details
                        response = client.models.generate_content(
                            model=MODEL_ID,
                            contents=[
                                "Extract the following from this Pakistani traffic challan: "
                                "1. Violation Name, 2. Fine Amount, 3. Date, 4. Vehicle Number. "
                                "Then, verify if the fine amount matches the standard Motor Vehicle Ordinance rules. "
                                "Explain if there are any discrepancies.",
                                {"inline_data": {"data": image_bytes, "mime_type": "image/jpeg"}}
                            ]
                        )

                        # 4. Display Results
                        st.success("Analysis Complete!")
                        st.markdown("### 📋 Analysis Results")
                        st.write(response.text)

                    except Exception as e:
                        st.error(f"An error occurred during analysis: {e}")
        else:
            st.info("Please upload an image file (JPG/PNG) to begin.")    

    elif selected_page == "Route Guide":
        st.header("🗺️ Route Guide")
        st.write("Complete the details below to get a specialized legal itinerary for your journey.")

        # Create the Form
        with st.form("route_form"):
            col1, col2 = st.columns(2)
            
            with col1:
                start_point = st.text_input("Starting Point", placeholder="e.g. Gulberg, Lahore")
                vehicle_type = st.selectbox("Vehicle Type", ["Car", "Motorcycle", "Commercial/Truck", "Electric Bike"])
            
            with col2:
                destination = st.text_input("Destination", placeholder="e.g. Bahria Town")
                travel_time = st.selectbox("Time of Travel", ["Daylight", "Night", "Rush Hour"])

            additional_details = st.text_area("Specific Concerns", placeholder="e.g. I have a modified exhaust, or I'm carrying heavy luggage.")
            
            submit_button = st.form_submit_button("Generate Legal Route Tips", type="primary")

        # Handle Form Submission
        if submit_button:
            if not start_point or not destination:
                st.warning("Please enter both a start and end point.")
            else:
                with st.spinner("Calculating route jurisdictions..."):
                    try:
                        # Constructing a detailed prompt for the Form data
                        route_prompt = f"""
                        Act as a Pakistani Traffic Law Expert. 
                        Provide a 'Safe Journey Guide' for the following trip:
                        - Route: From {start_point} to {destination}
                        - Vehicle: {vehicle_type}
                        - Time: {travel_time}
                        - User Notes: {additional_details}

                        Please structure your response with these headers:
                        ### 🚦 Route Jurisdictions
                        (Mention if they will encounter City Traffic Police, Cantt Board, or Motorway Police)
                        
                        ### ⚖️ Area-Specific Laws
                        (Highlight specific rules like helmet requirements, lane restrictions for bikes, or one-way zones common on this route)
                        
                        ### 🛡️ Legal Protection Tips
                        (Give 3-4 bullet points on what to do if stopped by an officer on this specific path)
                        """

                        response = client.models.generate_content(
                            model=MODEL_ID,
                            contents=route_prompt
                        )

                        # Display the Results
                        st.markdown("---")
                        st.success(f"Legal Guide for {start_point} ➔ {destination}")
                        st.markdown(response.text)
                        
                    except Exception as e:
                        st.error(f"Could not generate guide: {e}")

        # Static Tips Section (Always visible at the bottom)
        st.markdown("---")
        st.subheader("💡 General Journey Tips")
        t1, t2, t3 = st.columns(3)
        with t1:
            st.info("**Digital Docs**\nKeep a photo of your license and CNIC on your phone at all times.")
        with t2:
            st.info("**Checkpoints**\nBe extra cautious at 'Nakas' during late hours or near sensitive zones.")
        with t3:
            st.info("**Challan App**\nVerify any paper challan via the official 'Digital Challan' portal immediately.")