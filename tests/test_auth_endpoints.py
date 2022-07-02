import pytest
import requests


@pytest.mark.integration
def test_profile():
    BASE_URL = "http://localhost:8003"
    login_url = BASE_URL + "/api/v1/login"
    profile_url = BASE_URL + "/api/v1/profile"
    creds = {
        "username": "test_user",
        "password": "test",
    }

    login_response = requests.post(login_url, json=creds)
    assert login_response.status_code == 200
    if login_response.status_code == 200:
        token = login_response.json()["token"]
        resp = requests.get(profile_url, headers={"X-LEND-TOKEN": token})
        assert resp.status_code == 200
        user_data = resp.json()
        assert user_data["currency"] == "KES"


@pytest.mark.integration
def test_filter_by_date():
    BASE_URL = "http://localhost:8003"
    login_url = BASE_URL + "/api/v1/login"
    profile_url = BASE_URL + "/api/v1/filter/date"
    creds = {
        "username": "test_user",
        "password": "test",
    }
    login_response = requests.post(login_url, json=creds)
    assert login_response.status_code == 200
    if login_response.status_code == 200:
        token = login_response.json()["token"]
        resp = requests.get(profile_url, headers={"X-LEND-TOKEN": token})
        assert resp.status_code == 200
        txn_data = resp.json()
        assert txn_data["user"] == "test_user"
