# API for Toy Shop
This project represents an online store, specifically catering to handmade toys. 
It's developed to offer a wide range of toy products  for convenient and enjoyable online shopping experiences.

# Project Overview
The "ToyShopAPI" is a web application designed to provide users with access to a vast selection of toy products. 
Users can browse through various toy categories, add items to their cart, and proceed with purchases seamlessly.
Additionally, the API offers user registration and login functionalities to enhance user engagement and personalization.
## Features

- Browse products catalog categorized into different sections.
- Add products to wishlist and manage them.
- Checkout and place orders.
- User registration and login functionalities.
- View order history to track previous purchases.

# Endpoints

#### Documentation page: http://134.209.85.64/api/doc/swagger/

![img.png](images%2Fimg.png)
![img_1.png](images%2Fimg_1.png)
![img_2.png](images%2Fimg_2.png)

## Technologies Used

The "ToyShopAPI" project is developed using the following technologies:

- Django: Python-based web framework for building web applications.
- Database: PostgreSQL

## Usage Instructions

Python must be already installed.

1. **Installation:**
    - Clone the repository to your local machine `https://github.com/IlyaGrynyshyn/toy-shop-API`.
    - Create virtual environment `python3 -m venv venv`
    - Install the required dependencies using `pip install -r requirements.txt`.

2. **Running:**
    - Apply migrations `python manage.py migrate`
    - Start the server with `python manage.py runserver`.
    - Access the store via `http://localhost:8000` in your web browser.

3. **Registration/Login:**
    - To access all functionalities of the project, create super user and log in to your account.

## Test User
   - login: admin@admin.com
   - password: admin


## Developer Commands

- `python manage.py makemigrations`: Create database migrations.
- `python manage.py migrate`: Apply migrations to the database.
- `python manage.py createsuperuser`: Create a site administrator.

## Contribution

If you have ideas or would like to contribute to the project, please fork the repository and create a pull request.
