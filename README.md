# 🚀 User Authentication App (Flask)

Welcome to the **User Authentication App**! 🎉 This project lets you register, log in, and view users with a super simple API and a modern, minimal frontend. All data is stored in-memory (so every restart is a fresh start!).

---

## 🌐 Base URLs

-   **API:** `http://localhost:5000/api/`
-   **Frontend:** `http://localhost:5000/`

---

## 🔗 API Endpoints

### 1️⃣ Create User

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

### 2️⃣ Login User

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

### 3️⃣ Show All Users

-   **URL:** `/api/users`
-   **Method:** `GET`
-   **Response:**
    -   `200 OK`: List of all usernames
        ```json
        { "users": ["user1", "user2", ...] }
        ```

---

## 🎨 Frontend Endpoints

Enjoy a clean, Bootstrap-powered web interface:

-   `/` — Home page 🏠
-   `/register` — Register a new user 📝
-   `/login` — Login as a user 🔑
-   `/users` — Show all users 👥

---

## 💡 Notes

-   All API endpoints accept and return JSON.
-   User data is **not persistent** and will be lost when the server restarts. (Perfect for demos and learning!)
-   For persistent storage, check out the database-backed version.

---

✨ For more details, see the main application code and the `templates` folder. Happy coding! ✨
