# Budget Tracker

A simple budget tracker web application built using HTML, CSS, JavaScript, and Flask. This app helps users manage their finances effectively by tracking income and expenses.

## Table of Contents
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Running the Application](#running-the-application)
- [Usage](#usage)

## Features
- Track income and expenses
- View budget summaries
- User-friendly interface
- Responsive design

## Technologies Used
- HTML
- CSS
- JavaScript
- Flask (Python web framework)
- SQLite (for data storage)

## Installation

To set up the project on your local machine, follow these steps:

1. **Clone the repository**:

   ```bash
   git clone https://github.com/fathan-raedaya/budget-tracker.git

2. **Navigate to the project directory**:

   ```bash
   cd budget-tracker
   
3. **Set up a virtual environment (optional but recommended)**:

   ```bash
   python -m venv venv
   
4. **Activate the virtual environment**:
   
   On Windows:
   ```
   venv\Scripts\activate
   ```
   On macOS/Linux:
   ```
   source venv/bin/activate
   ```
6. **Install the required packages**:

   ````bash
   pip install -r requirements.txt

## Running the Application

1. **Set the Flask environment variables (if necessary)**:

   On Windows:
   ```
   set FLASK_APP=app.py
   set FLASK_ENV=development
   ```
   On macOS/Linux:
   ```
   export FLASK_APP=app.py
   export FLASK_ENV=development
   ```
   
1. **Run the Flask application**:
   With virtual environment:
   ```
   flask run
   ```
   Without virtual environment:
   ```
   python -m flask run
   ```

2. **Open your web browser and go to http://127.0.0.1:5000 to view the application.**

## Usage

Upon opening the web application, you can add income, expenses and goal

   
