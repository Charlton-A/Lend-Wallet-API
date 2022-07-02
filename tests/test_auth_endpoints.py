import imp
import pytest
import requests


@pytest.mark.integration
def test_profile():
    BASE_URL = "http://localhost:8003"
    login_url = BASE_URL + "/api/v1/login"
    profile_url = BASE_URL + "/api/v1/profile"
    login_response = requests.post(login_url,
                                   json={
                                       "username": "test_user",
                                       "password": "password",
                                   })
    assert login_response.status_code == 200
    if login_response.status_code == 200:
        token = login_response.json()["token"]
        resp = requests.get(profile_url, headers={"X-LEND-TOKEN": token})
        assert resp.status_code == 200
