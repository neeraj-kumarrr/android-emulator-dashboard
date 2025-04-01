# AdStacks Media - Python Intern Assignment

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