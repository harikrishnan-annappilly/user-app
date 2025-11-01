# User Authentication API (Flask + SQLAlchemy)

This API provides endpoints for user registration, login, and listing all users. Data is stored in a SQLite database using SQLAlchemy ORM.

## Base URL

```
http://localhost:5000/api/
```

## Endpoints

### 1. Create User

-   **URL:** `/api/create_user`
-   **Method:** `POST`
-   **Request Body (JSON):**
    ```json
    {
        "username": "string",
        "password": "string"
    }
    ```
-   **Responses:**
    -   `201 Created`: User created successfully
        ```json
        { "message": "User created successfully." }
        ```
    -   `400 Bad Request`: Missing fields or user already exists
        ```json
        { "error": "Username and password required" }
        { "error": "User already exists" }
        ```

### 2. Login User

-   **URL:** `/api/login`
-   **Method:** `POST`
-   **Request Body (JSON):**
    ```json
    {
        "username": "string",
        "password": "string"
    }
    ```
-   **Responses:**
    -   `200 OK`: Login successful
        ```json
        { "success": true, "message": "Login successful" }
        ```
    -   `401 Unauthorized`: Invalid password
        ```json
        { "success": false, "error": "Invalid password" }
        ```
    -   `404 Not Found`: User not found
        ```json
        { "success": false, "error": "User not found" }
        ```

### 3. Show All Users

-   **URL:** `/api/users`
-   **Method:** `GET`
-   **Response:**
    -   `200 OK`: List of all usernames
        ```json
        { "users": ["user1", "user2", ...] }
        ```

## Notes

-   All endpoints accept and return JSON.
-   Passwords are stored in plain text (for demo purposes only).
-   The database file is `users.db` in the project directory.

---

For frontend usage and more features, see the main application code.
