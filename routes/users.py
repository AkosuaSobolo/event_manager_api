from fastapi import APIRouter, Form, HTTPException, status
from typing import Annotated
from pydantic import EmailStr
from db import users_collection
import bcrypt
import jwt
import os


# Create users' router
user_router = APIRouter()



# Define endpoints
@user_router.post("/users/register")
def register_user(
    username: Annotated[str, Form()],
    email: Annotated[EmailStr, Form()],
    password: Annotated[str, Form(min_length=8)]
):
    # Ensure user doesn't already exist
    user_count = users_collection.count_documents(filter={"email": email})
    if user_count > 0: 
        raise HTTPException(status.HTTP_409_CONFLICT, "Sorry, user already exists!")
    # Hash user password
    hashed_password = bcrypt.hashpw(bytes(password.encode("utf-8")), bcrypt.gensalt())
    # Save user to database
    users_collection.insert_one({
        "username": username,
        "email": email,
        "password": hashed_password.decode("utf-8")
    })
    # Return response
    return {"message": "User registered successfully!"}

# Let user log in
@user_router.post("/users/login")
def login_user(
    email: Annotated[EmailStr, Form()],
    password: Annotated[str, Form(min_length=8)]
):
    # Find user in database
    user_in_db = users_collection.find_one(filter={"email": email})
    if not user_in_db:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Email or Passwork not found!")
    
    # Compare and verify password
    stored_hashed = user_in_db["password"]
    if not bcrypt.checkpw(password.encode("utf-8"), stored_hashed.encode("utf-8")):
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, "Invalid credentials. Try again!")
    # Generate for them an access token
    encoded_jwt = jwt.encode({"id": str(user_in_db["_id"])}, os.getenv("JWT_SECRET_KEY"), "HS256")

    # Return response 
    return {"message": "Login successful!",
            "access_token": encoded_jwt}

