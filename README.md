# Footwear Management System

## Overview
The Footwear Management System is a web-based application built using Django that allows users to manage footwear products, including adding, viewing, updating, and deleting product records. It also enables customers to browse and purchase footwear items, while administrators have full control over the inventory.

This project is ideal for managing a small to medium footwear store, keeping track of stock, and handling customer orders.

## Features
- **Admin Panel:** Allows administrators to add, edit, and delete footwear products.
- **User Interface:** A clean interface for customers to view, search, and purchase products.
- **Product Management:** Admins can manage product details including name, description, price, size, color, and image.
- **Image Handling:** Products can have images, supported by the Pillow library for image file processing.
- **CRUD Operations:** Users can perform Create, Read, Update, and Delete operations on footwear products.

## Technologies Used
- **Django:** Web framework for building the application.
- **Python:** Programming language used to write the backend logic.
- **HTML/CSS:** Used for the frontend design.
- **SQLite:** Default database for the project (can be changed to PostgreSQL, MySQL, etc. if required).
- **Pillow:** Library for handling image files (for product images).


## Project Structure
footwear-management-system/
│
├── footwear/              
│   ├── migrations/        
│   ├── models.py          
│   ├── views.py          
│   ├── admin.py           
│   ├── urls.py           
│   └── templates/         
│
├── manage.py              
├── requirements.txt       
└── footwear_management_system/  
    ├── __init__.py
    ├── settings.py      
    ├── urls.py         
    └── wsgi.py 

## Installation Instructions

### Prerequisites
- Python 3.x installed
- Django 3.x or later installed
- Pillow library for image processing

### Steps to Set Up the Project

1. **Clone the Repository:**

   Clone the project repository to your local machine:

   ```bash
   git clone https://github.com/rutujakale111/footwear-management-system.git

2. **Navigate to the Project Folder:**

cd footwear-management-system
Create and Activate a Virtual Environment:

**Create a virtual environment (optional but recommended):**

python -m venv env
Activate the virtual environment:

**On Windows:**

.\env\Scripts\activate
**On macOS/Linux:**

source env/bin/activate

**Install the Required Dependencies:**

Install the required libraries listed in requirements.txt (you may need to create this file if it doesn't exist):

pip install -r requirements.txt
If Pillow is not listed, install it manually:

python -m pip install Pillow
Apply Migrations:


Run the following command to set up the database:
python manage.py makemigrations
python manage.py migrate
Create a Superuser (Admin):

## Create an admin user to access the Django admin panel:

python manage.py createsuperuser
Follow the prompts to create the user.

## Run the Development Server:

## Start the Django development server:

python manage.py runserver
The application should now be accessible at http://127.0.0.1:8000/ in your web browser.

## Access the Admin Panel:

Go to http://127.0.0.1:8000/admin/ and log in using the admin credentials you created earlier to manage footwear products.