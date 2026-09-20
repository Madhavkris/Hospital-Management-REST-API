# Hospital Management REST API

A modular **Hospital Management REST API** built using **Python, Flask, SQLAlchemy, and MySQL**. The project provides APIs for managing patients, doctors, departments, and appointments using a layered backend architecture.

## 🚀 Features

* **Patient management**

  * Create patient
  * Retrieve all patients
  * Retrieve patient by ID
  * Update patient
  * Delete patient

* **Doctor management**

  * Create doctor
  * Retrieve all doctors
  * Retrieve doctor by ID
  * Update doctor
  * Delete doctor

* **Department management**

  * Create department
  * Retrieve all departments
  * Retrieve department by ID
  * Update department

* **Appointment management**

  * Create appointment
  * Retrieve all appointments
  * Retrieve appointment by ID
  * Update appointment
  * Delete appointment

* RESTful API endpoints

* JSON request and response handling

* HTTP status code handling

* SQLAlchemy ORM for database operations

* MySQL relational database

* Foreign-key relationships between entities

* SQLAlchemy relationships using `relationship()` and `back_populates`

* Transaction handling using `commit()` and `rollback()`

* Modular Flask Blueprint architecture

* Service-layer separation for database/business operations

## 🛠️ Technologies Used

* **Python**
* **Flask**
* **SQLAlchemy**
* **MySQL**
* **Flask-SQLAlchemy**
* **REST API**
* **Git & GitHub**
* **Postman** for API testing

## 📂 Project Structure

```text
Hospital-Management-REST-API/
│
├── app.py
├── requirements.txt
├── .gitignore
├── README.md
│
├── database/
│   └── connection.py
│
├── models/
│   ├── patient_model.py
│   ├── doctor_model.py
│   ├── department_model.py
│   └── appointments_model.py
│
├── services/
│   ├── patient_service.py
│   ├── doctor_service.py
│   ├── department_service.py
│   └── appointment_service.py
│
└── routes/
    ├── patient_route.py
    ├── doctor_route.py
    ├── department_route.py
    └── appointment_route.py
```

## 🏗️ Architecture

The application follows a layered architecture:

```text
Client / Postman
       ↓
Flask Routes / Blueprints
       ↓
Service Layer
       ↓
SQLAlchemy ORM
       ↓
MySQL Database
```

### Routes Layer

Handles:

* HTTP methods
* URL/path parameters
* Request JSON
* HTTP responses
* Status codes

### Service Layer

Handles:

* Database operations
* Creating and retrieving ORM objects
* Updating existing records
* Deleting records
* Transactions and rollback handling

### Models Layer

Defines the database entities and relationships using SQLAlchemy ORM.

## 🗄️ Database Relationships

The project contains four main entities:

```text
Department
    │
    └──< Doctors
              │
              └──< Appointments >── Patient
```

### Main Relationships

* One Department can have many Doctors.
* One Doctor can have many Appointments.
* One Patient can have many Appointments.
* An Appointment belongs to one Patient and one Doctor.

These relationships are implemented using SQLAlchemy `relationship()` and `back_populates`.

## 🔗 API Endpoints

### Patients

| Method | Endpoint                     | Description       |
| ------ | ---------------------------- | ----------------- |
| GET    | `/api/patients/`             | Get all patients  |
| GET    | `/api/patients/<patient_id>` | Get patient by ID |
| POST   | `/api/patients/`             | Create patient    |
| PUT    | `/api/patients/<patient_id>` | Update patient    |
| DELETE | `/api/patients/<patient_id>` | Delete patient    |

### Doctors

| Method | Endpoint                   | Description      |
| ------ | -------------------------- | ---------------- |
| GET    | `/api/doctors/`            | Get all doctors  |
| GET    | `/api/doctors/<doctor_id>` | Get doctor by ID |
| POST   | `/api/doctors/`            | Create doctor    |
| PUT    | `/api/doctors/<doctor_id>` | Update doctor    |
| DELETE | `/api/doctors/<doctor_id>` | Delete doctor    |

### Departments

| Method | Endpoint                           | Description          |
| ------ | ---------------------------------- | -------------------- |
| GET    | `/api/departments/`                | Get all departments  |
| GET    | `/api/departments/<department_id>` | Get department by ID |
| POST   | `/api/departments/`                | Create department    |
| PUT    | `/api/departments/<department_id>` | Update department    |

### Appointments

| Method | Endpoint                             | Description           |
| ------ | ------------------------------------ | --------------------- |
| GET    | `/api/appointments/`                 | Get all appointments  |
| GET    | `/api/appointments/<appointment_id>` | Get appointment by ID |
| POST   | `/api/appointments/`                 | Create appointment    |
| PUT    | `/api/appointments/<appointment_id>` | Update appointment    |
| DELETE | `/api/appointments/<appointment_id>` | Delete appointment    |

## 📋 Example Request

### Create Patient

**POST**

```text
/api/patients/
```

Request body:

```json
{
    "patient_name": "Ravi Kumar",
    "age": 25,
    "gender": "Male",
    "disease": "Fever"
}
```

### Update Patient

**PUT**

```text
/api/patients/1
```

Request body:

```json
{
    "patient_name": "Ravi Kumar",
    "age": 26,
    "gender": "Male",
    "disease": "Diabetes"
}
```

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/Madhavkris~~~~/Hospital-Management-REST-API.git
```

```bash
cd Hospital-Management-REST-API
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure the database

Create a MySQL database and configure the database connection using environment variables.

Example `.env`:

```env
DATABASE_URL=mysql+pymysql://username:password@localhost/hospital
```

**Do not commit your `.env` file to GitHub.**

### 5. Run the application

```bash
python app.py
```

The API will be available at:

```text
http://127.0.0.1:5000
```

## 🧪 API Testing

The API can be tested using **Postman**.

The project currently uses HTTP methods including:

```text
GET
POST
PUT
DELETE
```

Responses use appropriate HTTP status codes such as:

```text
200 OK
201 Created
400 Bad Request
404 Not Found
500 Internal Server Error
```

## 🔐 Environment Variables

Sensitive configuration should be stored in environment variables rather than directly in the source code.

Example:

```env
DATABASE_URL=your_database_connection_string
```

Add the following to `.gitignore`:

```text
.env
venv/
__pycache__/
*.pyc
```

## 📚 What I Learned

This project was built to strengthen practical backend development skills, including:

* Building REST APIs with Flask
* Designing API routes
* Using Flask Blueprints
* Working with SQLAlchemy ORM
* Mapping Python classes to database tables
* Working with primary keys and foreign keys
* Managing one-to-many relationships
* Using `relationship()` and `back_populates`
* Performing CRUD operations
* Managing database transactions
* Handling `commit()` and `rollback()`
* Working with JSON request data
* Using HTTP status codes
* Separating routes, services, models, and database configuration

## 🔮 Future Improvements

Planned improvements include:

* PATCH / partial update endpoints
* Improved request validation
* Centralized API error handling
* Query parameter filtering
* Pagination
* Authentication and JWT authorization
* Automated testing with Pytest
* Swagger / OpenAPI documentation
* Docker and Docker Compose
* Improved serialization and response schemas

## 👨‍💻 Author

**Madhav Krishna**

Electronics and Communication Engineering Student

Interested in **Python Backend Development, REST APIs, SQL, and Software Engineering**.

---
⭐ If you find this project useful, feel free to explore the repository and provide feedback.
