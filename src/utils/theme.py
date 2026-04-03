# import streamlit as st

# def apply_theme():

#     # Initialize state
#     if "dark_mode" not in st.session_state:
#         st.session_state.dark_mode = True

#     # Toggle in sidebar
#     st.sidebar.markdown("### 🎨 Theme")
#     dark_mode = st.sidebar.toggle("🌙 Dark Mode", value=st.session_state.dark_mode)

#     st.session_state.dark_mode = dark_mode

#     # Theme colors
#     if dark_mode:
#         bg_color = "#0E1117"
#         text_color = "#FFFFFF"
#         card_color = "#1E1E1E"
#         border_color = "#333"
#     else:
#         bg_color = "#FFFFFF"
#         text_color = "#000000"
#         card_color = "#F5F5F5"
#         border_color = "#DDD"

#     # Apply CSS
#     st.markdown(f"""
#         <style>
#         .stApp {{
#             background-color: {bg_color};
#             color: {text_color};
#         }}

#         div[data-testid="stSidebar"] {{
#             background-color: {card_color};
#         }}

#         .block-container {{
#             padding-top: 2rem;
#         }}

#         /* Buttons */
#         .stButton>button {{
#             background-color: #00ADB5;
#             color: white;
#             border-radius: 8px;
#             border: none;
#         }}

#         /* Input fields */
#         input, textarea {{
#             background-color: {card_color} !important;
#             color: {text_color} !important;
#             border: 1px solid {border_color} !important;
#         }}

#         /* Cards (custom markdown blocks) */
#         .custom-card {{
#             background-color: {card_color};
#             padding: 15px;
#             border-radius: 10px;
#             border: 1px solid {border_color};
#             margin-bottom: 10px;
#         }}

#         </style>
#     """, unsafe_allow_html=True)