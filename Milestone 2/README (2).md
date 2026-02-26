# 🏋️‍♂️ FitPlan AI: Personalized Fitness Plan Generator
### Milestone 2: Core AI Model Integration

**FitPlan AI** is a dynamic fitness assistant that transforms user metrics into actionable, high-performance workout routines. This milestone focuses on the integration of a structured generation model to provide personalized 5-day fitness plans.

---

## 🎯 Milestone Objective
The primary goal of Milestone 2 was to implement the **Core AI Model Integration**. This involved:
* Processing user-specific data (BMI, Age, Fitness Level).
* Constructing dynamic prompts based on available equipment and goals.
* Generating structured 5-day workout sequences.
* Deploying the functional logic to a cloud environment (Hugging Face Spaces).

##  Model Information
* **Model Type:** Logic-Driven Generation Engine.
* **Core Logic:** The application utilizes a `workout_generator` function that acts as a deterministic model, mapping specific user goals (Build Muscle, Weight Loss, Strength Gain, etc.) to optimized training protocols.
* **Inference Method:** Dynamic Template Mapping based on user profile context.

## 📝 Prompt Design Explanation
The system uses a **Context-Aware Prompt Construction** method. The input is not just a goal, but a multi-variable profile:
1. **User Identity:** Name and Age for personalization.
2. **Physical Profile:** Height and Weight are used to calculate **BMI**, which adjusts the plan's context.
3. **Constraint Logic:** "Available Equipment" acts as a filter to ensure the generated exercises are actually possible for the user.
4. **Goal Alignment:** The model selects from five distinct architectural paths (e.g., Hypertrophy for Muscle Build vs. Metabolic Conditioning for Weight Loss).

---

## Implementation Steps

1. **Model Loading:** Integrated a robust generation function into the Streamlit lifecycle.
2. **Prompt Creation:** Developed `prompt_builder.py` logic to synthesize Name, BMI, Goal, Level, and Equipment into a single generation request.
3. **Inference Testing:** Validated the model with three distinct scenarios:
    * **Scenario 1:** Beginner | Weight Loss | No Equipment.
    * **Scenario 2:** Advanced | Build Muscle | Full Gym.
    * **Scenario 3:** Intermediate | Flexibility | Yoga Mat.
4. **UI Styling:** Implemented a Dark Mode UI with custom CSS for plan readability.

---
## Deployment
The application is live and functional on Hugging Face Spaces:
**[REPLACE_WITH_YOUR_HF_SPACES_LINK]**
---

## 📊 Sample Generated Output

**User:** John Doe  
**Goal:** Build Muscle  
**BMI Category:** Normal  

> **➡️ Day 1: Chest (Push)**
> - Focus on the "stretch and squeeze" of the pectoral fibers.
> - Barbell Bench Press: 4 sets 6–8 reps.
> - Incline Dumbbell Press: 3 sets 10–12 reps.
> - Chest Dips: 3 sets to Failure.
> - Push-ups: 2 sets Max reps (finisher).

---



