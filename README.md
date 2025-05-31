# Simple Book Library

A simple RESTful API for managing a collection of books, built using **FastAPI**, **SQLModel**, and **SQLite**. This project demonstrates the basics of building CRUD operations using FastAPI with database integration.

---

## Table of Contents

* [Features](#features)
* [Project Structure](#project-structure)
* [Installation](#installation)
* [Running the Server](#running-the-server)
* [API Endpoints](#api-endpoints)

---

## Features

* Add a new book
* Retrieve all books (with pagination)
* Retrieve a single book by ID
* Delete a book by ID
* SQLite database integration

---

## Project Structure

```
Simple-Book-Library/
├── src/
│   ├── routes              # api routes
│       ├── __init__.py     # package file
│       ├── books.py        # routes for books library
│   ├── main.py             # FastAPI app
│   ├── models.py           # Book model using SQLModel
│   ├── database.py         # SQLite database setup and session dependency
│   ├── __init__.py     # package file
├── .gitignore
├── requirements.txt
└── README.md
```

---

## Installation

### Python Version

This project uses **Python 3.12.6**.

### Install Dependencies

1. Clone the repository:

```bash
git clone https://github.com/GiorgiEz/Simple-Book-Library.git
cd Simple-Book-Library/src
```

2. Create a virtual environment (recommended):

```bash
python -m venv venv
source venv\Scripts\activate
```

3. Install the required libraries:

```bash
pip install -r requirements.txt
```

---

## Running the Server

1. Navigate to the `src` folder:

```bash
cd src
```

2. Start the development server:

```bash
fastapi dev main.py
```

This will start the FastAPI server with hot-reloading. By default, visit [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) to view the interactive API docs (Swagger UI).

---

## API Endpoints

| Method | Endpoint      | Description         |
| ------ | ------------- |---------------------|
| POST   | `/books/`     | Add a new book      |
| GET    | `/books/`     | Get all books       |
| GET    | `/books/{id}` | Get a book by ID    |
| DELETE | `/books/{id}` | Delete a book by ID |

