# 🏋️‍♂️ FitPlan AI: Personalized Fitness Plan Generator
## Milestone 1: Front-End Development 

### 🎯 Objective of the Milestone
The objective of Milestone 1 is to build the core foundation of the FitPlan AI application. This phase focuses on:
- **User Interface:** Creating a professional, "app-like" experience using Streamlit.
- **Data Collection:** Capturing essential health and fitness parameters from the user.
- **Health Logic:** Implementing accurate BMI calculations and standard health classifications.
- **Persistence:** Ensuring user data is saved and editable throughout the application session.
- **Deployment:** Hosting a functional version on Hugging Face Spaces for stakeholder review.

---

### 🧮 BMI Formula & Logic
Body Mass Index (BMI) is calculated as a measure of relative weight based on an individual's mass and height.

1. **Unit Conversion:** The application captures height in centimeters ($cm$). To comply with the standard formula, it is converted to meters ($m$):
   $$m = \frac{cm}{100}$$

2. **The Formula:**
   The BMI is then calculated using the standard metric formula:
   $$BMI = \frac{Weight (kg)}{Height (m)^2}$$

3. **Classification:**
   Results are rounded to **two decimal places** and categorized according to WHO standards:
   - **Underweight:** BMI < 18.5
   - **Normal:** 18.5 ≤ BMI < 25.0
   - **Overweight:** 25.0 ≤ BMI < 30.0
   - **Obese:** BMI ≥ 30.0

---

### 🛠️ Steps Performed

1. **Form Creation:** - Developed a responsive profile form using `st.form`.
   - Included fields for Name, Age, Height (cm), Weight (kg), Fitness Goal, Equipment Access (multi-select), and Experience Level.
2. **Input Validation:** - Implemented logic to check for empty "Name" fields.
   - Added validation to ensure Height and Weight are positive numerical values, preventing calculation errors.
3. **BMI & Analytics Logic:** - Integrated Python logic to automate conversions and classifications.
   - Built a "Dashboard" module to visualize the results using metric cards and progress charts.
4. **State Management:** - Used `st.session_state` to allow the "Profile," "Dashboard," and "Health Metrics" sections to share data without resetting on navigation.
   - Implemented an "Edit Profile" feature to toggle between viewing and updating stats.
5. **Deployment:** - Configured `requirements.txt` for the Streamlit environment.
   - Deployed the application to **Hugging Face Spaces**.

---

### 💻 Technologies Used
- **Frontend/Backend:** Streamlit (Python-based framework)
- **Data Analysis:** Pandas (for consistency forecasting charts)
- **Deployment:** Hugging Face Spaces
- **Version Control:** GitHub

---

### 🔗 Live Application Link
**[View FitPlan AI on Hugging Face Spaces](https://huggingface.co/spaces/Shrey0405/Fitplan)**

---

###  Application Gallery


#### **1. Initial Setup**
*The clean, unpopulated form ready for user input.*
![Initial Form](Milestone1/form_empty.png)

#### **2. Data Entry & Profile Syncing**
*Capturing user stats and confirming the profile is successfully synced with the system.*
![Filled Form](Milestone1/form_filled.png)
![Synced Profile](Milestone1/profile_synced.png)

#### **3. Professional Dashboard**
*A high-level summary showing the calculated BMI (24.44), category (Normal), and progress charts.*
![Dashboard](Milestone1/dashboard.png)

#### **4. Deep-Dive Health Analysis**
*AI-driven insights regarding weight ranges and metabolic age based on the calculated BMI.*
![Health Analysis](Milestone1/health_metrics.png)

---
)
