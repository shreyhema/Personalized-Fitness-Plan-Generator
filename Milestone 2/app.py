import streamlit as st
import pandas as pd

# --- Generator Logic ---
def workout_generator(prompt, goal, max_new_tokens=1000):
    """
    This function now checks the 'goal' and returns a different 
    plan template for each one to show variety.
    """
    plans = {
        "Build Muscle": """
➡️Day 1: Chest (Push)
- Focus on the "stretch and squeeze" of the pectoral fibers.
- Barbell Bench Press: 4 sets 6–8 reps.
- Incline Dumbbell Press: 3 sets 10–12 reps.
- Chest Dips (Leaning forward): 3 sets Failure.
- Cable Flys (Middle to Low): 3 sets 15 reps.
- Push-ups: 2 sets Max reps (as a finisher).
➡️Day 2: Back (Pull)
-Drive with your elbows to ensure the lats are doing the work, not just your biceps.
- Deadlifts: 3 sets 5 reps (Heavy).
- Pull-Ups (or Lat Pulldowns): 4 sets 8–10 reps.
- Bent-Over Barbell Rows: 3 sets 10 reps.
- Seated Cable Rows: 3 sets 12 reps.
- Face Pulls: 3 sets 15–20 reps (for rear delts and posture).
➡️Day 3: Legs (Lower)
- The most demanding day. Ensure you hit full depth on your movements.
- Barbell Back Squats: 4 sets  8–10 reps.
- Leg Press: 3 sets 12–15 reps.
- Romanian Deadlifts: 3 sets 10–12 reps (for hamstrings).
- Leg Extensions: 3 sets 15 reps.
- Seated Calf Raises: 4 sets 15–20 reps.
➡️Day 4:  Shoulders
- Prioritize the side (lateral) head of the delt for maximum width.
- Overhead Press (Barbell or DB): 4 sets 8–10 reps.
- Lateral Raises (Dumbbell): 4 sets 15–20 reps.
- Front Raises (Plate or DB): 3 sets 12 reps.
- Reverse Pec Deck (Rear Delts): 3 sets 15 reps.
- Dumbbell Shrugs: 3 sets 12 reps.
➡️Day 5:  Arms & Abs
- High volume to force blood into the smaller muscle groups.
- Barbell Curls: 3 sets 10 reps.
- Close-Grip Bench Press: 3 sets 8–10 reps.
- Hammer Curls: 3 sets 12 reps.
- Tricep Rope Pushdowns: 3 sets 15 reps.
- Hanging Leg Raises: 3 sets 15 reps.
- Plank: 3 sets 60 seconds""",
        
        "Weight Loss": """
➡️Day 1: Upper Body (Push)
- Focuses on chest, shoulders, and triceps. 
- Dumbbell Chest Press: 3 sets of 10–12 reps.
- Shoulder Press: 3 sets of 10–12 reps.
- Triceps Pushdowns: 3 sets of 12–15 reps.
- Push-ups: 3 sets to failure.
- Cardio Finisher: 15 minutes of brisk walking.
➡️Day 2: Lower Body
- Focuses on quads, glutes, and hamstrings. 
- Goblet Squats: 3 sets of 12 reps.
- Walking Lunges: 3 sets of 10 reps per leg.
- Romanian Deadlifts: 3 sets of 10 reps.
- Glute Bridges: 3 sets of 15 reps.
- Cardio Finisher: 15 minutes on a cycle or treadmill.
➡️Day 3:  Cardio HIIT
- Designed to spike your heart rate and burn fat quickly. 
- Format: 30 seconds of high intensity (sprint/jumping jacks/burpees) followed by 60 seconds of low intensity (walking).
- Repeat: 10–15 rounds.
- Exercises to Mix: Mountain climbers, burpees, high knees, and skipping rope.
➡️Day 4:   Upper Body (Pull)
- Focuses on the back and biceps. 
- Lat Pulldowns: 3 sets of 10–12 reps.
- Seated Cable Rows: 3 sets of 12 reps.
- Dumbbell Bicep Curls: 3 sets of 12 reps.
- Face Pulls: 3 sets of 15 reps.
- Cardio Finisher: 15 minutes on the rowing machine.
➡️Day 5: Steady-State Cardio & Core
- Lower intensity to promote recovery while still burning calories. 
- Steady Cardio: 35–40 minutes of jogging, swimming, or brisk walking.
- Core Circuit (Repeat 3 times).
- Plank: Hold for 45–60 seconds.
- Russian Twists: 20 reps.
- Bicycle Crunches: 15 reps per side.""",
        
        "Strength Gain": """
➡️Day 1: Full Body Strength
- Focus on hitting every major muscle group in a single, high-intensity session.
- Barbell Squats: 3–5 sets of 5 reps.
- Barbell Bench Press: 3–5 sets of 5 reps.
- Barbell Rows: 3 sets of 6–8 reps.
- Overhead Press: 3 sets of 5–8 reps.
- Deadlifts: 1–3 sets of 5 reps.
➡️Day 2: Lower Body
- Focus on the largest muscles in the body to build massive foundational strength.
- Barbell Squats: 3 sets of 5–8 reps (Main power move).
Romanian Deadlifts: 3 sets of 8–10 reps (Targets hamstrings and glutes).
- Leg Press or Lunges: 3 sets of 10 reps (Builds quad volume).
- Calf Raises: 3 sets of 15 reps (Lower leg stability).
- Plank / Core Work: 3 sets of 60 seconds.
➡️Day 3: Leg Day
hit the main lifts for the second time this week.
Barbell Squats: 5 sets of 5 reps.
Barbell Bench Press: 5 sets of 5 reps.
Barbell Rows: 5 sets of 5 reps.
Dips: 3 sets to failure (for chest and tricep endurance).
Hanging Leg Raises: 3 sets of 15 reps (core strength).
➡️Day 4: Rest & Recovery
Light Walk: 20 mins to boost blood flow.
Stretch: Focus on hips and lower back.
Hydrate: Drink extra water for muscle repair.
Protein: Keep intake high to rebuild tissue.
Sleep: Aim for 8 hours of quality rest.
➡️Day 5: Upper Body
- Dumbbell Shoulder Press: 3 sets × 12 reps (Focus on vertical control).
- Cable Rows: 3 sets × 12–15 reps (Keep chest up, squeeze shoulder blades).
- Face Pulls: 3 sets × 15–20 reps (Great for posture and rear delts).
- Hammer Curls: 3 sets × 12 reps (Targets forearms and biceps).
- Tricep Overhead Extension: 3 sets × 12 reps""",
        
        "Abs Building": """
➡️Day 1: Upper Abs Focus
- Floor Crunch: 3 sets x 20 reps. Targets the upper rectus abdominis.
- Sit-ups: 4 sets x 15 reps. A classic for building core power.
- Toe Touches: 4 sets x 30 reps. Engages the upper abs through targeted flexion.
- Plank: 3 sets x Max Time. Essential for overall core tension.
➡️Day 2: Lower Abs Focus
- Lying Leg Raise: 3 sets x 15 reps. One of the best for lower ab activation.
- Reverse Crunch: 4 sets x 10-15 reps. Focuses on bringing the hips toward the chest.
- Flutter Kicks: 40 seconds. Keeps constant tension on the lower core.
- Scissor Kicks: 4 sets x 30 reps. Mimics walking to engage deep lower muscles.
➡️Day 3: Obliques
- Russian Twists: 4 sets x 20 reps. Key for rotational strength and side-ab definition.
- Side Plank: 30-45 seconds per side. Builds lateral stability.
- Crossbody Mountain Climbers: 30 seconds. Combines cardio with oblique rotation.
- Side Crunches: 40 seconds per side. Directly targets the love handle area.
➡️Day 4: Core Stability
- Bird Dog: 5 reps per side (slowly). Teaches the core to stay stable during movement.
- Plank Shoulder Taps: 40 seconds. Forces the core to resist rotation.
- Superman Hold: 40 seconds. Important for lower back health to support front abs.
- Plank Jacks: 10-15 reps. Adds a cardio element to traditional planking.
➡️Day 5: Total Core Burn
- Bicycle Crunches: 40 seconds. Often cited as the most effective ab exercise.
- V-Ups: 10 reps. An advanced move that hits upper and lower abs simultaneously.
- Mountain Climbers: 30 seconds. Explosive movement for final fat burning.
- High Knees: 30 seconds. Keeps heart rate up to maximize the "afterburn" effect.""",

        "Flexibility": """
➡️Day 1: Full Body Dynamic Mobility
- Neck Rolls: 2 sets of 30 seconds.
- Arm Circles: 2 sets of 20 reps (forward and backward).
- Cat-Cow Stretch: 3 sets of 10 reps to warm up the spine.
- Leg Swings: 2 sets of 15 reps per leg .
- Standing Forward Fold: 3 sets of 20 seconds
➡️Day 2: Hips & Hamstrings
- Downward Dog: 3 sets of 30 seconds for calves and hamstrings.
- Lunge Stretch: 3 sets of 20 seconds per leg to open hip flexors.
- Butterfly Pose: 3 sets of 30 seconds for inner thighs.
- Seated Hamstring Stretch: 3 sets of 30 seconds (lean from hips, not waist).
- Pigeon Pose: 2 sets of 30 seconds per side for deep hip opening.
➡️Day 3: Spine & Upper Body
- Cobra Stretch: 3 sets of 30 seconds for the front body and lower back.
- Child’s Pose: 2 sets of 1 minute for full back relaxation.
- Thread the Needle: 2 sets of 30 seconds per side for upper back rotation.
- Doorway Chest Stretch: 2 sets of 30 seconds to fix "hunched" posture.
- Seated Spinal Twist: 3 sets of 20 seconds per side.
➡️Day 4: Active Flexibility Flow
- Stretch: 1 minute per side (lunge + thoracic twist).
- Dynamic Lunges with Twist: 2 sets of 10 reps.
- Deep Squat Hold: 1–2 minutes (opens ankles and hips).
- Wall Angels: 2 sets of 15 reps for shoulder mobility.
- Standing Side Stretch: 2 sets of 20 seconds per side.
➡️Day 5: Dynamic Stretching
- Sun Salutations: 3 rounds (gentle flow).
- Figure-Four Stretch: 2 minutes per side for glutes.
- Pancake Stretch: 2 sets of 1 minute (legs wide, leaning forward).
- Overhead Triceps Stretch: 30 seconds per side.
- Savasana (Corpse Pose): 3–5 minutes for final relaxation."""
    }
    
    # Return the specific plan for the goal, or a default if not found
    text = plans.get(goal, "### 5-Day General Fitness Plan\nCustomized for your BMI and Age...")
    return [{"generated_text": text}]

# --- Initialize Session State ---
if "user_data" not in st.session_state:
    st.session_state.user_data = None

# --- Page Config ---
st.set_page_config(page_title="FitPlan AI", page_icon="🏋️‍♂️", layout="centered")

# --- Custom Styling ---
st.markdown("""
    <style>
    .stApp { background-color: #0E1117; color: white; }
    .stButton > button { 
        width: 100%; 
        border-radius: 8px; 
        font-weight: bold; 
        background: linear-gradient(45deg, #00F260, #0575E6); 
        color: white; 
        border: none; 
        height: 3em;
    }
    .plan-container { 
        background-color: #1c2128; 
        padding: 20px; 
        border-radius: 10px; 
        border: 1px solid #30363d; 
        margin-top: 20px;
        white-space: pre-wrap;
    }
    .bmi-box {
        text-align: center;
        padding: 10px;
        background-color: #21262d;
        border-radius: 10px;
        border: 1px solid #00F260;
        margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- Helper Functions ---
def calculate_bmi(w, h_cm):
    if h_cm > 0:
        return round(w / ((h_cm / 100) ** 2), 2)
    return None

def get_bmi_cat(bmi):
    if bmi is None: return "Unknown"
    if bmi < 18.5: return "Underweight"
    if bmi < 25: return "Normal"
    if bmi < 30: return "Overweight"
    return "Obese"

# --- SIDEBAR NAVIGATION ---
st.sidebar.title("📌 Navigation")
page = st.sidebar.radio("Go to", ["User Profile", "Personalized Plan"])

# --- SECTION 1: USER PROFILE ---
if page == "User Profile":
    st.markdown("<h1 style='text-align: center; color: #00F260;'>🏋️‍♀️ FitPlan AI</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>Enter your details to get your personalized workout plan</p>", unsafe_allow_html=True)
    st.write("---")

    name = st.text_input("Full Name", placeholder="e.g. John Doe")

    col1, col2, col3 = st.columns(3)
    with col1:
        gender = st.selectbox("Gender", ["Male", "Female", "Non-binary", "Prefer not to say"])
        height = st.number_input("Height (cm)", min_value=0.0, step=1.0, value=170.0)
    with col2:
        age = st.number_input("Age", min_value=1, max_value=120, step=1, value=25)
        weight = st.number_input("Weight (kg)", min_value=0.0, step=0.1, value=70.0)
    with col3:
        goal = st.selectbox("Fitness Goal", ["Build Muscle", "Weight Loss", "Strength Gain", "Abs Building", "Flexibility"])
        fitness_level = st.select_slider("Fitness Level", options=["Beginner", "Intermediate", "Advanced"])

    equipment = st.multiselect("Available Equipment", 
                               ["Dumbbells", "Barbell", "Kettlebell", "Resistance Band", "Yoga Mat", "Full Gym", "No Equipment"])

    bmi = calculate_bmi(weight, height)

    if st.button("Submit Profile & Generate Plan"):
        if not name:
            st.error("Please enter your name.")
        elif not equipment:
            st.error("Please select at least one equipment option.")
        elif bmi is None or height <= 0 or weight <= 0:
            st.error("Please enter valid height and weight.")
        else:
            bmi_status = get_bmi_cat(bmi)
            equipment_list = ", ".join(equipment)

            prompt = f"Plan for {name}, Goal: {goal}, Level: {fitness_level}."

            with st.spinner("Generating your dynamic AI workout plan..."):
                # Notice we pass 'goal' here so the generator knows what to pick
                raw_result = workout_generator(prompt, goal, max_new_tokens=1000)
                result = raw_result[0]["generated_text"]
            
            st.session_state.user_data = {
                "name": name,
                "goal": goal,
                "plan": result,
                "bmi": bmi,
                "bmi_status": bmi_status
            }
            st.success("✅ New Plan Generated! Switch to the 'Personalized Plan' tab.")

# --- SECTION 2: PERSONALIZED PLAN ---
elif page == "Personalized Plan":
    if st.session_state.user_data is None:
        st.warning("⚠️ No plan found. Please go to 'User Profile' and submit your details first.")
    else:
        user = st.session_state.user_data
        
        st.markdown(f"<h1 style='text-align: center; color: #00F260;'>Welcome, {user['name']}!</h1>", unsafe_allow_html=True)
        st.markdown(f"<h3 style='text-align: center;'>Your path to {user['goal']} starts here.</h3>", unsafe_allow_html=True)
        
        st.markdown(f"""
            <div class="bmi-box">
                <p style="margin:0; font-size: 1.1em;"><b>Your BMI:</b> {user['bmi']}</p>
                <p style="margin:0; color: #00F260;"><b>Category:</b> {user['bmi_status']}</p>
            </div>
        """, unsafe_allow_html=True)
        
        st.write("---")
        st.subheader(f"🏋️ Your Personalized 5-Day {user['goal']} Plan")
        
        st.markdown(f'<div class="plan-container">{user["plan"]}</div>', unsafe_allow_html=True)
        
        st.download_button("Download Plan as Text", user["plan"], file_name="workout_plan.txt")
