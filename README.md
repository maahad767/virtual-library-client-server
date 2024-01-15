# Virtual Library

## Installation

### Frontend

The frontend is built with React. To install:

1. Navigate to the `frontend` directory
2. Run `npm/bun/yarn install` to install dependencies
3. Run `npm/bun/yarn dev` to start the development server

### Backend

The backend is built with Python and Django and Django Ninja. To install:

1. Navigate to the `backend` directory
2. Run `virtualenv venv` to create virtual environment
3. Run `source venv/bin/activate` to activate the virtual environment
4. Run `poetry install` to install dependencies
5. Run `python manage.py migrate` to create database and tables
6. Run `python manage.py runserver` to start the server

## Features

- Browse books by category or search by title/author/description
- View book details including reviews and ratings
- Add books to share your book with other bookworms, you can charge a rent with a plan
- Leave ratings and reviews for books you've read
- Leave ratings and reviews to a specific copy of a book you rented
- Track a copy with status and order
- Get payments for sharing books
