import pytest

from models.client import ClientModel


def test_login_success(client, db_session):
    # Create client with plain-text password
    client_model = ClientModel(name="Test", lastname="User", email="login@test.com", telephone="+123", password="mypassword")
    db_session.add(client_model)
    db_session.commit()

    resp = client.post("/auth/login", json={"email": "login@test.com", "password": "mypassword"})
    assert resp.status_code == 200
    data = resp.json()
    assert "token" in data
    assert "user" in data
    assert data["user"]["email"] == "login@test.com"


def test_login_wrong_password(client, db_session):
    client_model = ClientModel(name="Test", lastname="User", email="login2@test.com", telephone="+123", password="correct")
    db_session.add(client_model)
    db_session.commit()

    resp = client.post("/auth/login", json={"email": "login2@test.com", "password": "wrong"})
    assert resp.status_code == 401
