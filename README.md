 # PG Management System

A web-based **PG (Paying Guest) Management System** to manage rooms, residents, and bookings efficiently. Built with **Django 6.0**, **Python (latest version)**, and **MySQL**.

---

## 📌 Features

- 🔐 User Registration (New users can create an account)
- 🔑 Secure Login & Logout functionality
- 🛡️ Role-based access control (Admin-only features)
- Add, update, and deactivate residents  
- Room-wise and floor-wise management  
- Track active and available beds  
- Room dashboard showing occupancy status  
- Deactivate residents without deleting data  
- Admin-only views for deactivated residents  
- Responsive and user-friendly interface

---

## 🛠️ Tech Stack

- **Backend:** Python, Django 6.0  
- **Frontend:** HTML, CSS, JavaScript  
- **Database:** MySQL  
- **Dependencies:** Listed in `requirements.txt` (including `mysqlclient`)  
- **Version Control:** Git & GitHub

---

## ⚙️ Installation & Setup

1. **Clone the repository**
```bash
git clone https://github.com/Chandu-AB/PG_Management.git
cd PG_Management


2. **Create and activate virtual environment**

      # Windows
      python -m venv venv
      venv\Scripts\activate
      
      # Linux / Mac
      python3 -m venv venv
      source venv/bin/activate


3. Install dependencies

   pip install -r requirements.txt


4. Set up database

    Install MySQL and create a database (example: pg_management_db)
    
    Update settings.py in your Django project with your MySQL credentials:


  
        DATABASES = {
      'default': {
          'ENGINE': 'django.db.backends.mysql',
          'NAME': 'pg_management_db',
          'USER': 'your_mysql_user',
          'PASSWORD': 'your_mysql_password',
          'HOST': 'localhost',
          'PORT': '3306',
      }
  }

5. Apply migrations:

     python manage.py makemigrations
     python manage.py migrate

6. Create a superuser for admin access:

      python manage.py createsuperuser
      # Follow the prompts to set username, email, and password


7. Run the server:
     python manage.py runserver
     Open your browser and visit: http://127.0.0.1:8000/



⚡ Notes

Only active residents are counted for room availability

Follow the above setup steps carefully to configure MySQL and Django

