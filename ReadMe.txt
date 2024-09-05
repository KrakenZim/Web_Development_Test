Web Programming Test
Overview
This project consists of a Python backend using Flask and SQLite, and a Vue.js frontend. The backend fetches data from a RESTful API, stores it in a SQLite database, and serves it via an API endpoint. The Vue.js frontend fetches this data from the backend and displays it.
Below is package that should be installed and how to run it - TLDR - flask run in one terminal(root path) and then npm run serve (from root/frontend/my-vue-app path) should let them both run.

Prerequisites
Python 3.x
Node.js and npm (Node Package Manager)

Create and activate a virtual environment:
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows

Install required Python packages:
pip install -r requirements.txt

Run the Flask server:
python app.py
The server will start at http://127.0.0.1:5000.

Frontend Setup
Navigate to the frontend directory:

cd frontend
Install required Node.js packages:
npm install

Run the Vue.js development server:
npm run serve
The Vue.js app will be available at http://localhost:8080.

Usage

Populating Data:
Open a browser and visit http://127.0.0.1:5000/populate to fetch data from the API and store it in the SQLite database.

Viewing Data:
Navigate to http://localhost:8080 in your browser to view the data fetched from the SQLite database.

Dependencies

Backend:
Flask
Flask-CORS
Requests
SQLite (included in Python’s standard library)

Frontend:
Vue.js
Axios (if used in the project for HTTP requests)

Troubleshooting
If you encounter issues with the API fetch:

Ensure that both the Flask server and Vue.js development server are running.
Check for CORS issues or network errors in the browser console.
If the Flask server is not running:

Verify that Flask is properly installed and there are no errors in the app.py file.

