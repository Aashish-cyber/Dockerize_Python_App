# Django Books Application

## Overview

The Django Books Application is a simple web application for managing and displaying a list of books and their authors. Built with Django, this application provides a clean and straightforward interface to interact with book data.

## Features

- Display a list of books.
- Each book includes details such as title and author.
- Simple and user-friendly web interface.

## Requirements

- Python 3.12+
- Django 5.1+
- Virtual environment (recommended)

## Installation

### Clone the Repository

git clone https://github.com/your-username/django-books-app.git
cd django-books-app

Set Up Virtual Environment

python -m venv venv
source venv/bin/activate


Install Dependencies

pip install -r requirements.txt


Configure the Application

Update ALLOWED_HOSTS: In book_collection/settings.py, add your server's IP address or domain to ALLOWED_HOSTS.
ALLOWED_HOSTS = ['your-public-ip', 'localhost', '127.0.0.1']


Run Migrations

python manage.py makemigrations
python manage.py migrate


Create a Superuser (optional): To access the Django admin panel.
python manage.py createsuperuser

Running the Application

To start the development server and make the application accessible from all network interfaces:

python manage.py runserver 0.0.0.0:8000
You can now access the application in your web browser at http://your-public-ip:8000/.


Directory Structure

book_collection/ - Project settings and configuration.

books/ - Django app for managing book data.

migrations/ - Database migrations for the books app.

__init__.py - Initialization file for the books app.

admin.py - Django admin configuration.

apps.py - Application-specific configuration.

models.py - Data models for books.

tests.py - Test cases for the books app.

urls.py - URL routing for the books app.

views.py - Views for displaying book data.

manage.py - Django management script.

requirements.txt - Project dependencies.



License
This project is licensed under the Apache License 2.0 - see the LICENSE file for details.
