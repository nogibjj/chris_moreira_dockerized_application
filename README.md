# Dockerized Application: Reporting Deffective Parts
[![Build and Push Docker Image](https://github.com/nogibjj/chris_moreira_dockerized_application/actions/workflows/build.yml/badge.svg)](https://github.com/nogibjj/chris_moreira_dockerized_application/actions/workflows/build.yml)
# Project Purpose
This project demonstrates the functionality of Python Flask as a lightweight web framework and its integration with front-end development in a Dockerized environment. The application serves as a simple tool for reporting defective parts, allowing users to fill out a form with their name, employee ID, selected part, and the cause of the defect. If the user selects "Something else" as the defect cause, they are prompted to provide additional details. While this project is not yet connected to a database or cloud application, it focuses on creating a front-end user interface. The app leverages Docker Hub to containerize and distribute the application, making it portable and easy to run. The structure and layout of the app are defined in the form.html file located in the templates folder.

# Take a look at the app
![image](https://github.com/user-attachments/assets/e04f14c0-3aa3-4b45-a502-92154456b546)
![image](https://github.com/user-attachments/assets/29f8bec8-dde2-4445-9e00-3f1a69fd8e06)
# Tools
- **Docker Hub**: Used to containerize the Flask application, enabling seamless sharing and deployment. The app's Docker image is built locally and pushed to Docker Hub, allowing others to easily pull and run it.
- **Flask**: Serves as the core framework for building the web application, managing user input through a dynamic form and displaying a confirmation message upon submission.
- **HTML**: Defines the structure and visual layout of the user interface, including input fields, dropdown menus, and the submit button, ensuring an interactive and user-friendly experience.

# Project File Structure
```css
chris_moreira_dockerized_application/
├── app.py
├── Dockerfile
├── LICENSE
├── Makefile
├── README.md
├── requirements.txt
├── templates/
│   └── form.html
└── .github/
    └── workflows/
        └── build.yml
```

# Process Flow for the Project
![image](https://github.com/user-attachments/assets/3c8a1faa-15ee-484f-83da-fd43ab521e35)

