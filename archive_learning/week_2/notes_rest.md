# REST Fundamentals – Practical Notes

## 1. What is REST

REST (Representational State Transfer) is a way to design APIs so that:

- Everything is treated as a **resource**
- Resources are accessed using **URLs**
- Actions are performed using **HTTP methods**

👉 Think of REST like a restaurant menu:

- URL = menu item
- HTTP method = what you want to do with it

---

## 2. HTTP Methods (Core Ones)

### GET

- Used to **fetch data**
- Does NOT change anything on the server

Example: GET /users/1  
→ Get details of user with id 1

---

### POST

- Used to **create new data**
- Sends data to the server

Example: POST /users  
→ Create a new user

---

### PUT

- Used to **update existing data**
- Replaces the full resource

Example: PUT /users/1  
→ Update user with id 1

---

### DELETE

- Used to **remove data**

Example: DELETE /users/1  
→ Delete user with id 1

---

## 3. HTTP Status Codes (Must-Know)

### 200 – OK

- Request successful
- Mostly used with GET, PUT, DELETE

---

### 201 – Created

- Resource created successfully
- Mostly used with POST

---

### 400 – Bad Request

- Client sent invalid data
- Example: missing required fields

---

### 401 – Unauthorized

- Authentication missing or invalid
- Example: no token, expired token

---

### 403 – Forbidden

- Authenticated but **not allowed**
- Example: user role not permitted

---

### 404 – Not Found

- Resource does not exist
- Example: wrong URL or ID

---

### 500 – Internal Server Error

- Server failed unexpectedly
- Not a client mistake

---

## 4. Request vs Response

### Request (Client → Server)

Contains:

- HTTP method (GET, POST, etc.)
- URL
- Headers (auth, content-type)
- Body (only for POST/PUT)

Example: POST /users  
Body: { "name": "Bunny", "role": "Tester" }

---

### Response (Server → Client)

Contains:

- Status code
- Headers
- Body (data or error)

Example: 201 Created  
Body: { "id": 1, "name": "Bunny" }

---

## Quick Tester Mindset

- Verify correct HTTP method
- Validate status code
- Check response body
- Ensure errors are meaningful
