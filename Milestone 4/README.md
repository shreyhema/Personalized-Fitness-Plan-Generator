# 🏋️‍♂️ FitPlan AI: Personalized Fitness Plan Generator
### Milestone 4: Application Finalization & Deployment

**FitPlan AI** is an all-in-one AI-driven health assistant. In this final milestone, the platform has been evolved from a workout generator into a comprehensive fitness ecosystem, integrating **Personalized Nutrition Plan** and a **Secure Authentication Flow**.

---

## 🎯 Milestone 4 Objectives
The final phase focused on polishing the user experience and ensuring production-readiness:
* **Full Authentication Suite:** Implementation of Signup, Login, and secure **OTP Verification** (including Resend OTP logic).
* **Holistic Health Approach:** Integration of a **Personalized Dietary Plan** generator alongside workout routines.
* **Input Validation:** Robust error handling for age, BMI, and physical metrics to ensure plan accuracy.
* **UI/UX Optimization:** Refined navigation between the User Dashboard and the dynamic Results page.
* **Model Resilience:** Graceful handling of AI inference to ensure 100% uptime of generated plans.

---

## New Feature: Personalized Dietary Plan
Recognizing that fitness is 70% nutrition, FitPlan AI now generates a daily meal structure aligned with the user's specific calorie needs and fitness goals:

| Meal | focus | Sample Dishes |
| :--- | :--- | :--- |
| **Breakfast** | High Protein / Energy | Oats with Whey, Greek Yogurt, or Scrambled Eggs |
| **Lunch** | Complex Carbs & Lean Protein | Grilled Chicken/Tofu with Brown Rice and Greens |
| **Snack** | Metabolic Boost | Almonds, Protein Shake, or Fruit |
| **Dinner** | Recovery & Low Carb | Grilled Fish or Quinoa Salad with Steamed Veggies |

*Includes: Specific calorie counts, optimal eating times, and curated dish suggestions.*

---

## AI Model & Prompt Engineering
The system uses a multi-layered prompt architecture to generate the **Total Transformation Plan**:
1. **User Persona:** Name: `Krish` | BMI: `Normal` | Goal: `Abs Building`.
2. **Workout Logic:** A 5-day split targeting the core with progressive intensity.
3. **Nutritional Logic:** Caloric scaling based on the user's metabolic rate and activity level.

---

## Application Final Walkthrough

* **Secure Access:** The verified OTP login system ensuring user data privacy. 
* **Input Validation:** Clean UI for entering height/weight with real-time BMI feedback. 
* **Final Plan:** The unified view showing both Workout and Dietary plans in a scannable layout. 

---

## 🚀 Final Deployment
The application is fully functional and deployed on Streamlit Cloud and Hugging Face Spaces:
* **Streamlit Clould link:** **[https://fitplan-ai-8qfajtbzuct4mfpjyev4nn.streamlit.app/]**
* **Hugging Face link:** **[https://huggingface.co/spaces/Infoysprojectwork/AI-Fitness-Plan-Generator]**


