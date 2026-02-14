import streamlit as st
import pandas as pd

# --- Page Config ---
st.set_page_config(page_title="FitPlan AI", page_icon="🏋️‍♂️", layout="wide")

# --- Custom Styling ---
st.markdown("""
    <style>
    .stApp { background-color: #0E1117; color: white; }
    [data-testid="stSidebar"] { background-color: #161B22 !important; }
    .stButton > button { width: 100%; border-radius: 8px; font-weight: bold; background: linear-gradient(45deg, #00F260, #0575E6); color: white; border: none; }
    .metric-card { background-color: #1c2128; padding: 15px; border-radius: 10px; border: 1px solid #30363d; }
    </style>
    """, unsafe_allow_html=True)

# --- Initialize Session State ---
if 'user_data' not in st.session_state:
    st.session_state.user_data = {
        'name': '', 'age': 25, 'height': 0.0, 'weight': 0.0,
        'goal': 'Build Muscle', 'level': 'Beginner', 'equip': ['No Equipment']
    }
if 'profile_complete' not in st.session_state:
    st.session_state.profile_complete = False
if 'edit_mode' not in st.session_state:
    st.session_state.edit_mode = True 

# --- Helper Functions ---
def calculate_bmi(w, h_cm):
    if h_cm > 0:
        return round(w / ((h_cm / 100) ** 2), 2)
    return 0

def get_bmi_cat(bmi):
    if bmi < 18.5: return "Underweight", "🔵"
    if bmi < 25: return "Normal", "🟢"
    if bmi < 30: return "Overweight", "🟠"
    return "Obese", "🔴"

# --- Sidebar Navigation ---
with st.sidebar:
    st.markdown("<h1 style='color: #00F260;'>🏋️‍♀️ FitPlan AI</h1>", unsafe_allow_html=True)
    st.markdown("---")
    menu = st.radio("MENU", ["👤 Profile", "📊 Dashboard", "📈 Health Metrics"])
    st.markdown("---")
    if st.session_state.profile_complete:
        st.success("✅ Profile Synced")
    else:
        st.warning("⚠️ Profile Incomplete")

# --- NAVIGATION LOGIC ---

if menu == "👤 Profile":
    st.title("👤 Profile")
    
    if st.session_state.profile_complete and not st.session_state.edit_mode:
        st.info("Your profile is synced! View your progress in the Dashboard.")
        
        # Display Static Data in Cards
        c1, c2, c3 = st.columns(3)
        with c1: st.markdown(f'<div class="metric-card"><b>Name:</b><br>{st.session_state.user_data["name"]}</div>', unsafe_allow_html=True)
        with c2: st.markdown(f'<div class="metric-card"><b>Goal:</b><br>{st.session_state.user_data["goal"]}</div>', unsafe_allow_html=True)
        with c3: st.markdown(f'<div class="metric-card"><b>Level:</b><br>{st.session_state.user_data["level"]}</div>', unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("✏️ Edit Profile"):
            st.session_state.edit_mode = True
            st.rerun()

    else:
        with st.form("profile_form"):
            st.markdown("### Stats")
            u_name = st.text_input("Name", value=st.session_state.user_data['name'])
            
            col1, col2, col3 = st.columns(3)
            u_age = col1.number_input("Age", min_value=1, max_value=120, value=st.session_state.user_data['age'])
            u_height = col2.number_input("Height (cm)", min_value=0.0, value=st.session_state.user_data['height'])
            u_weight = col3.number_input("Weight (kg)", min_value=0.0, value=st.session_state.user_data['weight'])
            
            u_goal = st.selectbox("Fitness Goal", ["Build Muscle", "Weight Loss", "Strength Gain", "Abs Building", "Flexible"], 
                                  index=["Build Muscle", "Weight Loss", "Strength Gain", "Abs Building", "Flexible"].index(st.session_state.user_data['goal']))
            
            u_equip = st.multiselect("Equipment", ["Dumbbells", "Barbell", "Kettlebell", "Resistance Band", "Yoga Mat", "Full Gym", "No Equipment"],
                                     default=st.session_state.user_data['equip'])
            
            u_level = st.select_slider("Experience", options=["Beginner", "Intermediate", "Advanced"], 
                                       value=st.session_state.user_data['level'])

            if st.form_submit_button("⚡ Sync & Save Profile"):
                if u_name and u_height > 0 and u_weight > 0:
                    st.session_state.user_data = {
                        'name': u_name, 'age': u_age, 'height': u_height, 'weight': u_weight,
                        'goal': u_goal, 'level': u_level, 'equip': u_equip
                    }
                    st.session_state.profile_complete = True
                    st.session_state.edit_mode = False
                    st.success("Profile saved successfully!")
                    st.rerun()
                else:
                    st.error("Please fill in Name, Height, and Weight correctly.")

elif menu == "📊 Dashboard":
    if not st.session_state.profile_complete:
        st.warning("Please complete your **Profile** first.")
    else:
        ud = st.session_state.user_data
        st.title(f"Dashboard: {ud['name']} 🥊")
        
        bmi = calculate_bmi(ud['weight'], ud['height'])
        cat, icon = get_bmi_cat(bmi)
        
        m1, m2, m3, m4 = st.columns(4)
        m1.metric("BMI", f"{bmi}")
        m2.metric("Category", f"{icon} {cat}")
        m3.metric("Goal", ud['goal'])
        m4.metric("Age", ud['age'])
        
        st.markdown("---")
        
        # --- Innovative Visual Modules ---
        left_col, right_col = st.columns([2, 1])
        
        with left_col:
            st.subheader("🚀 Goal Consistency Forecast")
            # Creating dummy data for the graph
            chart_data = pd.DataFrame({
                'Days': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
                'Performance %': [40, 55, 45, 70, 85, 90, 100]
            })
            st.area_chart(chart_data.set_index('Days'))
            
        with right_col:
            st.subheader("🏁 Level Progress")
            progress_map = {"Beginner": 33, "Intermediate": 66, "Advanced": 100}
            current_progress = progress_map.get(ud['level'], 0)
            st.write(f"Level: **{ud['level']}**")
            st.progress(current_progress / 100)
            
            st.markdown("<br>", unsafe_allow_html=True)
            st.markdown(f"""
            <div class="metric-card">
                <b>Equipment Checklist:</b><br>
                <small>{", ".join(ud['equip'])}</small>
            </div>
            """, unsafe_allow_html=True)

elif menu == "📈 Health Metrics":
    if not st.session_state.profile_complete:
        st.error("Setup profile to see analytics.")
    else:
        ud = st.session_state.user_data
        bmi = calculate_bmi(ud['weight'], ud['height'])
        cat, icon = get_bmi_cat(bmi)
        
        st.title("📈 Health Analysis")
        
        # BMI Gauge-like progress bar
        st.write(f"BMI Score: **{bmi}**")
        st.progress(min(bmi/40, 1.0))
        
        st.info(f"Classification: **{cat}** {icon}")
        
        # Calculation for ideal weight
        h_m = ud['height'] / 100
        ideal_low = round(18.5 * (h_m**2), 1)
        ideal_high = round(24.9 * (h_m**2), 1)
        
        st.markdown(f"""
        ### 💡 AI Insights
        * To stay in the **Normal** range, your weight should be between **{ideal_low}kg and {ideal_high}kg**.
        * Based on your goal of **{ud['goal']}**, your metabolic age is approximately **{ud['age'] - 2 if bmi < 25 else ud['age'] + 2}**.
        """)
