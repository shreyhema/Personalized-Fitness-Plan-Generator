#  FitPlan AI: Personalized Fitness Plan Generator

## 🚀 Milestone 3: Secure Login & OTP Verification

This milestone introduces a robust authentication layer to protect user data and personalize the dashboard experience. Access is now governed by a multi-step verification process.

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

---

##  Authentication Flow
1.  **User Registration:** User details are validated and saved to the local database.
2.  **Login Attempt:** The app checks the hashed password against the database record.
3.  **OTP Generation:** Upon valid login, a unique 6-digit code is generated.
4.  **Verification:** The code is sent via email; the user must enter this code on the OTP Verification page to unlock the Dashboard.

---

## Deployment
The application is currently configured for local deployment via VS Code:
Local Access URL: **(http://localhost:8501/)**

---

