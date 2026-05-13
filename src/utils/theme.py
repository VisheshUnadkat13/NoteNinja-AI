import streamlit as st

def apply_theme():
    # Initialize state
    if "dark_mode" not in st.session_state:
        st.session_state.dark_mode = True

    # Theme colors (Premium Dark Mode)
    bg_color = "#0f172a"
    accent_gradient = "linear-gradient(135deg, #6366f1 0%, #a855f7 100%)"
    secondary_accent = "#8b5cf6"
    text_color = "#f8fafc"
    card_bg = "rgba(30, 41, 59, 0.7)"
    border_color = "rgba(255, 255, 255, 0.1)"

    # Apply CSS
    st.markdown(f"""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap');

        /* Global Styles */
        html, body, [data-testid="stAppViewContainer"] {{
            font-family: 'Plus Jakarta Sans', sans-serif;
            background-color: {bg_color};
            color: {text_color};
            background-image: 
                radial-gradient(at 0% 0%, rgba(99, 102, 241, 0.15) 0px, transparent 50%),
                radial-gradient(at 100% 100%, rgba(168, 85, 247, 0.15) 0px, transparent 50%);
            background-attachment: fixed;
        }}

        /* Scrollbar Styling */
        ::-webkit-scrollbar {{
            width: 8px;
        }}
        ::-webkit-scrollbar-track {{
            background: {bg_color};
        }}
        ::-webkit-scrollbar-thumb {{
            background: {border_color};
            border-radius: 10px;
        }}
        ::-webkit-scrollbar-thumb:hover {{
            background: {secondary_accent};
        }}

        /* Main Container Padding */
        .block-container {{
            padding-top: 3rem;
            max-width: 1100px;
        }}

        /* Sidebar Styling (Advanced Glassmorphism) */
        [data-testid="stSidebar"] {{
            background: rgba(15, 23, 42, 0.7) !important;
            backdrop-filter: blur(20px) saturate(180%);
            border-right: 1px solid {border_color};
        }}
        
        [data-testid="stSidebar"] [data-testid="stMarkdownContainer"] h1,
        [data-testid="stSidebar"] [data-testid="stMarkdownContainer"] h2,
        [data-testid="stSidebar"] [data-testid="stMarkdownContainer"] h3 {{
            color: {text_color} !important;
            background: none;
            -webkit-text-fill-color: initial;
            font-weight: 600;
            letter-spacing: -0.02em;
        }}

        /* Premium Buttons */
        .stButton>button {{
            background: {accent_gradient};
            color: white !important;
            border: none;
            padding: 0.8rem 1.8rem;
            border-radius: 14px;
            font-weight: 600;
            font-size: 1rem;
            transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05);
            width: 100%;
            text-transform: none;
            letter-spacing: 0.2px;
        }}

        .stButton>button:hover {{
            transform: translateY(-4px) scale(1.02);
            box-shadow: 0 0 20px rgba(99, 102, 241, 0.6), 0 20px 25px -5px rgba(0, 0, 0, 0.2);
            border-color: transparent !important;
        }}

        .stButton>button:active {{
            transform: translateY(0) scale(0.98);
        }}

        /* Inputs, TextAreas & Selectboxes */
        div[data-baseweb="select"] > div, 
        div[data-baseweb="input"] > div,
        .stTextInput > div > div > input,
        .stTextArea > div > div > textarea {{
            background-color: {card_bg} !important;
            border: 1px solid {border_color} !important;
            border-radius: 14px !important;
            color: {text_color} !important;
            padding: 2px 10px !important;
            transition: all 0.3s ease;
        }}

        /* Fix Selectbox Text Color (Selected Value) */
        div[data-baseweb="select"] div[data-testid="stMarkdownContainer"] p,
        div[data-baseweb="select"] span,
        div[data-baseweb="select"] div {{
            color: {text_color} !important;
        }}

        /* Fix Selectbox Dropdown Options */
        div[data-baseweb="popover"] div {{
            background-color: {bg_color} !important;
            color: {text_color} !important;
        }}

        div[data-baseweb="select"] > div:hover, 
        div[data-baseweb="input"] > div:focus-within {{
            border-color: {secondary_accent} !important;
            box-shadow: 0 0 0 2px rgba(139, 92, 246, 0.2);
        }}

        /* File Uploader styling */
        [data-testid="stFileUploader"] {{
            background: {card_bg};
            border: 2px dashed {border_color};
            border-radius: 16px;
            padding: 20px;
            transition: all 0.3s ease;
        }}
        [data-testid="stFileUploader"]:hover {{
            border-color: {secondary_accent};
            background: rgba(30, 41, 59, 0.9);
        }}
        
        /* Style the 'Browse files' button inside the uploader */
        [data-testid="stFileUploader"] section button {{
            background-color: #0f172a !important;
            color: white !important;
            border: 1px solid {border_color} !important;
            border-radius: 10px !important;
        }}
        [data-testid="stFileUploader"] section button:hover {{
            background-color: {secondary_accent} !important;
            border-color: {secondary_accent} !important;
        }}

        /* Metric Cards */
        [data-testid="stMetric"] {{
            background: {card_bg};
            padding: 20px;
            border-radius: 16px;
            border: 1px solid {border_color};
        }}
        [data-testid="stMetricValue"] {{
            background: {accent_gradient};
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-weight: 800;
            font-size: 2.5rem !important;
        }}

        /* Custom Card Class */
        .premium-card {{
            background: {card_bg};
            backdrop-filter: blur(12px);
            padding: 30px;
            border-radius: 24px;
            border: 1px solid {border_color};
            margin-bottom: 25px;
            transition: all 0.4s ease;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
        }}

        .premium-card:hover {{
            transform: translateY(-5px);
            border: 1px solid rgba(139, 92, 246, 0.3);
            box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.2);
        }}

        /* Animation for headers */
        h1, h2, h3 {{
            background: {accent_gradient};
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-weight: 800;
            letter-spacing: -0.04em;
        }}

        /* Progress Bar */
        .stProgress > div > div > div {{
            background: {accent_gradient} !important;
            height: 10px !important;
            border-radius: 10px !important;
        }}

        /* Sidebar Divider */
        hr {{
            margin: 1.5rem 0;
            border: 0;
            border-top: 1px solid {border_color};
            opacity: 0.5;
        }}

        /* Custom Alerts */
        .stAlert {{
            background: {card_bg} !important;
            backdrop-filter: blur(10px) !important;
            border: 1px solid {border_color} !important;
            border-radius: 16px !important;
            color: {text_color} !important;
        }}

        /* Style Header to match website */
        header[data-testid="stHeader"] {{
            background-color: rgba(15, 23, 42, 0.0) !important;
            backdrop-filter: blur(10px);
            border-bottom: 1px solid rgba(255, 255, 255, 0.05);
        }}
        
        #MainMenu {{visibility: hidden;}}
        footer {{visibility: hidden;}}
        .stDeployButton {{display: none;}}



        /* Hero Animation */
        @keyframes fadeIn {{
            from {{ opacity: 0; transform: translateY(20px); }}
            to {{ opacity: 1; transform: translateY(0); }}
        }}

        .hero-section {{
            animation: fadeIn 0.8s ease-out;
        }}

        /* Radio Buttons - Hide default circles and style like chips */
        div[role="radiogroup"] {{
            gap: 10px;
        }}
        div[role="radiogroup"] label {{
            background: {card_bg};
            padding: 10px 20px;
            border-radius: 12px;
            border: 1px solid {border_color};
            transition: all 0.3s ease;
        }}
        div[role="radiogroup"] label:hover {{
            border-color: {secondary_accent};
            background: rgba(99, 102, 241, 0.1);
        }}
        /* Target the text inside the radio button label */
        div[role="radiogroup"] label div[data-testid="stMarkdownContainer"] p {{
            color: {text_color} !important;
        }}
        
        /* Global Sidebar Text Fix */
        [data-testid="stSidebar"] {{
            color: {text_color} !important;
        }}
        
        [data-testid="stWidgetLabel"] p {{
            font-weight: 600;
            color: {text_color} !important;
        }}

        /* Keep File Uploader label muted as requested */
        div[data-testid="stFileUploader"] label p {{
            color: #94a3b8 !important;
            font-weight: 400 !important;
        }}
        
        </style>
    """, unsafe_allow_html=True)