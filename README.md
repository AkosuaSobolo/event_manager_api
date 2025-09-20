# event_manager_api

A college event management API developed using Fast API

# FastAPI + MongoDB Event Manager App

This project is a **FastAPI + MongoDB** application for managing events with user authentication. It allows registered users to create, update, delete, and view events. Event flyers are uploaded and stored via **Cloudinary** for easy image hosting.

## Features

1. User registration & login with JWT authentication
2. Create new events with flyer upload to Cloudinary
3. Retrieve all events with search, filters, and pagination
4. Retrieve a single event by ID
5. Update event details and replace flyers
6. Delete events securely
7. Built with FastAPI for speed and scalability

## Tech Stack

1. Backend Framework: FastAPI
2. Database: MongoDB
3. Authentication: JWT (JSON Web Tokens)
4. Password Hashing: bcrypt
5. File Storage: Cloudinary
6. Environment Management: python-dotenv

## How to Run

1. Clone/download this project
2. Install dependencies: `pip install -r requirements.txt`
3. Set up `.env` file in the project root:

```
CLOUDINARY_CLOUD_NAME=your_cloud_name
CLOUDINARY_API_KEY=your_api_key
CLOUDINARY_API_SECRET=your_api_secret
MONGO_URI=mongodb://localhost:27017
JWT_SECRET_KEY=your_secret_key
```

4. Start the server: `fastapi dev`
   
5. Open your browser or Postman at: http://127.0.0.1:8000/docs

## Endpoints

Note: All create and update endpoints use **form-data** (not raw JSON), since they are implemented with `Annotated[str, Form(...)]`.

### Home

`GET /`
Response:

```json
{"message": "You are on the home page"}
```

---

## User Authentication

### Register User

`POST /users/register`
**Request (form-data):**

```json
{
  "username": "John Doe",
  "email": "john@example.com",
  "password": "StrongPass123"
}
```

Response:

```json
{"message": "User registered successfully!"}
```

### User Login

`POST /users/login`
Request (form-data):

```json
{
  "email": "john@example.com",
  "password": "StrongPass123"
}
```

Response:

```json
{
  "message": "Login successful!",
  "access_token": "your_jwt_token"
}
```

## Event Management

### Get All Events

`GET /events?title=&description=&limit=10&skip=0`

Example request:
`GET /events?title=Tech&limit=2`

Example response:

```json
[
  {
    "title": "Tech Conference",
    "date": "2025-09-22",
    "location": "Accra",
    "description": "Annual tech conference"
  },
  {
    "title": "Music Festival",
    "date": "2025-10-10",
    "location": "Accra",
    "description": "Live music and performances"
  }
]
```

### Create Event

`POST /events`
Requires Authentication

Request (form-data):

* title: string
* description: string
* flyer: file (image)

Response:

```json
{"message": "Event added successfully"}
```

### Get Event by ID

`GET /events/{event_id}`

Response:

```json
{
  "title": "Tech Conference",
  "date": "2025-09-22",
  "location": "Accra",
  "description": "Annual tech conference"
}
```

### Update Event

`PUT /events/{event_id}`

Request (form-data):

```
title=Updated Tech Summit
location=Kumasi
```

Response:

```json
{"message": "Event replaced successfully"}

### Delete Event

`DELETE /events/{event_id}`
Requires Authentication

**Response:**

```json
{"message": "Event deleted successfully"}
```

## Error Handling

* Invalid MongoDB ID → **422 Unprocessable Entity**
* Event not found → **404 Not Found**
* Duplicate event per user → **409 Conflict**
* Unauthorized / Invalid token → **401 Unauthorized**
* Database error → **500 Internal Server Error**



## Extra Challenge

* Added flyer upload to Cloudinary
* Implemented JWT authentication for secure access
* Added filtering, skip, and limit (pagination) for `/events`



## Future Improvements

1. User Profiles: Link events to user dashboards
2. Event Categories & Tags: Filter events by categories
3. RSVP System: Enable attendees to register for events
4. Notification System: Email reminders for upcoming events
5. Frontend UI: Build a React/Vue interface for event management
6. Testing & CI/CD: Add pytest unit tests and GitHub Actions
7. Deployment: Dockerize and deploy on Render/Railway for live demos
