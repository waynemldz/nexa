# 🤖 Nexa

> AI-powered WhatsApp virtual assistant built with FastAPI, Python and Google Gemini.

Nexa is a portfolio project that simulates a real customer service assistant for WhatsApp. It combines deterministic conversation flows with generative AI to provide support, answer company-related questions and manage customer interactions.

---

## 🚀 Features

- 📱 WhatsApp integration with `whatsapp-web.js`
- 🤖 AI responses powered by Google Gemini
- 💬 Conversation state management
- 🎫 Human support ticket creation
- 🧠 Company knowledge base
- 📝 Conversation history
- 🗄️ SQLite database with SQLAlchemy
- 🐳 Docker support
- 📚 Interactive API documentation with Swagger

---

## 🛠️ Tech Stack

- Python 3.14
- FastAPI
- SQLAlchemy
- SQLite
- Google Gemini API
- Node.js
- whatsapp-web.js
- Axios
- Docker

---

## 📂 Project Structure

```text
api
│
├── app
│   ├── commands
│   ├── config
│   ├── knowledge
│   ├── models
│   ├── repositories
│   ├── routes
│   └── services
│
├── database.py
├── main.py
├── Dockerfile
└── docker-compose.yml
```

---

## ⚙️ How it Works

```
WhatsApp

        │

        ▼

Node.js (whatsapp-web.js)

        │

        ▼

FastAPI

        │

        ▼

Command Dispatcher

        │
        ├───────────────┐
        │               │
        ▼               ▼

Commands          Google Gemini

        │               │
        └───────┬───────┘
                ▼

           Response
```

The assistant first attempts to identify predefined intents such as:

- Support
- Pricing
- Scheduling
- Menu navigation

If no command matches the user's message, the request is forwarded to Google Gemini, which answers based on the company's knowledge base.

---

## 📖 Conversation Flow

```
User

↓

Main Menu

↓

Pricing
Support
Scheduling

↓

If necessary

↓

AI (Gemini)

↓

Human Support
```

---

## 🧠 AI

The assistant uses Google Gemini together with a local knowledge base (`company.txt`).

The AI only answers questions related to the company.

Unknown questions are gracefully redirected to human support.

---

## 🐳 Running the Project

Clone the repository:

```bash
git clone https://github.com/your-user/nexa.git
```

Navigate to the project:

```bash
cd nexa
```

Start with Docker:

```bash
docker compose up --build
```

The API will be available at:

```
http://localhost:8000
```

Swagger documentation:

```
http://localhost:8000/docs
```

---

## 📌 Future Improvements

- Conversation timeout
- Rich WhatsApp buttons
- Admin dashboard
- Authentication
- PostgreSQL support
- Automated testing
- CI/CD pipeline

---

## 👨‍💻 Author

Wayne Gabriel

GitHub:
https://github.com/seu-usuario

LinkedIn:
https://www.linkedin.com/in/seu-linkedin
