# User Authentication App (Flask)

This application provides both API endpoints and a minimal frontend for user registration, login, and listing users. User data is stored in a Python dictionary (in-memory, not persistent).

## Base URLs

-   API: `http://localhost:5000/api/`
-   Frontend: `http://localhost:5000/`

## API Endpoints

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

## Frontend Endpoints

The app also provides a simple web interface using Bootstrap-based templates:

-   `/` — Home page
-   `/register` — Register a new user
-   `/login` — Login as a user
-   `/users` — Show all users

## Notes

-   All API endpoints accept and return JSON.
-   User data is not persistent and will be lost when the server restarts.
-   For persistent storage, use a database-backed version.

---

For more details, see the main application code and the `templates` folder.
