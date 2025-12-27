 # PG Management System

A web-based **PG (Paying Guest) Management System** to manage rooms, residents, and bookings efficiently. Built with **Django 6.0**, **Python (latest version)**, and **MySQL**.

---

## 📌 Features

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


## 🖼️ Screenshots

**Room Dashboard**  
![Room Dashboard](https://raw.githubusercontent.com/Chandu-AB/PG_Management/main/screenshots/Roomdashboard.png)

**Add Person Page**  
![Add Person](https://raw.githubusercontent.com/Chandu-AB/PG_Management/main/screenshots/Add_person.png)

**Room Details**  
![Room Details](https://raw.githubusercontent.com/Chandu-AB/PG_Management/main/screenshots/Room_details.png)

**Person List (Room-wise)**  
![Person List](https://raw.githubusercontent.com/Chandu-AB/PG_Management/main/screenshots/person_list.png)

**Admin Panel**  
![Admin Panel](https://raw.githubusercontent.com/Chandu-AB/PG_Management/main/screenshots/admin.png)

👤 Admin Access

Superuser can view all residents, including deactivated ones

Manage room availability and active residents

Deactivated residents remain in the database but do not occupy bed counts



⚡ Notes

Only active residents are counted for room availability

Follow the above setup steps carefully to configure MySQL and Django

