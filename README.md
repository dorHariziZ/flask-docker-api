# 🚀 CRUD API Server with Docker

This repository contains a **simple CRUD API server** built with **Flask**, running inside a **Docker container**. 
The server provides basic **Create, Read, Update, and Delete (CRUD)** operations and logs received data.

---

## **📌 Project Overview**
### **Goals**
✅ Implement a basic **CRUD API**.  
✅ Run the API inside a **Docker container**.  
✅ Use **Flask** for lightweight API handling.  
✅ Enable easy deployment & scalability.  

---

## **📡 API Endpoints**
| Method | Endpoint             | Description                |
|--------|----------------------|----------------------------|
| `POST` | `/create`            | Create a new item         |
| `GET`  | `/read/<item_id>`     | Retrieve an item by ID    |
| `PUT`  | `/update/<item_id>`   | Update an item by ID      |
| `DELETE` | `/delete/<item_id>` | Delete an item by ID      |

**Response:**  
- **`200 OK`** → Request successful  
- **`400 Bad Request`** → Data missing  

---

## **⚙️ Project Structure**
```
flask-docker-api/
│── vendor/                # Pre-installed Python dependencies (Flask)
│── Dockerfile             # Docker instructions to build the API container
│── server.py              # Main Flask application (API logic)
│── requirements.txt       # Python dependencies
│── README.md              # Documentation
```

---

## **🛠️ Setup & Running**
### **🚀 Run Locally (Without Docker)**
1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
2. **Run the Flask server**:
   ```bash
   python server.py
   ```
3. **Test API in Postman or `curl`**:
   ```bash
   curl -X POST http://127.0.0.1:5000/create -H "Content-Type: application/json" -d '{"name": "item"}'
   ```

---

### **🐳 Running with Docker**
1️⃣ **Build the Docker image**:
   ```bash
   docker build -t flask-server-docker:1.0 .
   ```

2️⃣ **Run the container**:
   ```bash
   docker run -p 5001:5000 flask-server-docker:1.0
   ```

3️⃣ **Access API in Postman** at:
   ```
   http://127.0.0.1:5001
   ```