# Task Management Dashboard

This project implements a task management dashboard using Django for the backend and HTML, Tailwind CSS, and jQuery for the frontend.
## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Running the Server](#running-the-server)
- [License](#license)

## Features
- CRUD operations for tasks.
- API endpoints for task status queries.
- Real-time task updates with Ajax
- User-friendly UI built with Tailwind CSS
- Responsive design for mobile and desktop

## Installation

### Prerequisites
- Python 3.8+
- Django 4.0+
- pip
- virtualenv

### Steps

1. **How to fork the Repository**
   - Navigate to the [Bolaji18 taskmore repository](https://github.com/Bolaji18/taskmore) on GitHub.
   - Click the "Fork" button in the top-right corner of the page to create a copy of the repository under your GitHub account.

2. **How to clone the Repository**
   ```bash
   git clone https://github.com/Bolaji18/taskmore.git
   cd taskmore
   ```

3. **How to create and Activate a Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

4. **How to install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## Running the Server

1. **Apply Migrations**
   ```bash
   python manage.py makemigrations
   ```
   ```bash
   python manage.py migrate
   ```

2. **Run the Local Server**
   ```bash
   python manage.py runserver
   ```

3. **Access the Application**
   - Open your browser and navigate to `http://127.0.0.1:8000`.

## functions and how to use app
 
1. **Click on user image at the top right corner to go to the login page**

2. **Create new user through the link provided at the bottom of page, fill the input page and login to page**

3. **Click on Addtask to add new task by providing the info on the page**

4. **Delete the task by clicking on the delete icon at the bottom of the task**



## Documentation
After starting the local server enter `http://127.0.0.1:8000/docs/` into your browser to see documentation about the taskmore.