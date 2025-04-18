# 🛡️ Cyberbullying Detection System using VADER

A web application that detects **harassment or toxic comments** using the **VADER Sentiment Analysis Algorithm**. Users posting harmful content are **automatically blocked**, but can be **unblocked manually** via an intuitive interface.

Built using:
- ⚙️ Python + Flask
- 🧠 VADER Sentiment Analysis
- 🎨 HTML + CSS + JavaScript

---

## 🎯 Features

- ✅ Real-time comment sentiment analysis
- 🚫 Auto-blocks usernames with offensive comments
- 🔄 “Unblock a User” button opens a toggleable form
- 📝 Form clears automatically after submission
- ⏳ Smooth processing animation for unblock
- 🧼 Clean, colorful and dynamic UI

---

## 🧠 How It Works

1. User submits a **username** and **comment**
2. Comment is passed through **VADER sentiment analyzer**
3. If comment is **toxic/harassing** (compound score ≤ -0.5):
   - The user is **blocked**
   - A warning is displayed
4. Blocked users can be **manually unblocked** using a form
5. All transitions are animated and the UI is smooth

---


---

## 📦 Setup Instructions

### 🔧 1. Clone the Repository

```bash
git clone https://github.com/your-username/cyberbully-detector.git
cd cyberbully-detector


### 💽 2. Install Required Libraries
Make sure you have Python 3 installed.

pip install flask vaderSentiment


### ▶️ 3. Run the App

python app.py


📜 License
MIT License. Free to use and modify.



👨‍💻 Author
Manivel
🎓 Final Year CSE Student, Anna University
💬 Passionate about meaningful tech + web apps

🌟 Support
If you like this project, feel free to ⭐ it and share it with friends!


---

Would you like me to export this as a `.md` file and include screenshots or icons for real use? Or zip the full project with this included?



