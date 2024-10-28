# Data Type Inference Application

This project is a web application that processes and displays data, focusing on data type inference and conversion for datasets using Python and Pandas. It includes a Django backend and a React frontend for user interaction.

## Table of Contents
- [Project Overview](#project-overview)
- [Requirements](#requirements)
- [Setup Instructions](#setup-instructions)
  - [Backend Setup](#backend-setup)
  - [Frontend Setup](#frontend-setup)
- [Running the Application](#running-the-application)
- [Usage](#usage)
- [Additional Notes](#additional-notes)

## Project Overview

The application comprises the following components:

1. **Pandas Data Type Inference and Conversion**: A Python script capable of inferring and converting data types in datasets imported from CSV or Excel files.
2. **Django Backend Development**: A Django project that incorporates the data processing script, creating models, views, and URLs for handling user interactions.
3. **Frontend Development using React**: A frontend application that allows users to upload files, submit them for processing, and view the processed data.

## Requirements

- Python 3.7 or higher
- Django 3.2 or higher
- React 17 or higher
- Pandas
- Other Python libraries as needed

## Setup Instructions

### Backend Setup

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/HaiderSana338/data-type-inference-app.git
   cd data-type-inference-app
   ```

2. **Create a Virtual Environment**:
   It is recommended to use a virtual environment to manage dependencies.
   ```bash
   python -m venv venv
   ```

3. **Activate the Virtual Environment**:
   - For Windows:
     ```bash
     venv\Scripts\activate
     ```
   - For macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Run Migrations**:
   ```bash
   python manage.py migrate
   ```

6. **Start the Django Development Server**:
   ```bash
   python manage.py runserver
   ```

### Frontend Setup

1. **Navigate to the Frontend Directory**:
   If your frontend code is in a separate directory (e.g., `frontend`), navigate to that directory:
   ```bash
   cd frontend
   ```

2. **Install Node.js Dependencies**:
   Make sure you have Node.js installed. Then, install the required packages:
   ```bash
   npm install
   ```

3. **Start the React Development Server**:
   ```bash
   npm start
   ```

## Running the Application

After starting both the Django and React servers, you should be able to access the application in your web browser at `http://localhost:3000` (React) and `http://localhost:8000` (Django).

## Usage

1. **Upload Data**: Use the frontend interface to upload a CSV or Excel file.
2. **Process Data**: The application will process the file and infer the data types for each column.
3. **View Results**: The processed results will be displayed on the frontend.

## Additional Notes

- Ensure you have the correct permissions to upload files.
- Review the code for detailed comments and documentation.
- For issues and contributions, please open an issue or pull request in the repository.
