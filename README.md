# Flask RESTful API Example

This repository contains a simple RESTful API built using Flask, Flask-RESTful, and Flask-CORS. The API demonstrates basic GET and POST requests to handle and display user data.

## Features

- **GET Request**: Fetches user data stored in the API.
- **POST Request**: Adds user data (name and age) to the API.
- **CORS Support**: Enables cross-origin requests for better integration with frontend applications.

## How It Works

1. **GET `/api`**
   - Returns the user data stored in the API.
   - Response Example:
     ```json
     {
       "nama": "John",
       "umur": "25"
     }
     ```

2. **POST `/api`**
   - Accepts `nama` and `umur` as form data and stores them in the API.
   - Request Example:
     ```json
     {
       "nama": "John",
       "umur": "25"
     }
     ```
   - Response Example:
     ```json
     {
       "msg": "Data berhasil dimasukkan"
     }
     ```

## Prerequisites

Ensure the following are installed:

- Python 3.x
- Flask
- Flask-RESTful
- Flask-CORS

Install dependencies using pip:

```bash
pip install flask flask-restful flask-cors
```

## How to Run

1. Clone the repository:

   ```bash
   git clone https://github.com/your-repo-url
   ```

2. Navigate to the project directory:

   ```bash
   cd your-project-directory
   ```

3. Run the Flask application:

   ```bash
   python app.py
   ```

4. Access the API at:

   - **GET**: [http://127.0.0.1:5005/api](http://127.0.0.1:5005/api)
   - **POST**: Use tools like Postman or cURL to send POST requests.

## Code Overview

### `MembuatAPI` Class

- **GET Method**: 
  - Retrieves the stored `identitas` dictionary containing user data.

- **POST Method**: 
  - Accepts `nama` and `umur` from form data, stores them in the `identitas` dictionary, and returns a success message.

### `api.add_resource`

Maps the `MembuatAPI` class to the `/api` endpoint, supporting both GET and POST methods.

## Example Interaction

1. Start the server:
   ```bash
   python app.py
   ```

2. **POST Request**:
   - URL: [http://127.0.0.1:5005/api](http://127.0.0.1:5005/api)
   - Data:
     ```json
     {
       "nama": "Jane",
       "umur": "30"
     }
     ```
   - Response:
     ```json
     {
       "msg": "Data berhasil dimasukkan"
     }
     ```

3. **GET Request**:
   - URL: [http://127.0.0.1:5005/api](http://127.0.0.1:5005/api)
   - Response:
     ```json
     {
       "nama": "Jane",
       "umur": "30"
     }
     ```
