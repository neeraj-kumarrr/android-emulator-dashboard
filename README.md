# AdStacks Media - Python Intern Assignment
##How to run Script##
=================================
# 1. Navigate to project directory
cd Adstacks_project

# 2. Start Django server (in first terminal)
python manage.py runserver

# 3. Run the Android simulator (in second terminal)
python manage.py shell
>>> from adstacks.android_simulator import AndroidSimulator
>>> simulator = AndroidSimulator()
>>> simulator.start_emulator()  # Starts virtual device
>>> exit()  # To exit shell
##how to install app##
===================================
# In Django shell or script:
simulator.install_app("/path/to/your/app.apk")

# Example with test APK:
simulator.install_app("sample.apk")  # Place APK in project root first

# Expected output:
"Installing sample.apk..."
"Installation successful"

##system information logged##
======================================
system_info = simulator.get_system_info()
print(system_info)

# Project Overview
A Django-based backend system with Android emulator integration that demonstrates:
- RESTful API development
- Database management
- Virtual Android system simulation
- Secure client-server communication

# Key Features

## Backend API System

 *CRUD Operations* for Android apps:
- `POST /api/add-app/` - Add new app
- `GET /api/get-app/<id>/` - Retrieve app details
- `DELETE /api/delete-app/<id>/` - Remove app


*Database Models*:
- `AndroidApp` model with fields:
  ```python
  app_name = models.CharField(max_length=100)
  version = models.CharField(max_length=50)
  description = models.TextField()