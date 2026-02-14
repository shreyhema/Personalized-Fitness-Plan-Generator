#  FitPlan AI: Personalized Fitness Plan Generator
## Milestone 1: Front-End Development

###  Objective of the Milestone
The objective of Milestone 1 is to build the core foundation of the FitPlan AI application. This phase focuses on:
- **User Interface:** Creating Personalized Fitness tracking using Streamlit.
- **Data Collection:** Capturing essential health and fitness parameters including Name, Age, Height, Weight, and Goals.
- **Health Logic:** Implementing accurate BMI calculations and standard health classifications.
- **Persistence:** Ensuring user data is saved and editable throughout the application session using session state.
- **Deployment:** Hosting a functional version on Hugging Face Spaces.

---

###  BMI Formula & Logic
Body Mass Index (BMI) is calculated as a measure of relative weight based on an individual's mass and height.

1. **Unit Conversion:** The application captures height in centimeters ($cm$). It is converted to meters ($m$) for the formula:
   $$m = \frac{cm}{100}$$

2. **The Formula:**
   $$BMI = \frac{Weight (kg)}{Height (m)^2}$$

3. **Classification:**
   Results are rounded to **two decimal places** and categorized according to standard health guidelines:
   - **Underweight:** BMI < 18.5
   - **Normal:** 18.5 ≤ BMI < 25.0
   - **Overweight:** 25.0 ≤ BMI < 30.0
   - **Obese:** BMI ≥ 30.0

---

###  Steps Performed
1. **Form Creation:** Developed a responsive profile form with input validation for health and fitness details.
2. **Input Validation:** Implemented checks to ensure Name, Height, and Weight are provided and non-negative.
3. **BMI & Analytics Logic:** Built a backend engine to automate unit conversions and health classifications.
4. **State Management:** Used `st.session_state` to allow users to navigate between Profile and Dashboard without losing data, including an "Edit Profile" feature.
5. **Deployment:** Deployed the application to **Hugging Face Spaces**.

---

###  Technologies Used
- **Frontend/Backend:** Streamlit
- **Data Visualization:** Pandas
- **Deployment:** Hugging Face Spaces
- **Version Control:** GitHub

---

###  Live Application Link
**[View FitPlan AI on Hugging Face Spaces](https://huggingface.co/spaces/Shrey0405/Fitplan)**

---

###  Application Gallery

#### **1. Initial Setup**
*The clean, unpopulated form ready for user input.*
![Initial Form](Milstone 1/Screenshot/form_empty.png)

#### **2. Data Entry & Profile Syncing**
*Capturing user stats and confirming the profile is successfully synced.*
![Filled Form](Milstone 1/Screenshot/form_filled.png)
![Synced Profile](Milstone 1/Screenshot/profile_synced.png)

#### **3. Professional Dashboard**
*A summary showing calculated BMI, category, and goal consistency charts.*
![Dashboard](Milstone 1/Screenshot/dashboard.png)

#### **4. Deep-Dive Health Analysis**
*AI-driven insights regarding ideal weight ranges and metabolic age.*
![Health Analysis](Milstone 1/Screenshot/health_metrics.png)

---
