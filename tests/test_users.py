import pytest
from fastapi.testclient import TestClient
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException
from src.main import app  
from src.schemas import UserCreate, UserResponse
from src.db import get_session 
from src.models import User


@pytest.fixture
def client():
    with TestClient(app) as client:
        yield client


@pytest.fixture
def mock_db():
  
    pass


@pytest.mark.asyncio
async def test_create_user(client: TestClient, mock_db: AsyncSession):
    user_data = {"name": "Test User", "email": "testuser@example.com"}
    
    
    response = await client.post("/users/", json=user_data)
    
    assert response.status_code == 200
    assert response.json()["name"] == user_data["name"]
    assert response.json()["email"] == user_data["email"]


@pytest.mark.asyncio
async def test_get_user(client: TestClient, mock_db: AsyncSession):
    user_data = {"name": "Test User", "email": "testuser@example.com"}
    
    created_user = await users.create_user(mock_db, name=user_data["name"], email=user_data["email"])
    
    response = await client.get(f"/users/{created_user.id}")
    
    assert response.status_code == 200
    assert response.json()["id"] == created_user.id
    assert response.json()["name"] == user_data["name"]
    assert response.json()["email"] == user_data["email"]


@pytest.mark.asyncio
async def test_get_users(client: TestClient, mock_db: AsyncSession):
    user_data1 = {"name": "Test User 1", "email": "testuser1@example.com"}
    user_data2 = {"name": "Test User 2", "email": "testuser2@example.com"}
    
    await users.create_user(mock_db, name=user_data1["name"], email=user_data1["email"])
    await users.create_user(mock_db, name=user_data2["name"], email=user_data2["email"])
    
    response = await client.get("/users/")
    
    assert response.status_code == 200
    users_list = response.json()
    assert len(users_list) >= 2
    assert users_list[0]["name"] == user_data1["name"]
    assert users_list[1]["name"] == user_data2["name"]


@pytest.mark.asyncio
async def test_update_user(client: TestClient, mock_db: AsyncSession):
    user_data = {"name": "Test User", "email": "testuser@example.com"}
    
    created_user = await users.create_user(mock_db, name=user_data["name"], email=user_data["email"])
    
    updated_data = {"name": "Updated User", "email": "updateduser@example.com"}
    
    response = await client.put(f"/users/{created_user.id}", json=updated_data)
    
    assert response.status_code == 200
    assert response.json()["id"] == created_user.id
    assert response.json()["name"] == updated_data["name"]
    assert response.json()["email"] == updated_data["email"]


@pytest.mark.asyncio
async def test_delete_user(client: TestClient, mock_db: AsyncSession):
    user_data = {"name": "Test User", "email": "testuser@example.com"}
    
    created_user = await users.create_user(mock_db, name=user_data["name"], email=user_data["email"])
    
    response = await client.delete(f"/users/{created_user.id}")
    
    assert response.status_code == 200
    assert response.json()["id"] == created_user.id
    assert response.json()["name"] == user_data["name"]
    assert response.json()["email"] == user_data["email"]
    
    response = await client.get(f"/users/{created_user.id}")
    assert response.status_code == 404


@pytest.mark.asyncio
async def test_create_user_invalid_email(client: TestClient):
    user_data = {"name": "Invalid User", "email": "invalid_email"}
    
    response = await client.post("/users/", json=user_data)
    
    assert response.status_code == 422  
