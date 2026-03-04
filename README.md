# HRMS – Human Resource Management System (DRF)

A simple Django REST Framework (DRF) based backend API for managing employees and tracking attendance records.

---

## Tech Stack

- Python  
- Django  
- Django REST Framework  
- SQLite (default database)  
- CORS Headers  

---

## Features

- Employee CRUD operations  
- Attendance tracking (Present / Absent / Leave)  
- Department management  
- Employee-wise attendance filtering  
- Automatic timestamps (`created_at`, `updated_at`)  

---

## Installation & Setup

### Clone the Repository

```bash
git clone https://github.com/prachikush16/hrms-drf.git
cd hrms-drf
```

If connecting an existing local project to GitHub:

```bash
git remote add origin https://github.com/prachikush16/hrms-drf.git
git branch -M main
git push -u origin main
```

---

### Create Virtual Environment

```bash
python -m venv venv
```

Activate it:

**Windows**
```bash
venv\Scripts\activate
```

**Mac/Linux**
```bash
source venv/bin/activate
```

---

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

### Apply Migrations

```bash
python manage.py migrate
```

---

### Run Development Server

```bash
python manage.py runserver
```

Server will run at:

```
http://127.0.0.1:8000/
```

---

---

## Author

**Prachi Kushwah**  
GitHub: https://github.com/prachikush16