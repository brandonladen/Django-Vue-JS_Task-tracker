# TodoApp

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)
- [Setup and Installation](#setup-and-installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Contributing](#contributing)
- [License](#license)

## Introduction

TodoApp is a task management application designed to help users manage their daily tasks efficiently. The application allows users to create, read, update, and delete tasks. It features a user-friendly interface with modals for adding and editing tasks.

## Features

- User authentication (login/logout)
- Create new tasks
- View a list of tasks
- Edit existing tasks
- Delete tasks
- Responsive design

## Technologies Used

- **Frontend:**
  - Vue.js 3
  - Vuex
  - Vue Router
  - Axios

- **Backend:**
  - Django (Django REST framework)

- **Other:**
  - HTML5
  - CSS3
  - JavaScript (ES6+)

## Project Structure

TodoApp/
├── backend/                   # Django backend project
│   ├── app/                   # Django app for managing tasks
│   ├── manage.py              # Django management script
│   └── ...                    # Other Django project files
├── frontend/                  # Vue.js frontend project
│   ├── public/                # Public assets
│   ├── src/                   # Source files
│   │   ├── components/        # Vue components
│   │   │   ├── CreateTaskModal.vue
│   │   │   ├── EditTaskModal.vue
│   │   │   └── ...
│   │   ├── store/             # Vuex store
│   │   ├── views/             # Vue views
│   │   │   ├── Home.vue
│   │   │   └── ...
│   │   ├── App.vue            # Root component
│   │   ├── main.js            # Entry point
│   │   └── ...
│   ├── package.json           # NPM dependencies
│   └── ...
└── README.md                  # Project README


## Setup and Installation

### Prerequisites

- Node.js and npm
- Python and pip
- Django
- Vue CLI

### Backend Setup

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/TodoApp.git
    cd TodoApp/backend
    ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv venv
    source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
    ```

3. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

4. Apply migrations and start the server:
    ```sh
    python manage.py migrate
    python manage.py runserver
    ```

### Frontend Setup

1. Navigate to the frontend directory:
    ```sh
    cd ../frontend
    ```

2. Install the dependencies:
    ```sh
    npm install
    ```

3. Start the development server:
    ```sh
    npm run serve
    ```

## Usage

1. Ensure both the backend and frontend servers are running.
2. Open your web browser and navigate to `http://localhost:8080` to access the TodoApp.
3. You can register a new account, log in, and start managing your tasks.

## API Endpoints

### Authentication

- **POST** `/api/auth/login/` - User login
- **POST** `/api/auth/register/` - User registration
- **POST** `/api/auth/logout/` - User logout

### Tasks

- **GET** `/api/app/view/` - Get all tasks
- **POST** `/api/app/view/` - Create a new task
- **PUT** `/api/app/view/{id}/` - Update an existing task
- **DELETE** `/api/app/view/{id}/` - Delete a task

## Contributing

We welcome contributions from the community! To contribute:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and ensure they are well tested.
4. Commit your changes with descriptive commit messages.
5. Push your changes to your forked repository.
6. Open a pull request to the main repository.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
