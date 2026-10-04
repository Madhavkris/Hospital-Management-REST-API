# Hospital Management REST API

A modular **Hospital Management REST API** built using **Python, Flask, SQLAlchemy, and MySQL**.

The project manages patients, doctors, departments, and appointments through RESTful APIs using a layered backend architecture.

---

## 🚀 Features

### Patient Management
- Create patient
- Retrieve all patients
- Retrieve patient by ID
- Update patient
- Partially update patient
- Delete patient
- Filter patients using query parameters

### Doctor Management
- Create doctor
- Retrieve all doctors
- Retrieve doctor by ID
- Update doctor
- Partially update doctor
- Delete doctor
- Filter doctors using query parameters

### Department Management
- Create department
- Retrieve all departments
- Retrieve department by ID
- Update department
- Partially update department
- Filter departments using query parameters

### Appointment Management
- Create appointment
- Retrieve all appointments
- Retrieve appointment by ID
- Update appointment
- Partially update appointment
- Delete appointment
- Filter appointments using query parameters

### Backend Features
- RESTful API design
- JSON request and response handling
- HTTP status code handling
- Request validation
- Query parameter filtering
- SQLAlchemy ORM
- MySQL database
- Foreign-key relationships
- SQLAlchemy `relationship()` and `back_populates`
- Database transactions
- `commit()` and `rollback()` handling
- Flask Blueprint architecture
- Service-layer separation
- Layered project structure
- Postman API testing

---

## 🛠️ Technologies Used

- **Python**
- **Flask**
- **Flask-SQLAlchemy**
- **SQLAlchemy**
- **MySQL**
- **REST API**
- **Git & GitHub**
- **Postman**

---

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
├── routes/
│   ├── patient_route.py
│   ├── doctor_route.py
│   ├── department_route.py
│   └── appointment_route.py
│
└── utils/
    ├── patient_validation.py
    ├── doctor_validation.py
    ├── department_validation.py
    └── appointment_validation.py
```

---

## 🏗️ Architecture

The application follows a layered architecture:

```text
Client / Postman
       ↓
Flask Routes / Blueprints
       ↓
Validation Layer
       ↓
Service Layer
       ↓
SQLAlchemy ORM
       ↓
MySQL Database
```

### Routes Layer

Handles:

- HTTP methods
- URL/path parameters
- Query parameters
- JSON request data
- HTTP responses
- HTTP status codes

### Validation Layer

Handles:

- Required fields
- Data types
- Empty values
- Numeric validation
- Date and time validation
- PUT and PATCH validation

### Service Layer

Handles:

- Database operations
- Creating ORM objects
- Retrieving records
- Updating records
- Deleting records
- SQLAlchemy queries
- Transactions
- Rollback handling

### Models Layer

Defines database entities and their relationships using SQLAlchemy ORM.

---

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

- One Department can have many Doctors.
- One Doctor can have many Appointments.
- One Patient can have many Appointments.
- One Appointment belongs to one Patient.
- One Appointment belongs to one Doctor.

These relationships are implemented using SQLAlchemy `relationship()` and `back_populates`.

---

# 🔗 API Endpoints

## Patients

| Method | Endpoint | Description |
|---|---|---|
| GET | `/api/patients/` | Get all patients |
| GET | `/api/patients/<patient_id>` | Get patient by ID |
| POST | `/api/patients/` | Create patient |
| PUT | `/api/patients/<patient_id>` | Replace patient data |
| PATCH | `/api/patients/<patient_id>` | Partially update patient |
| DELETE | `/api/patients/<patient_id>` | Delete patient |

### Patient Filtering

```text
GET /api/patients/?gender=Male
```

```text
GET /api/patients/?age=21
```

```text
GET /api/patients/?disease=Fever
```

Multiple filters can be combined:

```text
GET /api/patients/?gender=Male&age=21&disease=Fever
```

The supplied filters are combined using `AND`.

---

## Doctors

| Method | Endpoint | Description |
|---|---|---|
| GET | `/api/doctors/` | Get all doctors |
| GET | `/api/doctors/<doctor_id>` | Get doctor by ID |
| POST | `/api/doctors/` | Create doctor |
| PUT | `/api/doctors/<doctor_id>` | Replace doctor data |
| PATCH | `/api/doctors/<doctor_id>` | Partially update doctor |
| DELETE | `/api/doctors/<doctor_id>` | Delete doctor |

### Doctor Filtering

```text
GET /api/doctors/?specialization=Cardiology
```

```text
GET /api/doctors/?department_id=2
```

Multiple filters:

```text
GET /api/doctors/?department_id=2&specialization=Cardiology
```

---

## Departments

| Method | Endpoint | Description |
|---|---|---|
| GET | `/api/departments/` | Get all departments |
| GET | `/api/departments/<department_id>` | Get department by ID |
| POST | `/api/departments/` | Create department |
| PUT | `/api/departments/<department_id>` | Replace department data |
| PATCH | `/api/departments/<department_id>` | Partially update department |

### Department Filtering

```text
GET /api/departments/?department_id=1
```

```text
GET /api/departments/?department_name=Cardiology
```

Multiple filters:

```text
GET /api/departments/?department_id=1&department_name=Cardiology
```

---

## Appointments

| Method | Endpoint | Description |
|---|---|---|
| GET | `/api/appointments/` | Get all appointments |
| GET | `/api/appointments/<appointment_id>` | Get appointment by ID |
| POST | `/api/appointments/` | Create appointment |
| PUT | `/api/appointments/<appointment_id>` | Replace appointment data |
| PATCH | `/api/appointments/<appointment_id>` | Partially update appointment |
| DELETE | `/api/appointments/<appointment_id>` | Delete appointment |

### Appointment Filtering

```text
GET /api/appointments/?patient_id=1
```

```text
GET /api/appointments/?doctor_id=2
```

```text
GET /api/appointments/?status=Booked
```

```text
GET /api/appointments/?appointment_date=2026-10-05
```

Multiple filters:

```text
GET /api/appointments/?doctor_id=2&status=Booked
```

```text
GET /api/appointments/?patient_id=1&doctor_id=2&appointment_date=2026-10-05
```

---

# 🔍 Path Parameters vs Query Parameters

### Path Parameter

Used to identify a specific resource.

```text
GET /api/patients/5
```

Here `5` identifies the patient.

### Query Parameter

Used to filter the collection.

```text
GET /api/patients/?gender=Male
```

Here `gender=Male` tells the API how to filter the patients.

General pattern:

```text
Path parameter  → Which resource?
Query parameter → How should the resources be filtered?
```

Only the first query parameter uses `?`.

Additional query parameters use `&`.

Correct:

```text
/api/patients/?age=21&gender=Male
```

Incorrect:

```text
/api/patients/?age=21&?gender=Male
```

---

# 📋 Example Requests

## Create Patient

### POST

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

---

## Update Patient

### PUT

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

---

## Partial Update Patient

### PATCH

```text
/api/patients/1
```

Request body:

```json
{
    "disease": "Diabetes"
}
```

Only the supplied field is updated.

---

# ⚠️ Validation and Error Handling

The API validates incoming request data before performing database operations.

Examples of validation include:

- Required fields
- String validation
- Integer validation
- Positive ID validation
- Age range validation
- Date validation
- Time validation
- Empty value validation

Query parameters are also validated and converted when necessary.

For example:

```text
/api/patients/?age=abc
```

returns:

```text
400 Bad Request
```

because the age must be an integer.

### HTTP Status Codes

The project uses status codes including:

```text
200 OK
201 Created
400 Bad Request
404 Not Found
500 Internal Server Error
```

---

# 🔄 PUT vs PATCH

### PUT

Used when replacing the complete resource.

Example:

```text
PUT /api/patients/1
```

All required patient fields must be supplied.

### PATCH

Used when updating only selected fields.

Example:

```text
PATCH /api/patients/1
```

Request:

```json
{
    "age": 26
}
```

Only the age is changed.

---

# ⚙️ Installation and Setup

## 1. Clone the repository

```bash
git clone https://github.com/Madhavkris/Hospital-Management-REST-API.git
```

```bash
cd Hospital-Management-REST-API
```

## 2. Create a virtual environment

```bash
python -m venv venv
```

### Windows

```bash
venv\Scripts\activate
```

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

## 4. Configure the database

Create a MySQL database and configure the database connection using environment variables.

Create a `.env` file locally.

**Do not commit `.env` to GitHub.**

Example configuration:

```env
DB_HOST=localhost
DB_USER=your_username
DB_PASSWORD=your_password
DB_DATABASE=hospital
```

Use your project's actual environment variable names when configuring the application.

## 5. Run the application

```bash
python app.py
```

The API will be available at:

```text
http://127.0.0.1:5000
```

---

# 🧪 API Testing

The API can be tested using **Postman**.

### HTTP methods implemented

```text
GET
POST
PUT
PATCH
DELETE
```

### Example filtering request

```text
GET /api/patients/?gender=Male&age=21
```

### Example invalid request

```text
GET /api/patients/?age=abc
```

Expected response:

```text
400 Bad Request
```

---

# 🔐 Environment Variables

Sensitive configuration should be stored in environment variables rather than directly in the source code.

The `.env` file should **never be committed to GitHub**.

Recommended `.gitignore` entries include:

```text
.env
venv/
.venv/
__pycache__/
*.pyc
.idea/
.vscode/
*.log
```

---

# 📚 What I Learned

This project was built to strengthen practical backend development skills, including:

- Building REST APIs with Flask
- Designing API routes
- Using Flask Blueprints
- Working with SQLAlchemy ORM
- Mapping Python classes to database tables
- Working with primary keys and foreign keys
- Managing one-to-many relationships
- Using `relationship()` and `back_populates`
- Performing CRUD operations
- PUT and PATCH operations
- Request validation
- Query parameter filtering
- Converting and validating query parameters
- Building dynamic SQLAlchemy queries
- Managing database transactions
- Using `commit()` and `rollback()`
- Handling JSON request data
- Using HTTP status codes
- Separating routes, validation, services, models, and database configuration
- Testing APIs using Postman
- Using Git and GitHub for version control

---

# 🗺️ Development Roadmap

Completed:

```text
CRUD Operations                 ✅
Request Validation              ✅
Error Handling                  ✅
Query Parameters & Filtering    ✅
```

Planned:

```text
Pagination                      🔜
Improved Serialization          🔜
JWT Authentication              🔜
Authorization / Roles           🔜
Automated Testing with Pytest   🔜
Swagger / OpenAPI               🔜
Docker & Docker Compose         🔜
Production Deployment           🔜
```

---

# 👨‍💻 Author

**Madhav Krishna**

Electronics and Communication Engineering Student

Interested in:

- Python Backend Development
- REST APIs
- SQL
- Software Engineering

---

⭐ If you find this project useful, feel free to explore the repository and provide feedback.