# 🧾 Invoice & Quotation Management App – CI/CD Deployment

A Python Flask based **Invoice & Quotation Management Application** deployed on **AWS EC2** using a complete **CI/CD pipeline with Jenkins, GitHub, Pytest, Gunicorn and systemd**.

---

## 📌 Project Overview

The main purpose of this project is to develop a simple Invoice & Quotation Management web application and automate its testing, build and deployment process using CI/CD.

The application is developed using **Python and Flask** and provides a professional dashboard for managing invoices, quotations and reports.

The application is hosted on an **AWS EC2 Ubuntu server** and runs using **Gunicorn**.

---

# 🏗️ Architecture Diagram
![](/image/Architecture%20Digram.png)

```text
                    👨‍💻 Developer
                         |
                         |
                       VS Code
                         |
                    git push
                         |
                         v
                  +-------------+
                  |   GitHub    |
                  | Repository  |
                  +-------------+
                         |
                         |
                         v
                  +-------------+
                  |   Jenkins   |
                  |   CI/CD     |
                  +-------------+
                         |
              +----------+----------+
              |                     |
              v                     v
        Checkout Code       Install Dependencies
              |                     |
              +----------+----------+
                         |
                         v
                    Run Pytest
                         |
                    Tests Passed
                         |
                         v
                       Build
                         |
                         v
                  +-------------+
                  |   AWS EC2   |
                  |   Ubuntu    |
                  +-------------+
                         |
                         v
                    Gunicorn
                         |
                         v
                  Flask Application
                         |
                         v
                     Port 5000
                         |
                         v
                     Browser
```
🛠️ Technologies Used
Technology	Purpose
Python	Application development
Flask	Web framework
HTML	Web page structure
CSS	Web page design
Pytest	Automated testing
Git	Version control
GitHub	Source code repository
Jenkins	CI/CD automation
AWS EC2	Cloud server
Ubuntu	Operating system
Gunicorn	Python WSGI application server
systemd	Application service management

```

📁 Project Structure
invoice-quotation-app-CICD-deployment/
│
├── app.py
├── Jenkinsfile
├── requirements.txt
├── README.md
│
├── tests/
│   └── test_app.py
│
└── venv/
```
📄 File Description
app.py

app.py is the main Flask application file.

It contains:

Flask application
Home page
Health check endpoint
HTML and CSS design
Application configuration

Example:
```
from flask import Flask


app = Flask(__name__)


@app.route("/")
def home():
    return "Invoice & Quotation Management App"


@app.route("/health")
def health():
    return "Application is Healthy!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
```

📄 Jenkinsfile

The Jenkinsfile defines the CI/CD pipeline.

The pipeline contains the following stages:

Checkout
Install Dependencies
Run Tests
Build
Post Actions

Pipeline flow:
```
Checkout
    |
    v
Install Dependencies
    |
    v
Run Tests
    |
    v
Build
    |
    v
Deployment
```
📄 requirements.txt

The requirements.txt file contains the Python dependencies required by the application.

Main dependencies include:
```
Flask
Gunicorn
Pytest
Werkzeug
Jinja2
Click
Blinker
```
Dependencies are installed using:
```
pip install -r requirements.txt
🧪 Testing
```
Pytest is used for automated testing.

The project contains tests inside the tests directory.

Test command:
```
python -m pytest
```
Expected result:
```
2 passed
```
Final testing result:

2 passed in 0.14s
🔍 Health Check

The application contains a health check endpoint.

Endpoint:
```
/health
`````
Command:
```
curl http://127.0.0.1:5000/health
```
Expected output:
```
Application is Healthy!
```
The health endpoint is useful for verifying whether the Flask application is running successfully.

🔄 CI/CD Pipeline

CI/CD stands for:
```
CI = Continuous Integration
CD = Continuous Delivery / Deployment
```
The CI/CD pipeline automatically checks the application whenever new code is pushed to GitHub.

🔵 Continuous Integration
![](/image/Screenshot%20(589).png)

Continuous Integration is used to automatically:

Get the latest source code
Install dependencies
Run automated tests
Verify that the application is working correctly
Build the application

Pipeline:
```
GitHub
   |
   v
Jenkins
   |
   v
Checkout Code
   |
   v
Install Dependencies
   |
   v
Run Pytest
   |
   v
Build
```
If the tests fail, the pipeline stops and the later stages are skipped.

🟢 Continuous Deployment

After the required checks are successful, the application can be deployed to the AWS EC2 server.

Deployment architecture:
```
GitHub
   |
   v
Jenkins
   |
   v
AWS EC2
   |
   v
Gunicorn
   |
   v
Flask Application
```
☁️ AWS EC2 Setup

The application is deployed on an AWS EC2 instance.

Server configuration:
```
Operating System : Ubuntu
Application       : Flask
Application Port  : 5000
Application Server: Gunicorn
Deployment Path   : /opt/invoice-app
```
📂 Deployment Directory

The application is stored on the EC2 server at:
```
/opt/invoice-app
```
Navigate to the directory:

```
cd /opt/invoice-app
```
Check project files:
```
ls
```
Expected output:
```
Jenkinsfile
README.md
app.py
requirements.txt
tests
venv
```
🐍 Python Virtual Environment

A Python virtual environment is used to isolate project dependencies.

Create virtual environment:
```
python3 -m venv venv
```
Activate it:
```
source venv/bin/activate
```
Install dependencies:
```
pip install -r requirements.txt
```
🧪 Run Tests on EC2

After deployment, tests can also be executed directly on the EC2 server.

Command:
```
python -m pytest
```
Expected result:
```
2 passed
```
This confirms that the application code and tests are working correctly on the server.

🚀 Gunicorn

Gunicorn is used as the production WSGI server for the Flask application.

Run the application manually:
```
gunicorn --bind 0.0.0.0:5000 app:app
```
Gunicorn listens on:
```
0.0.0.0:5000
```
The application can then be accessed using:
```
http://EC2-PUBLIC-IP:5000
```
⚙️ systemd Service

To keep the application running continuously, a systemd service is used.

Service name:

invoice-app.service

Start the service:
```
sudo systemctl start invoice-app
```
Check service status:
```
sudo systemctl status invoice-app
```
Restart the service:
```
sudo systemctl restart invoice-app
```
Stop the service:
```
sudo systemctl stop invoice-app
```
🔁 Enable Application at Boot

To automatically start the application when the EC2 server starts:
```
sudo systemctl enable invoice-app
```
Check whether the service is enabled:
```
sudo systemctl is-enabled invoice-app
```
Expected output:
```
enabled
```
🔐 Port Configuration

The Flask/Gunicorn application runs on:
```
Port: 5000
`````
The AWS EC2 Security Group should allow inbound traffic for port 5000 if the application needs to be accessed directly from the internet.

Example:
```
Type   : Custom TCP
Port   : 5000
Source : Required client/network
```
🌐 Accessing the Application

After starting the application, open:
```
http://EC2-PUBLIC-IP:5000
```
Example:
```
http://13.201.4.219:5000
```
The browser displays the Invoice & Quotation Management dashboard.

🖥️ Application Dashboard

The application dashboard contains three main sections.

🧾 Invoices

Used for managing customer invoices.

📋 Quotations

Used for creating and managing quotations.

📊 Reports

Used for viewing invoice and quotation records.

⚡ Quick Actions

The dashboard contains buttons for:
```
Create Invoice
Create Quotation
View Reports
```
🔄 Complete Development Process

The complete development process followed in this project is:
```
1. Create Flask Application
          |
          v
2. Create HTML/CSS UI
          |
          v
3. Add Health Check Endpoint
          |
          v
4. Create Automated Tests
          |
          v
5. Create requirements.txt
          |
          v
6. Push Code to GitHub
          |
          v
7. Create Jenkins Pipeline
          |
          v
8. Jenkins Checkout
          |
          v
9. Install Dependencies
          |
          v
10. Run Pytest
          |
          v
11. Build Application
          |
          v
12. Deploy to AWS EC2
          |
          v
13. Run Application using Gunicorn
          |
          v
14. Manage Application using systemd
          |
          v
15. Access Application through Browser
```
🔧 Git Commands Used

Initialize Git repository:
```
git init
```
Check status:
```
git status
```
Add files:
```
git add .
```
Commit changes:
```
git commit -m "updated"
```
Add GitHub remote:
```
git remote add origin <repository-url>
```
Push code:
```
git push -u origin main
```
📥 Clone Project on EC2

Create deployment directory:
```
sudo mkdir -p /opt/invoice-app
```
Change ownership:
```
sudo chown -R ubuntu:ubuntu /opt/invoice-app
```
Navigate to the directory:
```
cd /opt/invoice-app
```
Clone the GitHub repository:
```
git clone https://github.com/vaibhavbhuse42/invoice-quotation-app-CICD-deployment.git .
```
🔄 Jenkins Pipeline Stages
Stage 1: Checkout

Jenkins downloads the latest source code from GitHub.

GitHub → Jenkins
Stage 2: Install Dependencies

Jenkins creates a Python virtual environment and installs the required packages.
```
python3 -m venv .venv
```
Then:
```
pip install --upgrade pip
pip install -r requirements.txt
```
Stage 3: Run Tests

Jenkins runs:
```
python -m pytest
```
If all tests pass, the pipeline continues.

If a test fails, later stages are skipped.

Stage 4: Build

The build stage runs after successful testing.
```
Tests Passed
     |
     v
   Build
   ```
Stage 5: Deployment

The application is deployed to the EC2 server and managed using Gunicorn and systemd.

❌ Error Handling

During development, a test initially failed because the /health route was missing.

The error was:
```
404 NOT FOUND
```
The test expected:
```
Application is Healthy!
```
The health endpoint was then added to the Flask application.

Another test issue occurred when the endpoint returned:
```
OK
```
instead of:
```
Application is Healthy!
```
The response was corrected so that the automated test passed.

Final result:

2 passed
🔥 Port 5000 Issue

During deployment, port 5000 was already being used by another Gunicorn process.

The error was:
```
Address already in use
```
The port was checked using:
```
sudo lsof -i :5000
```
The old Gunicorn process was stopped.

The systemd service was then restarted:

sudo systemctl restart invoice-app

After restarting, Gunicorn successfully listened on:
```
0.0.0.0:5000
```
✅ Final Application Status

The application was successfully deployed and verified.

Service status:
```
Active: active (running)
```
Gunicorn:
```
Listening at: http://0.0.0.0:5000
```
Health check:
```
curl http://127.0.0.1:5000/health
```
Output:
```
Application is Healthy!
```
Automated tests:
```
2 passed
```
Systemd:

enabled
📊 Final CI/CD Flow
```
                  DEVELOPER
                      |
                      v
                  +-------+
                  | VS Code|
                  +-------+
                      |
                  git push
                      |
                      v
                 +---------+
                 | GitHub  |
                 +---------+
                      |
                      v
                 +---------+
                 | Jenkins |
                 +---------+
                      |
             +--------+--------+
             |                 |
             v                 v
        Checkout        Dependencies
             |                 |
             +--------+--------+
                      |
                      v
                   Pytest
                      |
                Tests Passed
                      |
                      v
                    Build
                      |
                      v
                 +---------+
                 | AWS EC2 |
                 +---------+
                      |
                      v
                  Gunicorn
                      |
                      v
                Flask App
                      |
                      v
                  Port 5000
                      |
                      v
                  Browser
```
🎯 Project Objectives

The main objectives of this project are:

Develop a Flask web application
Create a responsive dashboard
Implement automated testing
Use Git and GitHub for version control
Configure Jenkins CI/CD
Deploy the application on AWS EC2
Use Gunicorn as a production server
Use systemd for service management
Verify application health using a health endpoint
📚 Learning Outcomes

Through this project, the following concepts were practiced.

Python
Flask
Virtual environments
Python packages
Pytest
Git
Repository management
Commit
Push
Clone
Branch
Jenkins
Pipeline
Jenkinsfile
Stages
Automated testing
Build automation
AWS
EC2
Ubuntu server
Security Groups
Public IP
Application deployment
Linux
Directory management
Permissions
Process management
systemd services
Port checking
Deployment
Gunicorn
Flask production deployment
Service management
Health monitoring

🧑‍💻 Author

Vaibhav Navnath Bhuse

BCA Student

Project:

Invoice & Quotation Management App – CI/CD Deployment