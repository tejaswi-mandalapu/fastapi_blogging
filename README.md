# FastAPI Blogging 🚀

A lightweight blogging backend built with **FastAPI**, **SQLAlchemy**, and **PostgreSQL**, featuring user authentication, CRUD for posts and comments, and JWT-powered security.

---

## Table of Contents

- [Features](#features)  
- [Tech Stack](#tech-stack)  
- [Getting Started](#getting-started)  
  - [Prerequisites](#prerequisites)  
  - [Installation](#installation)  
  - [Database Setup](#database-setup)  
  - [Environment Variables](#environment-variables)  
  - [Running the App](#running-the-app)  
- [API Documentation](#api-documentation)  


---

## Features

- User registration & login (JWT-based auth)  
- Create, read, update, and delete blog posts  
- Commenting functionality with moderation  
- Role-based access controls (e.g. admin vs regular users)  
- Built with asynchronous FastAPI & Pydantic  

---

## Tech Stack

- **FastAPI** – web framework  
- **SQLAlchemy (Async)** – ORM for database interactions  
- **PostgreSQL** – relational database    
- **Pydantic** – data validation  
- **JWT (PyJWT)** – authentication  

---

## Getting Started

### Prerequisites

- Python 3.9+  
- PostgreSQL 12+

---

### Installation

1. Clone the repo:
	git clone https://github.com/tejaswi-mandalapu/fastapi_blogging.git
   	cd fastapi_blogging

2. Create & activate a virtual environment:
	python3 -m venv venv
	source venv/bin/activate  # macOS/Linux
	venv\Scripts\activate     # Windows

3. Install dependencies.txt
	pip install -r requirements.txt


### Environment Variables

1. Create a .env in the root folder with:
	DATABASE_URL=postgresql+asyncpg://user:password@localhost/blogdb
	JWT_SECRET=your_jwt_secret_here
	ACCESS_TOKEN_EXPIRE_MINUTES=30

### Running the App

1. Run via Uvicorn:
	uvicorn app.main:app --reload

### API Documentation

1. Interactive Swagger UI is available at:
	http://127.0.0.1:8000/docs



	
