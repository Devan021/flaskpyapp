# Flask CRUD Application with MongoDB

![Flask Logo](https://www.creativefabrica.com/wp-content/uploads/2021/09/27/AI-logo-design-vector-Graphics-17915917-1-580x369.jpg)

This is a straightforward Flask application that offers CRUD (Create, Read, Update, Delete) operations to manage user records in a MongoDB database through a REST API.

## Table of Contents

- [Setup](#setup)
  - [Prerequisites](#1-prerequisites)
  - [Clone the Repository](#2-clone-the-repository)
  - [Create a Virtual Environment (Optional)](#3-create-a-virtual-environment-optional)
  - [Install Dependencies](#4-install-dependencies)
  - [Configure MongoDB](#5-configure-mongodb)
- [Running the Application](#running-the-application)
- [API Endpoints](#api-endpoints)
- [Testing with Postman](#testing-with-postman)
- [Screenshots](#screenshots)
- [Contributing](#contributing)
- [License](#license)

## Setup

### 1. Prerequisites

Before getting started, make sure you have the following prerequisites installed:

- Python 3.x (You can download it from [python.org](https://www.python.org/downloads/))
- MongoDB (You can download it from [mongodb.com](https://www.mongodb.com/try/download/community))

### 2. Clone the Repository

Clone this repository to your local machine:

```bash
git clone https://github.com/your-username/your-repo.git
cd your-repo
````

### 3. Create a Virtual Environment (Optional)
  Although optional, it's recommended to use a virtual environment to isolate your project's dependencies:

```bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows, use 'venv\Scripts\activate'
```

### 4. Install Dependencies
Install the necessary Python dependencies for this project:

```bash
Copy code
pip install -r requirements.txt
```

### 5. Configure MongoDB

Ensure your MongoDB server is up and running.
Open app.py and update the MongoDB URI and database name as follows:
python

```bash
Copy code
app.config['MONGO_URI'] = 'mongodb://localhost:27017/your_database_name'
````

### Running the Application
To start the Flask application, use the following command:

```bash
Copy code
python app.py
```
The application will start and be accessible at http://localhost:5000.

### API Endpoints

GET /users: Retrieve a list of all users.
GET /users/<id>: Retrieve a specific user by ID.
POST /users: Create a new user with JSON data.
PUT /users/<id>: Update a user by ID with JSON data.
DELETE /users/<id>: Delete a user by ID.
Testing with Postman
You can use Postman, a popular API testing tool, to test the CRUD operations on user records. Import the provided Postman collection for a more straightforward testing experience.

### Postman Collection

### Screenshots
Include screenshots or videos here showing the testing process and results.

### Contributing
We welcome contributions! If you find issues or have improvements to suggest, please feel free to open issues or submit pull requests.

License
```
This project is licensed under the MIT License. See the LICENSE file for details.
```
