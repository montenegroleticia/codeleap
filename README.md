# CodeLeap Project

This project implements a basic CRUD (Create, Read, Update, Delete) application using Django and Django REST Framework (DRF).

The application manages a `Person` model with the following fields:

- **id**: Auto-generated primary key
- **username**: String field representing the user's name
- **created_datetime**: Auto-generated datetime field when a record is created
- **title**: String field representing the title of a post
- **content**: Text field representing the content of a post

## Prerequisites

Ensure you have the following installed on your system:

- Python 3.8+
- pip
- Virtualenv

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/montenegroleticia/codeleap
   cd codeleap
   ```

2. Create and activate a virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Apply migrations to set up the database:

   ```bash
   python3 manage.py makemigrations
   python3 manage.py migrate
   ```

5. Run the development server:

   ```bash
   python3 manage.py runserver
   ```

6. Access the application:
   - API Endpoint: [http://127.0.0.1:8000](http://127.0.0.1:8000)

## Running Tests

To run the test, use the following command:

```bash
python3 manage.py test
```

## Linting with Flake8

This project uses Flake8 for linting. To run Flake8:

```bash
flake8
```

## API Endpoints

### 1. Create a Person

- **URL**: `/api/persons/`
- **Method**: POST
- **Request Body**:
  ```json
  {
    "username": "Test",
    "title": "My First Post",
    "content": "This is the content of the post."
  }
  ```
- **Response**:
  ```json
  {
    "id": 1,
    "username": "Test",
    "created_datetime": "2024-12-31T17:56:32.807687Z",
    "title": "My First Post",
    "content": "This is the content of the post."
  }
  ```

### 2. Read All Persons

- **URL**: `/api/persons/`
- **Method**: GET
- **Response**:
  ```json
  [
    {
      "id": 1,
      "username": "Test",
      "created_datetime": "2024-12-31T17:56:32.807687Z",
      "title": "My First Post",
      "content": "This is the content of the post."
    }
  ]
  ```

### 3. Read a Single Person

- **URL**: `/api/persons/<id>/`
- **Method**: GET

### 4. Update a Person

- **URL**: `/api/persons/<id>/`
- **Method**: PATCH
- **Request Body**:
  ```json
  {
    "title": "Updated Title",
    "content": "Updated content."
  }
  ```

### 5. Delete a Person

- **URL**: `/api/persons/<id>/`
- **Method**: DELETE

## Additional Notes

- **Django Admin**: The `Person` model is registered in the Django Admin for easy data management.
- **Database**: SQLite is used as the default database.
- **Django REST Framework**: DRF is used to expose the CRUD functionality via APIs.
