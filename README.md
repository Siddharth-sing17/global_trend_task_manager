# Global Trend - Task Management App

This is a full-stack Task Management Web Application developed as part of the Skill Assessment for the Global Trend Internship. The application allows users to manage daily tasks with a clean and responsive interface.

## Project Overview
The app is built using the Django framework (Python) and follows the MVT (Model-View-Template) architecture. It supports full CRUD (Create, Read, Update, Delete) operations.

## Features
- **Add New Tasks:** Users can input a task title and description.
- **Task List:** View all tasks in a structured table format.
- **Status Tracking:** Mark tasks as 'Pending', 'In Progress', or 'Completed'.
- **Delete Tasks:** Remove tasks easily from the database.
- **Responsive UI:** Designed to work on desktop and mobile screens.
- **Database:** Uses SQLite for persistent data storage.

## Tech Stack
- **Backend:** Python, Django
- **Frontend:** HTML, CSS (Custom Styling)
- **Database:** SQLite (Default Django DB)

## Setup & Installation Instructions

To run this project locally on your computer, follow these steps:

1. Clone the Repository
   Open your terminal and run:
   git clone https://github.com/Siddharth-sing17/global_trend_task_manager.git
   cd global_trend_task_manager

2. Install Django
   Make sure you have Python installed, then run:
   pip install django

3. Setup Database
   Create the database tables by running migrations:
   python manage.py makemigrations
   python manage.py migrate

4. Run the Server
   Start the local development server:
   python manage.py runserver

5. Access the Application
   Open your web browser and go to:
   http://127.0.0.1:8000/

## Project Structure
- global_trend/ (Project Settings)
- tasks/ (Main Application Logic)
  - migrations/ (Database changes)
  - templates/tasks/ (HTML Files)
  - models.py (Database Schema)
  - views.py (Backend Logic)
  - urls.py (Routing)
- manage.py (Django Utility)
- db.sqlite3 (Database File)

---
**Submission By:** Siddharth Singh
**For:** Global Trend Full Stack Developer Internship
