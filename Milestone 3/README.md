# ⚡ FitPlan AI: Personalized Fitness Plan Generator

**FitPlan AI** is a state-of-the-art, intelligence-powered fitness application designed to generate dynamic workout and dietary plans tailored to individual user profiles. Built with a premium aesthetic and a focus on security, the platform ensures that your journey to peak performance is both data-driven and secure.

---

## 🚀 Milestone 3: Secure Login & OTP Verification

The latest update introduces a robust authentication layer to protect user data and personalize the dashboard experience. Access is now governed by a multi-step verification process.

### Key Features
* **Secure Signup:** New users can register with their email and a hashed password stored securely in a local database.
* **Credential Verification:** Sophisticated login logic that verifies user credentials against the database.
* **Multi-Factor Authentication (MFA):** Beyond simple passwords, the app implements a secure 6-digit OTP (One-Time Password) system.
* **Email Integration:** Seamless delivery of verification codes directly to the user's registered email using the SendGrid API.
* **Premium UI/UX:** A cinematic splash screen and a refined "Old Money" aesthetic using custom CSS and high-end typography (Playfair Display & DM Sans).
* **Restricted Access:** The Personal Dashboard and AI Plan Generators are locked behind a successful OTP verification gate.

---

## 🛠️ Technical Stack

| Component | Technology |
| :--- | :--- |
| **Frontend** | Streamlit (Custom CSS Injection) |
| **Backend** | Python 3.x |
| **Database** | SQLite / SQLAlchemy |
| **Security** | JWT (JSON Web Tokens) & PBKDF2 Password Hashing |
| **Email Service** | SendGrid API |
| **AI Engine** | Gemini 1.5 Pro / Flash |

---

## 📦 Installation & Setup

1.  **Clone the Repository**
    ```bash
    git clone [https://github.com/YOUR_USERNAME/FitPlan-AI-Personalized-Fitness-Plan-Generator.git](https://github.com/YOUR_USERNAME/FitPlan-AI-Personalized-Fitness-Plan-Generator.git)
    cd FitPlan-AI-Personalized-Fitness-Plan-Generator
    ```

2.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Configure Environment Variables**
    Create a `.env` file in the root directory and add your credentials:
    ```env
    SENDGRID_API_KEY='your_sendgrid_key_here'
    FROM_EMAIL='your_verified_sender_email'
    GOOGLE_API_KEY='your_gemini_api_key'
    JWT_SECRET='your_random_secret_string'
    ```

4.  **Run the Application**
    ```bash
    streamlit run app.py
    ```

---

## 🛡️ Authentication Flow
1.  **User Registration:** User details are validated and saved to the local database.
2.  **Login Attempt:** The app checks the hashed password against the database record.
3.  **OTP Generation:** Upon valid login, a unique 6-digit code is generated.
4.  **Verification:** The code is sent via email; the user must enter this code on the OTP Verification page to unlock the Dashboard.

---

## 🎨 Visual Identity
The application utilizes a unique **"Noir-Minimalist"** theme:
* **Colors:** Champagne (#F5F0E8), Deep Espresso (#1A1410), and Burnished Gold (#C8A064).
* **Typography:** Playfair Display for headers and DM Mono for technical data points.
* **Animations:** Cinematic splash exits and card-rise effects for a tactile feel.

---
*Developed as part of the FitPlan AI Project Milestone Series — 2026.*

