# 🎓 Udemy Free Course Telegram Bot

> Automated Python bot that monitors public RSS feeds to detect free Udemy courses and sends real-time notifications directly to Telegram.

Built with a practical, automation-first mindset, this project demonstrates real-world scripting skills commonly used in systems engineering and DevOps environments.

---

## 📌 Overview

Finding high-quality free courses can be time-consuming.  
This bot automates the process by continuously scanning public RSS feeds and instantly notifying the user whenever a new free course is published.

The project focuses on **efficiency, simplicity, and real-world usability** rather than academic examples.

---

## 🚀 Key Features

✅ Automatic detection of newly published free courses  
✅ Instant Telegram notifications  
✅ Duplicate prevention system  
✅ Lightweight and fast execution  
✅ Beginner-friendly yet production-oriented architecture  

---

## 🧠 Technical Skills Demonstrated

This project showcases practical abilities in:

- API consumption (Telegram Bot API)
- Automation scripting
- Data parsing (RSS feeds)
- Event-driven workflows
- Git version control
- Dependency management
- Clean project structuring

These are core skills for roles in:

👉 Systems Administration  
👉 Cybersecurity  
👉 DevOps  
👉 Cloud Engineering  

---

## 🛠 Tech Stack

| Technology | Purpose |
|------------|------------|
| Python | Core scripting language |
| feedparser | RSS data extraction |
| requests | HTTP communication |
| Telegram Bot API | Notification system |
| Git & GitHub | Version control |

---

## ⚙️ Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/diegofonterosa/udemy-free-course-bot.git
cd udemy-free-course-bot

2️⃣ Create a virtual environment
python -m venv venv


Activate it:

Windows

venv\Scripts\activate


Linux / Mac

source venv/bin/activate

3️⃣ Install dependencies
pip install feedparser requests

4️⃣ Configure your Telegram credentials

Open bot.py and replace:

TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
CHAT_ID = "YOUR_CHAT_ID"


⚠️ Never expose real tokens in public repositories.

5️⃣ Run the bot
python bot.py


Once running, you will automatically receive Telegram alerts whenever new free courses are detected.

🔐 Security Note

Credentials should ideally be stored using environment variables rather than hardcoded values.

Future versions of this project will implement secure credential handling.

🔮 Roadmap / Future Improvements

Planned enhancements include:

Docker containerization

Cloud deployment (24/7 uptime)

Environment variable support

Course filtering by category

Database integration

Multi-source aggregation

Web dashboard

🎯 Why This Project Matters

This is not just a tutorial script — it reflects the type of automation engineers build to eliminate repetitive tasks.

Projects like this demonstrate initiative, problem-solving ability, and a practical understanding of modern technical workflows.

👨‍💻 Author

Diego Pérez
ASIR Student | Future Cybersecurity & Systems Specialist

Passionate about automation, infrastructure, and security-oriented technologies.

⭐ If you found this project useful...

Consider giving it a star ⭐
It helps the repository gain visibility!


---
