#Academic Project Management System (SGPA API)

REST API built with **FastAPI** for managing academic projects, users, roles, and project status within a university environment.

---

#Academic Information

**Program:** Systems and Computer Engineering
**Course:** Backend and Database Elective

**Authors**

* Camila Cáceres

---

#Project Overview

The **SGPA (Academic Project Management System)** is designed to centralize and manage academic project information, allowing different roles to interact with the system:

* Students
* Professors
* Coordinators

The system supports project tracking, role management, and structured academic data organization.

---

#Architecture

```bash
app/ │
 ├── config/ # Database configuration 
 ├── models/ # Pydantic schemas
 ├── controllers/ # Business logic
 ├── routes/ # API endpoints
 └── main.py # Application entry point

 #Technologies Used

* Python 3.11
* FastAPI
* PostgreSQL (Neon Database)
* Psycopg2
* Uvicorn
* Postman
* GitHub

#Database

PostgreSQL database hosted on Neon.

Main entities:

* User

* Role

* Project

* Status

Relationships are enforced using foreign keys to ensure data integrity.


Running the Project Locally

1️⃣ Clone the repository
git clone https://github.com/YOUR_USERNAME/ACADEMIC-PROJECT-MANAGEMENT-API.git
cd ACADEMIC-PROJECT-MANAGEMENT-API

2️⃣ Create virtual environment
python -m venv venv
source venv/bin/activate

Windows:

venv\Scripts\activate

Install dependencies
pip install -r requirements.txt

4️⃣ Run the server
uvicorn main:app --reload

API documentation available at:

http://localhost:8000/docs
🧪 API Documentation

Interactive Swagger documentation:

/docs
Main Endpoints
Users

GET /api/users

POST /api/users

PUT /api/users/{id}

DELETE /api/users/{id}

Roles

GET /api/roles

POST /api/roles

Projects

GET /api/projects

POST /api/projects

Status

GET /api/status

POST /api/status

Postman Collection

Import:

postman_collection.json

to test all endpoints quickly.

🌐 Live Deployment

Public API URL:

https://YOUR-DEPLOY-URL/docs

This allows instructors to test the API without local installation.

🔐 Future Improvements

Password hashing with bcrypt

JWT Authentication

Role-based authorization

Frontend integration using Svelte + Tailwind

👩‍💻 Author

Camila Andrea Cáceres Reyes

Academic backend project developed for educational purposes.